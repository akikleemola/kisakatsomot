import random
import sqlite3

db = sqlite3.connect("database.db")

db.execute("DELETE FROM users")
db.execute("DELETE FROM places")
db.execute("DELETE FROM reviews")

user_count = 1000
place_count = 10**5
review_count = 10**6

for i in range(1, user_count + 1):
    db.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
               ["user" + str(i), "hash"])

for i in range(1, place_count + 1):
    user_id = random.randint(1, user_count)
    db.execute("""INSERT INTO places (title, address, city, description, user_id)
                  VALUES (?, ?, ?, ?, ?)""",
               ["place" + str(i), "address", "city", "description", user_id])

for i in range(1, review_count + 1):
    user_id = random.randint(1, user_count)
    place_id = random.randint(1, place_count)
    stars = random.randint(1, 5)
    db.execute("""INSERT INTO reviews (comment, stars, user_id, place_id)
                  VALUES (?, ?, ?, ?)""",
               ["review" + str(i), stars, user_id, place_id])

db.commit()
db.close()
