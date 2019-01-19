import pymysql
import openpyxl

class Database:

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='')

    def reset_database(self):
        try:
            self.conn.cursor().execute('DROP DATABASE project')
        except:
            print(">>> Required database not found....")
            print(">>> Creating new database")
        self.conn.cursor().execute('CREATE DATABASE project')
        self.conn.cursor().execute('CREATE TABLE PROJECT.auth_user(USER_ID INTEGER, REG_NO VARCHAR(20), CAR_MODEL VARCHAR(20),NAME VARCHAR(40),PHONE_NO VARCHAR(15),DEPT_ID INTEGER)')
        self.conn.cursor().execute('CREATE TABLE PROJECT.department(DEPT_ID INTEGER,DEPT_NAME VARCHAR(50))')
        print(">>> Database has been reset to empty")

    def load_data(self):
        # Open excel book and read the content to the database
        pass

    def reset_auth_users(self):
        # Drop the existing PROJECT.AUTH_USERS and recreate the table
        pass

    def reset_department(self):
        # Drop the existing PROJECT.DEPARTMENT and recreate the table
        pass

    def load_auth_users_manually(self):
        # Read the content from the terminal
        pass

    def load_auth_users_automatically(self):
        # Read the workbook sheet1 only to the database
        pass

    def load_department_manually(self):
        # Read the content from the terminal
        pass

    def load_department_automatically(self):
        # Read the workbook sheet2 only to the database
        pass

    def troubleshoot_problems(self):
        # Check if the database is in working state or not
        pass

    def resolve_problems(self):
        # Resolve the problem associated to the database
        pass


database = Database()
database.reset_database()
