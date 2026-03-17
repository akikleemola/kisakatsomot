import db
def add_place(title, address, city, description, user_id):
    sql = """INSERT INTO places (title, address, city, description, user_id)
            VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, address, city, description, user_id])

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
    return db.query(sql, [place_id])[0]

def update_place(place_id, title, address, city, description):
    sql = """UPDATE places SET title = ?,
                                address = ?,
                                city = ?,
                                description = ? 
                            WHERE id = ?"""
    db.execute(sql, [title, address, city, description, place_id])