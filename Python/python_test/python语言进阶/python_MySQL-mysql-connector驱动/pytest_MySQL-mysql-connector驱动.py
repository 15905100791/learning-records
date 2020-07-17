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



