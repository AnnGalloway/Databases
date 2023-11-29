from lib.cohort_repository import *
from lib.database_connection import *

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed('seeds/student_directory_2.sql')
    
    def run(self):
        print('Which cohort would you like to view? \n')
        response = input('Enter your choice: ')
        cohort = CohortRepository(self._connection)
        print('\n')
        print(cohort.find_with_students(response))

if __name__ == '__main__':
    app = Application()
    app.run()