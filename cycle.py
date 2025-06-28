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