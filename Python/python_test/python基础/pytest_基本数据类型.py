#!/usr/bin/python3


'''
Python3 基本数据类型
'''

'''
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

等号（=）用来给变量赋值。

等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。
'''

counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串

print (counter)
print (miles)
print (name)

'''
多个变量赋值
Python允许你同时为多个变量赋值。
'''

a = b = c = 1
print('a = b = c = 1 :', 'a=', a, 'b=', b, 'c=', c)
# 以上实例，创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。
# 也可以为多个对象指定多个变量。例如：

a, b, c = 1, 2, "runoob"
print('a, b, c = 1, 2, "runoob" :', 'a=', a, 'b=', b, 'c=', c)
# 以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。



'''
标准数据类型
Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
'''

# 变量对应的值中的数据是不能被修改，如果修改就会生成一个新的值从而分配新的内存空间。
a = 1
print(id(a))
a = 2
print(id(a))

# 变量对应的值中的数据可以被修改，但内存地址保持不变。
print('追加修改地址不会变：')
name = ['qwe', 'asd', 'zxc']
print(id(name))
name.append('aaa')
print(id(name))

print('重新赋值的话地址会变：')
name = ['qwe', 'asd', 'zxc']
print(id(name))
name = ['qqq', 'www', 'aaa']
print(id(name))




'''
Number（数字）
Python3 支持 int、float、bool、complex（复数）。

在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。

像大多数语言一样，数值类型的赋值和计算都是很直观的。

内置的 type() 函数可以用来查询变量所指的对象类型。
'''
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

# 此外还可以用 isinstance 来判断
a = 100
print(isinstance(a, int))

'''
isinstance 和 type 的区别在于：

type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
'''
class A:
    pass

class B(A):
    pass

print(isinstance(A(), A))
print(type(A()) == A)
print(isinstance(B(), A))
print(type(B()) == A)

'''
当你指定一个值时，Number 对象就会被创建：

var1 = 1
var2 = 10
您也可以使用del语句删除一些对象引用。

del语句的语法是：

del var1[,var2[,var3[....,varN]]]
您可以通过使用del语句删除单个或多个对象。例如：

del var
del var_a, var_b
'''





