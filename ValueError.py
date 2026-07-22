try:
    age=int(input())
    if age<0:
        raise ValueError("年龄不能小于0")
    print("年纪合法")

except ValueError:
    print("年龄不能小于0")


