import db
def add_place(title, address, city, description, user_id):
    sql = """INSERT INTO places (title, address, city, description, user_id)
            VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, address, city, description, user_id])

def get_places():
    sql = "SELECT id, title FROM places ORDER BY id DESC"
    return db.query(sql)

def get_place(place_id):
    sql = """SELECT places.title,
                    places.address,
                    places.city,
                    places.description,
                    users.username
            FROM places, users
            WHERE places.user_id = users.id AND
                    places.id = ?"""
    return db.query(sql, [place_id])[0]