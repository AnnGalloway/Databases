from lib.student import *
from lib.cohort import *
from lib.cohort_repository import *
October = 'October'

def test_find_with_students(db_connection):
    db_connection.seed('seeds/student_directory_2.sql')
    repository = CohortRepository(db_connection)
    cohort = repository.find_with_students(1)
    assert cohort == Cohort(1, October, '2023-10-30', [
        Student(1, 'person1', 1),
        Student(2, 'person2', 1),
        Student(3, 'person3', 1)
    ])