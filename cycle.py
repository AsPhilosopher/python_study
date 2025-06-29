i = 0
while i < 5:
    print("Hello Pyhon!")
    i += 1

print("循环结束, i = %d" % i)

i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1

print("1~100的和为: %d" % sum)

i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1

print("1~100的偶数和为: %d" % sum)

i = 0
while i < 10:
    if i == 6:
        i += 1
        continue
    print(i)
    if i == 8:
        break
    i += 1

row = 1
while row <= 5:
    print("*" * row)
    row += 1

row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    print("")
    row += 1

row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d" % (row, col, row * col), end="\t")
        col += 1
    print("")
    row += 1

print("123455\t12345678\t123")
print("5678\t123\t\t888")
print("5678\t123\t888")

# \r 是 回车符 （Carriage Return），表示将光标移动到当前行的开头。后续字符会覆盖当前行已有的内容。
# 输出：5674
print("1234\r567")