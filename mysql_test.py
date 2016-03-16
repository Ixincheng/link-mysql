# coding:utf-8
import MySQLdb

conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'root',
    db = 'mytest',
)

cur = conn.cursor()
# cur.execute("create TABLE student(id int,name VARCHAR (20),class VARCHAR (30),age VARCHAR (10))")

# cur.execute("insert into student VALUE ('2','Tom','3 year 2 class','9')")

# cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

# cur.execute("delete from student where age = '9'")
sqli = "insert into student values(%s,%s,%s,%s)"
# cur.execute(sqli,('3','Huhu','2 year 1 class','7'))
# sqld = "delete from student where name='Huhu'"
# cur.execute(sqld)
# cur.executemany(sqli,[
#     ('3','Tom','1 year 1 class','6'),
#     ('3','Jack','2 year 1 class','7'),
#     ('3','Yaheng','2 year 2 class','7'),
# ])
# aa = cur.execute("select * from student")
# print aa
# info = cur.fetchmany(aa)
# for ii in info:
#     print ii
cur.execute("select * from student")
a = cur.fetchone()
b = cur.fetchone()
c = cur.fetchone()
d = cur.fetchone()
e = cur.fetchone()

print a,b
print c,d
print e


cur.close()
conn.commit()
conn.close()
