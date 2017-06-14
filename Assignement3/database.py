import pymysql

db = pymysql.connect("localhost","root","root","flask" )
cursor = db.cursor()

sql = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,  
   SEX CHAR(1),
   INCOME FLOAT )"""

cursor.execute(sql)

sql1 = """INSERT INTO EMPLOYEE(FIRST_NAME,
   LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Smit', 'Shah', 24, 'M', 20000)"""

sql2 = """INSERT INTO EMPLOYEE(FIRST_NAME,
   LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Nix', 'patel', 20, 'M', 25000)"""

sql3 = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)

sql4 = "UPDATE EMPLOYEE SET AGE = AGE + 1 \
                          WHERE SEX = '%c'" % ('M')



try:
   # Execute the SQL command
   cursor.execute(sql1)
   cursor.execute(sql2)
   cursor.execute(sql3)
   results = cursor.fetchall()
   for row in results:
       fname = row[0]
       lname = row[1]
       age = row[2]
       sex = row[3]
       income = row[4]

   print("fname = %s,lname = %s,age = %d,sex = %s,income = %d" % (fname, lname, age, sex, income))
   # Commit your changes in the database
   cursor.execute(sql4)

   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()






# disconnect from server
db.close()