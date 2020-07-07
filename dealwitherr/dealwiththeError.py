# 异常分为 语法异常，和其他异常

# f = open('bbbbb.txt','r')    # 读取一个不存在的文件，此处为异常
# print(f.read())
# f.close()                    # 这时运行会报错

# 此时可以手动处理，处理方式如下：
# try:
#     f = open('bbbbb.txt', 'r')
#     print(f.read())
#     f.close()
# except:
#     print('文件不存在')
#
# print('操作完文件')


# def div(a, b):                    # 常识：除数不能为0，否则会报错
#     try:                          # 可以手动用try做处理
#         return a / b
#     except:                       # 若除数为0，返回空值
#         return
#
#
# print(div(10, 0))


# def div(a, b):                    # 常识：除数不能为0，否则会报错
#     try:                          # 可以手动用try做处理
#         return a / b
#     except ZeroDivisionError:     # 我们可以使用已知的异常名字来捕获特定的异常
#         return                    # 前提是我们已经拿到异常的类型名字
#                                   # 这样做就可以避免捕捉其他异常而混乱
#
#
# print(div(10, 0))


# 还有一种加else和finallly的用法，祥见wiki后台第7单元第九点\\


# # 用户自定义异常类型，只要该类继承了Exception类即可，至于类的主题内容用户自定义，可参考官方异常类
# class CustomException(Exception):
#     def __init__(self, value='值不能为0'):
#         self.value = value
#
#     def __str__(self):
#         return self.value
#
#
# a = 0                               # a==0时，触发异常；a==1时，不触发异常
# try:
#     if a == 0:
#         print('a = {}触发异常'.format(a))
#         raise CustomException
#     print('a = {}未触发异常'.format(a))
# except CustomException as e:
#     print(e)



# xintianjiade



# 123134546469879789786415113156156


# dsadasdasda
