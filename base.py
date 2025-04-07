print("-" * 10)  # 输出10个“-”
print(2**10)  # 幂运算
print(9 // 2)  # 取整数

price = 8.5
weight = 7.5
amount = price * weight
print(amount)

c = "C"
print(c)
print(type(c))
print(type(2**35))
print(type(2**100))

print(5 == True) # False
print(1 == True) # True
if 18:
    print("is True") # 输出，非零即为True

if 0:
    print("is True")
else:
    print("is False") # 输出

password = input("请输入：") # 输入都是字符串类型
print(password)

# %.2f表示保留两位小数（会四舍五入），%d表示整数，%s表示字符串，,%%输出%
print("苹果的价格为%.2f元，重量为%d斤，购买人：%s，商品好评率为%d%%" % (8.568, 7, "小明", 98))

# %10d表示输出的整数宽度为10，右对齐
print("我的年龄是%10d岁" % 1800000)

scale = 0.25
print("数据比例为：%.2f%%" % (scale * 100)) # 后面的乘法要加括号

"""
变量名需见名知义，只能由字母、下划线和数字组成
不能以数字开头，不能使用关键字，不能使用Python内置的函数和类名
变量名区分大小写

变量名小写，不同单词间，用下划线连接
"""

import keyword
print(keyword.kwlist) # 输出Python的关键字
print("\n\n\n")
import builtins
print(dir(builtins)) # 输出Python的内置函数和类名
