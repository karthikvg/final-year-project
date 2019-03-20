import pymysql
import openpyxl
from helpers import *

class Database:

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='')

    def reset_database(self):
        # Resets the database to normal state
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
        self.load_auth_users_automatically()
        self.load_department_automatically()
        pass

    def reset_auth_users(self):
        # Drop the existing PROJECT.AUTH_USERS and recreate the table
        self.conn.cursor().execute('DROP TABLE PROJECT.auth_user')
        self.conn.cursor().execute('CREATE TABLE PROJECT.auth_user(USER_ID INTEGER, REG_NO VARCHAR(20), CAR_MODEL VARCHAR(20),NAME VARCHAR(40),PHONE_NO VARCHAR(15),DEPT_ID INTEGER)')
        print(">>> auth_users has been reset to empty state")
        pass

    def reset_department(self):
        # Drop the existing PROJECT.DEPARTMENT and recreate the table
        self.conn.cursor().execute('DROP TABLE PROJECT.department')
        self.conn.cursor().execute('CREATE TABLE PROJECT.department(DEPT_ID INTEGER,DEPT_NAME VARCHAR(50))')
        print(">>> department table has been reset to empty state")
        pass

    def load_auth_users_manually(self):
        # Read the content from the terminal
        row=input(">>> Enter values with comma seperated as --- id,reg_no,car_model,name,phone_no,dept_id\n")
        sql="INSERT INTO PROJECT.auth_user values("+row+")"
        print(sql)
        self.conn.cursor().execute(sql)
        self.conn.commit()
        print("query successful")
        pass

    def load_auth_users_automatically(self):
        # Read the workbook sheet1 only to the database
        wb = openpyxl.load_workbook(WORKBOOK_PATH)
        sheet = wb['Sheet1']

        for i in range(2,sheet.max_row):
            data= str(sheet[i][0].value)+str(",'"+sheet[i][1].value+"'")+str(",'"+sheet[i][2].value+"'")+str(",'"+sheet[i][3].value+"'")+str(",'"+str(sheet[i][4].value)+"',")+str(sheet[i][5].value)
            #print(data)
            sql="INSERT INTO PROJECT.auth_user values("+data+")"
            print(sql)
            self.conn.cursor().execute(sql)
            self.conn.commit()
        pass

    def load_department_manually(self):
        # Read the content from the terminal
        pass

    def load_department_automatically(self):
        # Read the workbook sheet2 only to the database
        pass

    def check(self,reg_no):
        # Checks if a record exists or not in the database
        sql="select * from PROJECT.auth_user where REG_NO like '%"+reg_no+"%';"
        result=self.conn.cursor().execute(sql)
        return result
        pass

database = Database()
database.reset_database()
database.load_auth_users_automatically()
#database.reset_database()
#database.load_auth_users_manually()

def query(number):
    # Check if the car is registered or not
    return database.check(number)