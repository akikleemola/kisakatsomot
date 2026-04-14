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

CREATE Table classes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    value TEXT
);

CREATE TABLE place_classes (
    id INTEGER PRIMARY KEY,
    place_id INTEGER REFERENCES places(id),
    title TEXT,
    value TEXT
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    place_id INTEGER REFERENCES places(id),
    user_id INTEGER REFERENCES users(id),
    stars INTEGER,
    comment TEXT
);

CREATE INDEX idx_place_reviews ON reviews (place_id);