#!/usr/bin/python3

'''
Python MySQL - mysql-connector 驱动
'''
'''
MySQL 是最流行的关系型数据库管理系统，如果你不熟悉 MySQL，可以阅读我们的 MySQL 教程。

本章节我们为大家介绍使用 mysql-connector 来连接使用 MySQL， mysql-connector 是 MySQL 官方提供的驱动器。

我们可以使用 pip 命令来安装 mysql-connector：

python -m pip install mysql-connector
使用以下代码测试 mysql-connector 是否安装成功：

demo_mysql_test.py:
import mysql.connector
执行以上代码，如果没有产生错误，表明安装成功。

注意：如果你的 MySQL 是 8.0 版本，密码插件验证方式发生了变化，早期版本为 mysql_native_password，8.0 版本为 caching_sha2_password，所以需要做些改变：

先修改 my.ini 配置：

[mysqld]
default_authentication_plugin=mysql_native_password
然后在 mysql 下执行以下命令来修改密码：

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '新密码';
'''

import mysql.connector


# mydb = mysql.connector.connect(
#     host="localhost",  # 数据库主机地址
#     user="root",  # 数据库用户名
#     passwd="1"  # 数据库密码
# )
#
# print(mydb)

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="1"
# )
#
# mycursor = mydb.cursor()
#
#
# # mycursor.execute("CREATE DATABASE runoob_db")
# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#     print(x)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1",
    database="runoob_db",
    buffered = True
)

mycursor = mydb.cursor()

try:
    sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites
    mycursor.execute(sql)
except:
    print('fail to drop table')

# 输出所有数据库列表
mycursor.execute('SHOW DATABASES')
for x in mycursor:
    print(x)

mycursor.execute("show databases like 'runoob_db'")
for x in mycursor:
    print(x)
    if x is not None:
        flag = True

if flag == False:
    # 创建数据库
    mycursor.execute("CREATE DATABASE runoob_db")
    print('crate runoob_db')
else:
    print('runoob_db exist')
'''
或者我们可以直接连接数据库，如果数据库不存在，会输出错误信息：

demo_mysql_test.py:
import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="runoob_db"
)
'''



'''
创建数据表
创建数据表使用 "CREATE TABLE" 语句，创建数据表前，需要确保数据库已存在，以下创建一个名为 sites 的数据表
'''
try:
    mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
except:
    print('sites already exist')

# 我们也可以使用 "SHOW TABLES" 语句来查看数据表是否已存在
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)







'''
主键设置
创建表的时候我们一般都会设置一个主键（PRIMARY KEY），我们可以使用 "INT AUTO_INCREMENT PRIMARY KEY" 语句来创建一个主键，主键起始值为 1，逐步递增。
如果我们的表已经创建，我们需要使用 ALTER TABLE 来给表添加主键
'''
try:
    mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
except:
    print('PRIMARY KEY already exist')

# 如果你还未创建 sites 表，可以直接使用以下代码创建
# try:
#     mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")
# except:
#     print('PRIMARY KEY already exist')



'''
插入数据
插入数据使用 "INSERT INTO" 语句
'''
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("RUNOOB", "https://www.runoob.com")
mycursor.execute(sql, val)

mydb.commit()  # 数据表内容有更新，必须使用到该语句

print(mycursor.rowcount, "记录插入成功。")




'''
批量插入
批量插入使用 executemany() 方法，该方法的第二个参数是一个元组列表，包含了我们要插入的数据：
'''
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
    ('Google', 'https://www.google.com'),
    ('Github', 'https://www.github.com'),
    ('Taobao', 'https://www.taobao.com'),
    ('stackoverflow', 'https://www.stackoverflow.com/')
]

mycursor.executemany(sql, val)

mydb.commit()  # 数据表内容有更新，必须使用到该语句

print(mycursor.rowcount, "记录插入成功。")


# 如果我们想在数据记录插入后，获取该记录的 ID ，可以使用以下代码
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("Zhihu", "https://www.zhihu.com")
mycursor.execute(sql, val)

mydb.commit()

print("1 条记录已插入, ID:", mycursor.lastrowid)




'''
查询数据
查询数据使用 SELECT 语句
'''
mycursor.execute("SELECT * FROM sites")

myresult = mycursor.fetchall()  # fetchall() 获取所有记录

for x in myresult:
    print(x)

print('# 也可以读取指定的字段数据')
mycursor.execute("SELECT name, url FROM sites")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


print('如果我们只想读取一条数据，可以使用 fetchone() 方法')
mycursor.execute("SELECT * FROM sites")
myresult = mycursor.fetchone()
print(myresult)





'''
where 条件语句
'''
print('如果我们要读取指定条件的数据，可以使用 where 语句')

sql = "SELECT * FROM sites WHERE name ='RUNOOB'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print(' 也可以使用通配符 %')
sql = "SELECT * FROM sites WHERE url LIKE '%oo%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


print('为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义查询的条件')
sql = "SELECT * FROM sites WHERE name = %s"
na = ("RUNOOB",)
mycursor.execute(sql, na)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)





'''
排序
'''
print('查询结果排序可以使用 ORDER BY 语句，默认的排序方式为升序，关键字为 ASC，如果要设置降序排序，可以设置关键字 DESC')
sql = "SELECT * FROM sites ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print('降序排序实例')
sql = "SELECT * FROM sites ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)



'''
Limit
'''
print('如果我们要设置查询的数据量，可以通过 "LIMIT" 语句来指定')
mycursor.execute("SELECT * FROM sites LIMIT 3")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print('也可以指定起始位置，使用的关键字是 OFFSET')
mycursor.execute("SELECT * FROM sites LIMIT 3 OFFSET 1")  # 0 为 第一条，1 为第二条，以此类推
myresult = mycursor.fetchall()
for x in myresult:
    print(x)




'''
删除记录
'''
print('删除记录使用 "DELETE FROM" 语句')
sql = "DELETE FROM sites WHERE name = 'stackoverflow'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, " 条记录删除")



# 注意：要慎重使用删除语句，删除语句要确保指定了 WHERE 条件语句，否则会导致整表数据被删除。
print('为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义删除语句的条件')
sql = "DELETE FROM sites WHERE name = %s"
na = ("stackoverflow",)
mycursor.execute(sql, na)
mydb.commit()
print(mycursor.rowcount, " 条记录删除")





'''
更新表数据
'''
print('数据表更新使用 "UPDATE" 语句')
sql = "UPDATE sites SET name = 'ZH' WHERE name = 'Zhihu'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, " 条记录被修改")
# 注意：UPDATE 语句要确保指定了 WHERE 条件语句，否则会导致整表数据被更新。

print('为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义更新语句的条件')
sql = "UPDATE sites SET name = %s WHERE name = %s"
val = ("Zhihu", "ZH")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, " 条记录被修改")




'''
删除表
'''
print('删除表使用 "DROP TABLE" 语句， IF EXISTS 关键字是用于判断表是否存在，只有在存在的情况才删')
sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites
mycursor.execute(sql)







