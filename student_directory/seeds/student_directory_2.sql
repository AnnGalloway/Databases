
DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;
DROP TABLE IF EXISTS cohorts;
DROP SEQUENCE IF EXISTS cohorts_id_seq;


CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date text
);

CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int
);

INSERT INTO cohorts (name, starting_date) VALUES ('October', '30 oct');
INSERT INTO cohorts (name, starting_date) VALUES ('August', '1 aug');
INSERT INTO cohorts (name, starting_date) VALUES ('February', '1 feb');

INSERT INTO students (name, cohort_id) VALUES ('person1', 1);
INSERT INTO students (name, cohort_id) VALUES ('person2', 1);
INSERT INTO students (name, cohort_id) VALUES ('person3', 1);
INSERT INTO students (name, cohort_id) VALUES ('person4', 2);
INSERT INTO students (name, cohort_id) VALUES ('person5', 2);
INSERT INTO students (name, cohort_id) VALUES ('person6', 2);
INSERT INTO students (name, cohort_id) VALUES ('person7', 2);
INSERT INTO students (name, cohort_id) VALUES ('person8', 3);
INSERT INTO students (name, cohort_id) VALUES ('person9', 3);
INSERT INTO students (name, cohort_id) VALUES ('person10', 4);