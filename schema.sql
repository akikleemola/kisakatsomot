CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);
CREATE Table places(
    id INTEGER PRIMARY KEY,
    title TEXT,
    address TEXT,
    city TEXT,
    description TEXT,
    user_id INTEGER REFERENCES users
);