import db
def add_place(title, address, city, description, user_id, classes):
    sql = """INSERT INTO places (title, address, city, description, user_id)
             VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, address, city, description, user_id])

    place_id = db.last_insert_id()
    sql = "INSERT INTO place_classes (place_id, title, value) VALUES (?, ?, ?)"

    for class_title, class_value in classes:
        db.execute(sql, [place_id, class_title, class_value])

def get_classes(place_id):
    sql = "SELECT title, value FROM place_classes WHERE place_id = ?"
    return db.query(sql, [place_id])

def get_places():
    sql = "SELECT id, title FROM places ORDER BY id DESC"
    return db.query(sql)

def get_place(place_id):
    sql = """SELECT places.id,
                    places.title,
                    places.address,
                    places.city,
                    places.description,
                    users.id user_id,
                    users.username
            FROM places, users
            WHERE places.user_id = users.id AND
                    places.id = ?"""
    result = db.query(sql, [place_id])
    return result[0] if result else None

def update_place(place_id, title, address, city, description):
    sql = """UPDATE places SET title = ?,
                                address = ?,
                                city = ?,
                                description = ? 
                            WHERE id = ?"""
    db.execute(sql, [title, address, city, description, place_id])

def remove_place(place_id):
    sql = "DELETE FROM places WHERE id = ?"
    db.execute(sql, [place_id])

def find_places(query):
    sql = """SELECT id, title
            FROM places
            WHERE title LIKE ? OR address LIKE ? OR city LIKE ? OR description LIKE ?
            ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like, like, like])