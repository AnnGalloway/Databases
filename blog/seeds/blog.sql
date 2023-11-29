
DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comment_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;


CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text
);

CREATE SEQUENCE IF NOT EXISTS comment_id_seq;
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  content text,
  author text,
  post_id int
);

INSERT INTO posts (title, content) VALUES ('Post1', 'content1');
INSERT INTO posts (title, content) VALUES ('Post2', 'content2');
INSERT INTO posts (title, content) VALUES ('Post3', 'content3');
INSERT INTO posts (title, content) VALUES ('Post4', 'content4');


INSERT INTO comments (content, author, post_id) VALUES ('content1', 'person1', 1);
INSERT INTO comments (content, author, post_id) VALUES ('content2', 'person2', 1);
INSERT INTO comments (content, author, post_id) VALUES ('content3', 'person3', 2);
INSERT INTO comments (content, author, post_id) VALUES ('content4', 'person4', 2);
INSERT INTO comments (content, author, post_id) VALUES ('content5', 'person5', 3);
INSERT INTO comments (content, author, post_id) VALUES ('content6', 'person6', 4);
