import pymysql

db = pymysql.connect('localhost', 'root', '', 'dwit')
cursor = db.cursor()
# sql = 'create table student(id int primary key auto_increment,name varchar(30),course varchar(30),email varchar(30))' # CREATE
# sql = "insert into student(name,course,email) values('{}','{}','{}')".format('Apoorba','Python','apoorba@gmail.com')  # INSERT
# sql = "update student set name='{}',email='{}' where id={}".format('Sunil','sunil@gmail.com',4) #UPDATE
# sql = "Select * from student"
sql = 'Delete from student where id={}'.format(3)  # DELETE
cursor.execute(sql)
db.commit()
# to fetch one data
# results = cursor.fetchone()
# print(results)

# to fetch multiple data
# results= cursor.fetchall()
# for r in results:
#     print("id = {}".format(r[0]))
#     print("name = {}".format(r[1]))
#     print("course = {}".format(r[2]))
#     print("email = {}".format(r[3]))
#     print()
# print(cursor.rowcount)
db.close()