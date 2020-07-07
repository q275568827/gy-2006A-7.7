"""

# 找出299-345之间能被4整除的数字，包含299与345

for i in range(299,346):
    if (i % 4 != 0):
        continue
    print(i)

"""


# 定义一个求两个数商和余数的方法

#
# def way(a,b):
#     if(b == 0):
#         print('除数不能为0')
#     else:
#         print(a % b)  # 取余数
#         print(a // b)   # 取商
#
# way(60,0)
#
# def way1(a,b):
#     if (b == 0):
#         print('除数不能为0')
#     else:
#         print('商：', a // b, '，余', a % b )
#
# way1(60,0)


# 定义一个求两个数商和余数的方法，并调用方法到其他
# def way2(a, b):
#     if b == 0:
#         return None
#     else:
#         return (a // b, a % b)     # 定义方法


# aaa = way2(20,0)           # 定义变量(按照位置传参)

# aaa = way2(b=12, a=18)   # 定义变量(按照关键字传参,关键字位置可无序)
#
# if aaa is None:                # 调用变量/方法
#     print('参数错误')
# else:
#     print('商:', aaa[0], '余:', aaa[1])


#
# def sum1(name, *args, **kwargs):    # *args接受动态位置参数，**kwargs 接收动态关键字参数
#     print(kwargs)
#     print(name)
#     s = 0
#     for i in args:
#         s += i
#     return s
#
#
# print(sum1(1, 2, 3, 4, 5, 6, 4, 7, 8))
# print(sum1(name="孔大顺", age=18))


# def person(a, b, name, age, **kwargs):
#     print(name, age, kwargs)
#     return a*b
#
#
# print(person(a=3, b=6, name='啊啊', age=18, job='tester'))


# 面向对象
# class Calc():
#     a = None
#     b = None
#     res = None
#
#     def input(self, a, b):
#         self.a = a
#         self.b = b
#
#     def sum(self):
#         self.res = self.a + self.b
#
#     def div(self):
#         self.res = self.a / self.b
#
#     def get_result(self):
#         print(self.res)
#
#
# c = Calc()  # 类的实例化  c对象
#
# c.input(10, 20)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()


# 面向对象2
# class Calc():
#     res = None  # 类的所有实例共享
#
#     def __init__(self, a, b):  # 魔法函数，类实例化的时候调用，又称构造方法
#         self.a = a
#         self.b = b
#
#     def sum(self):
#         self.res = self.a + self.b
#
#     def div(self):
#         self.res = self.a / self.b
#
#     def get_result(self):
#         print(self.res)
#
#
# c = Calc(45, 78)
#
# c.sum()
# c.get_result()
# c.div()
# c.get_result()


# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(j, "X", i, "=", i*j, end="\t")
#     print()


# 格式化输出99
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("{}X{}={}" .format(j, i, i*j), end="\t")
#     print()


# 冒泡排序
# li = [3, 5, 7, 8, 4, 5, 45, 78, 65, 12, 45, 78, 132, 465, 46, 0]
# # length = len(li)                                    # 定义变量：长度
# # for i in range(length-1, 0, -1):                    # 以数据下标倒序循环
# #     for j in range(i):                              # 对每个下标位置数据大小做比较
# #         if li[j] > li[j+1]:                         # 若前一个下标位置数据大于后一个
# #             li[j], li[j+1] = li[j+1], li[j]         # 则交换数据位置
# # print(li)


