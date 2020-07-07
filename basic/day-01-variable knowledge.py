a = 10
b = 20
print(a + b)


aa = 1,2,3,4,5
print(aa)


a,b,c,d = [1,2,3,4]
print(a)
print(b)
print(c)
print(d)


aaaa = {"name":"地瓜花","age":"20","city":"上海"}
print(aaaa["city"])


a = (1,2,3,4,5,6,7,8,9,0)

x,*y = a
print(x)
print(y)

b,c,d,*e = a
print(b)
print(c)
print(d)
print(e)

b = [0,1,2,3,4,5,6,7,8,9]
b[8] = 100
print(b)
print(b[8])
print(b)


c = [1,2,3,4,5,6,7,8,9]
c[7] = 99
print(c)
print( c [7])

print(10 % 20)
print(10 // 20)
print(2**3)
print(2**5)
print(10==20)
print(2!=2)



a = 1
b = 2
c = a + b
print(c)

d = 1/2
print(d)

a = 1
b = 2
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a >= b)
print(a <= b)

print(a == b and a < b)
print(a != b or a > b)


a = 1
b = 1
# a = a + b
# print(a)





a = 987546445464645643123163
print( a % 10)

b = a // 10
print(b)
print(b % 10)


m = ["你", "我", "他", "她", "他们", "她们"]
if "我们" in m:
    print("no")
else:
    print("0.0")


# 成绩评定
score = 25    # int(input("请输入成绩"))

if score >= 0 and score <60:
    print("不及格")
elif(score >= 60 and score <= 70):
    print("及格")
elif(score >=71 and score <= 80):
    print("良好")
elif(score >=81 and score <= 100):
    print("优秀")
else:
    print("请输入正确的成绩")


# 成绩评定
a = [20,30,50,55,44,80,90,80,100,55,77,86]

for b in a:
    if(b >=0 and b <60):
        print("不及格")
    elif(b >= 60 and b <= 70):
        print("及格")
    elif(b >=71 and b <= 80):
        print("良好")
    elif(b >= 81 and b <= 100):
        print("优秀")
    else:
        print("请输入正确的成绩")


# 求10*9*8*7.....*1的结果
s = 1
for i in range(10, 0, -1):
    s *= i
print(s)


# 猜数字
# x = True
#
# a = 89
#
# while x :
#     b = int(input("请输入数字"))
#     if(b > a):
#         print("大了")
#     elif(b < a):
#         print("小了")
#     else:
#         print("猜对了")
#         x = False


flag = True
a = 100
while flag:
    b = int(input("请输入数字"))
    if b > a:
        print("大了")
    elif b < a:
        print("小了")
    else:
        print("猜对了")
        flag = False


