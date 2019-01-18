import pymysql

conn = pymysql.connect(host='localhost',user='root',password='')

try:
    conn.cursor().execute('drop database pikachu')

except:
    print("error cannot be dropped")