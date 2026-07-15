score=int(input("please input your score:"))
if score<60:
    print("不合格，需要重考")
if 60<=score<80:
    print("及格，还有提升空间")
if 80<=score<90:
    print("良好，表现不错")
if 90<=score<=100:
    print("优秀，太棒了")
if score>100:
    print("you're a good guy")