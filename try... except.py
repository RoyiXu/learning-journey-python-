try:
    num = int(input())
    print(50 / num)

except ValueError:
    print("输入错误")

except ZeroDivisionError:
    print("不能除以0")