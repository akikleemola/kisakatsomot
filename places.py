import db

def get_all_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)

    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)

    return classes

def add_place(title, address, city, description, user_id, classes):
    sql = """INSERT INTO places (title, address, city, description, user_id)
             VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, address, city, description, user_id])

    place_id = db.last_insert_id()

    sql = "INSERT INTO place_classes (place_id, title, value) VALUES (?, ?, ?)"

    for class_title, class_value in classes:
        db.execute(sql, [place_id, class_title, class_value])
    return place_id

def get_classes(place_id):
    sql = "SELECT title, value FROM place_classes WHERE place_id = ?"
    return db.query(sql, [place_id])

def get_places():
    sql = """
        SELECT places.id, places.title, places.city, ROUND(AVG(reviews.stars), 1) AS average_stars
        FROM places
        LEFT JOIN reviews ON places.id = reviews.place_id
        GROUP BY places.id
        ORDER BY places.id DESC
    """
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

def update_place(place_id, title, address, city, description, classes):
    sql = """UPDATE places SET title = ?,
                                address = ?,
                                city = ?,
                                description = ?
                            WHERE id = ?"""
    db.execute(sql, [title, address, city, description, place_id])

    sql = "DELETE FROM place_classes WHERE place_id = ?"
    db.execute(sql, [place_id])

    sql = "INSERT INTO place_classes (place_id, title, value) VALUES (?, ?, ?)"

    for class_title, class_value in classes:
        db.execute(sql, [place_id, class_title, class_value])

def remove_place(place_id):
    sql = "DELETE FROM reviews WHERE place_id = ?"
    db.execute(sql, [place_id])
    sql = "DELETE FROM place_classes WHERE place_id = ?"
    db.execute(sql, [place_id])
    sql = "DELETE FROM places WHERE id = ?"
    db.execute(sql, [place_id])

def find_places(query):
    sql = """SELECT id, title
            FROM places
            WHERE title LIKE ? OR address LIKE ? OR city LIKE ? OR description LIKE ?
            ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like, like, like])

def add_review(place_id, user_id, stars, comment):
    sql = """INSERT INTO reviews (place_id, user_id, stars, comment)
             VALUES (?, ?, ?, ?)"""
    db.execute(sql, [place_id, user_id, stars, comment])

def get_reviews(place_id):
    sql = """SELECT reviews.id, reviews.stars, reviews.comment, users.username, reviews.user_id
             FROM reviews
             JOIN users ON reviews.user_id = users.id
             WHERE reviews.place_id = ?"""
    return db.query(sql, [place_id])

def delete_review(review_id, user_id):
    sql = "DELETE FROM reviews WHERE id = ? AND user_id = ?"
    db.execute(sql, [review_id, user_id])

def get_review(review_id):
    sql = "SELECT id, place_id, user_id, stars, comment FROM reviews WHERE id = ?"
    result = db.query(sql, [review_id])
    return result[0] if result else None

def update_review(review_id, stars, comment, user_id):
    sql = """UPDATE reviews SET stars = ?, comment = ? WHERE id = ? AND user_id = ?"""
    db.execute(sql, [stars, comment, review_id, user_id])
