while True:
    number=int(input("please input a number:"))
    if number==8:
        print("恭喜你，猜对了")
        break
    elif number>8:
        print("太大了")
    else:
        print("太小了")
        break