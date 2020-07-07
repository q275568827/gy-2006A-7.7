# # 数据转换
# str1 = '123'
# int1 = 456
# print(int(str1) + int1)
# print(str1 + str(int1))

# 打开模式：r 读取  w 清空写入   a 追加写入  b 二进制模式

# file1 = open('kds.txt', 'w')
# file1.write('hello world\n你好')   # 输出  多行可以用\n换行
# file1.writelines(['啊大大叔\n', '发刚发的刚发\n', '请问去他\n'])
# print(file1.writable())         # 判断文件是否可写入
# file1.close()        # 关闭文件


# 读取

# file2 = open('kds.txt','r')

# print(file2.read())         # 默认读取全部数据
# print(file2.read(10))       # 读取指定大小的数据
# print(file2.readline())     # 按行读取，读取一行
# print(file2.readlines())    # 按行读取，读取所有行
# file2.close()


# 字符串取指定下标的值    包含左边界，不包含右边界
# a = 'abcdefghijklmnopq'
# print(a[0])                 # 取第一位
# print(a[-1])                # 取最后一位
# print(a[1:-2])              # 取第二位-倒数第二位(不包含倒数第二位)
# print(a[1:-2:2])            # 取第二-倒数第二位，步长为2(不包含倒数第二位)
# print(a[-1:0:-1])           # 从最后一位到第一位（不包含第一位）
# print(a[::-1])              # 从最后一位到第一位
# print(a[2:])                # 从第二位到最后
# print(a[:-2])               # 从头到倒数第二位(不包含倒数第二位)


# li = 'jkfdhd,hfjidjhd,hsjiqew,rfqqef'
# print(li.split(','))               # 以关键字','拆分
# with open('kds.txt', 'r') as f:  # with 使用一个上下文管理器
#     lines = f.readlines()
#     print(lines)
#     for i in lines:
#         print(i.replace('\n', ''), end='')   # print 默认带一个换行  (replace替换)

# 99乘法表  格式化输出1    python3以上可用
# for i in range(1,10):
#     for k in range(1, i+1):
#         print(f'{k}X{i}={i*k}', end='\t')
#     print('')


# 格式化输出2    占位符
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('%d X %d = %d' % (j, i, i*j), end='\t')
#     print('')
#

# 格式化输出3    .format
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{} X {} = {}'.format(j, i, j*i), end='\t')
#     print('')


# 找出某字符串中的某个字段，显示的是下标
# s = 'dsadasjkodhjasohfi.ohasofoasf'
# print(s.find('.oh'))


# 更改列表里的某些值
# l1 = [1, 2, 4, 54, 5, 7, 8, 7, 7]
# l1[0] = 3                       # 更改单个值，按下标搜索
# print(l1)
# l1[1:6] = 3, 4, 5, 6, 8      # 更改多个值，按下标（第2到第6位）不包含右边界
# print(l1)


# 往列表里新增数据
# l1 = [1, 2]                      # 一个空列表
# l1.append('王大锤')               # 新增一个数据，加在最后面
# print(l1)
# l1.extend((1, 888,'你好'))       # 新增多个数据，加在最后面
# print(l1)
# l1.insert(1, '王大锤')             # 在指定位置插入数据，前者是下标
# print(l1)

# 从列表中删除数据
# l = [True,1, 2, 3, 4, 5, 6]
# print(l.pop())                      # 默认挤出最后一位
# print(l)
# print(l.pop(1))                     # 删除下标为1的那个数据
# print(l)


# l = [True,1, 2, 3, 4, 5, 6]
# l.remove(3)                         # 从列表中删除指定的数据，此处删除3
# print(l)
# l.remove(1)                         # python中True为1，False为0
# print(l)


# 默认排序参数
# a = [5,45,12,5,7,5,6,8,9,9,1,0,14,5,456,456,4131,13]
# a.sort()                        # 默认升序排序
# print(a)
# a.sort(reverse=True)            # 降序排序
# print(a)


# 字典相关操作
d = {'name': '小米', 'age': '18', 'sex': '男'}

# for key in d:                       # 遍历字典，只能取出key
#     print(d[key])
#
# for k, v in d.items():              # 遍历字典，可以取出key和value
#     print(k, v)
#


# d['addr'] = '上海闵行'                  # 以key修改字典中的字段，没有则新增
# print(d)
# d['addr'] = '上海浦东'                  # 以key修改字典中的字段，已有则修改
# print(d)

# d.update({'addr': '上海闵行', '学历': '本科'})   # 新增或修改字典中多个字段,没有则新增
#                                                 # ,已有则修改
# print(d)

# 添加一行新代码


a = 1
print(a)
