-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS user_accounts;
DROP SEQUENCE IF EXISTS user_accounts_id_seq;


--Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS user_accounts_id_seq;
CREATE TABLE user_accounts (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    username VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content VARCHAR(255),
    views INTEGER,
    user_account_id INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO user_accounts (email, username) VALUES ('email1@email.com', 'user1');
INSERT INTO user_accounts (email, username) VALUES ('email2@email.com', 'user2');
INSERT INTO user_accounts (email, username) VALUES ('email3@email.com', 'user3');
INSERT INTO user_accounts (email, username) VALUES ('email4@email.com', 'user4');
INSERT INTO user_accounts (email, username) VALUES ('email5@email.com', 'user5');



INSERT INTO posts (title, content, views, user_account_id) VALUES ('title1', 'content1', 4, 1);
INSERT INTO posts (title, content, views, user_account_id) VALUES ('title2', 'content2', 100, 1);
INSERT INTO posts (title, content, views, user_account_id) VALUES ('title3', 'content3', 6, 2);
INSERT INTO posts (title, content, views, user_account_id) VALUES ('title4', 'content4', 5, 3);

