from lib.cohort import *
from lib.student import *

class CohortRepository:

    def __init__(self,connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM cohorts'
        )
        cohorts = []
        for row in rows:
            item = Cohort(row['id'], row['name'], row['starting_date'])
            cohorts.append(item)
        return cohorts

    def find_with_students(self,cohort_id):
        rows = self._connection.execute(
            'SELECT cohorts.id AS cohort_id, cohorts.name AS cohort_name, cohorts.starting_date, students.id AS student_id, students.name AS student_name '\
            'FROM cohorts JOIN students on cohorts.id = students.cohort_id '\
            'WHERE cohorts.id = %s', [cohort_id])
        students = []
        for row in rows:
            student = Student(row['student_id'], row['student_name'], row['cohort_id'])
            students.append(student)
        print(students)
        
        print(Cohort(rows[0]['cohort_id'], rows[0]['cohort_name'], rows[0]['starting_date'],students))
        return Cohort(rows[0]['cohort_id'],rows[0]['cohort_name'], rows[0]['starting_date'], students)