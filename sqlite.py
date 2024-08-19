import sqlite3

## Connect to SQLite
connection=sqlite3.connect("student.db");
# Create a Cursor object to insert record,create table

cursor = connection.cursor();
##create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""

cursor.execute(table_info)

##Insert Some more records

cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',95)''')
cursor.execute('''Insert Into STUDENT values('Arko','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Sreya','Data Science','A',99)''')
cursor.execute('''Insert Into STUDENT values('Parthiv','DEVOPS','B',96)''')
cursor.execute('''Insert Into STUDENT values('Manish','DEVOPS','A',90)''')

## Display ALL the records

print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)


## Commit your changes in the data base

connection.commit()
connection.close()