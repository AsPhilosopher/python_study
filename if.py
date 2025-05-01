# 缩进：tab和空格不要混用
age = int(input("请输入你的年龄："))
if age >= 18:
    print("你已经成年了，欢迎来到网吧")
else:
    print("你还未成年，回家写作业吧")

print("是否执行与判断无关")

age = 60
if age >= 18 and age <= 60:
    print("年龄正确")
    print("你已经成年了，欢迎来到网吧")

python_score = 50
c_score = 77
if python_score >= 60 or c_score >= 60:
    print("考试通过")

is_employee = False
if not is_employee:
    print("非本公司员工，请勿入内")

# 类似三目运算
result = "成年" if age >= 18 else "未成年"
print(result)

holiday = "情人节"
if holiday == "情人节":
    print("买玫瑰")
    print("看电影")
elif holiday == "平安夜":
    print("买苹果")
    print("吃大餐")

has_ticket = True
knife_length = 20
if has_ticket:
    print("车票检查通过，准备开始安检...")
    if knife_length > 20:
        print("刀长度超过20cm，需要警察处理。")
    else:
        print("安检通过，祝您旅途愉快！")
else:
    print("您没有车票，无法通过安检。")

print(bool("trUe")) # 大小写无关
print(bool("")) # 空字符串为False
print(bool(0)) # 0为False
print(bool(None)) # None为False

# 下面的写法，可读性较强
if ((1==1 and False)
        or (2==2 and False)
        or (3==3 and True)):
    print("条件成立")

import random
secret = random.randint(1, 10) # 返回1-10之间的随机数 [1, 10]
print(secret)
