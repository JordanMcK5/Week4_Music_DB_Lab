CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    artist VARCHAR(255)
);

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);