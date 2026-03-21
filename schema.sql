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
CREATE TABLE place_classes (
    id INTEGER PRIMARY KEY,
    place_id INTEGER REFERENCES places(id),
    title TEXT,
    value TEXT
);