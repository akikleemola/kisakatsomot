import db
def add_place(title, address, city, description, user_id):
    sql = """INSERT INTO places (title, address, city, description, user_id)
            VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, address, city, description, user_id])