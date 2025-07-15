def multiple_table():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d = %d" % (row, col, row * col), end="\t")
            col += 1
        print("")
        row += 1


def num1_c_num2(num1, num2):
    """
    求任意两个数的乘积
    :param num1: 第一个数
    :param num2: 第二个数
    :return: 乘积
    """
    return num1 * num2

name = "测试"