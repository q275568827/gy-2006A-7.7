# 冒泡排序
list1 = [0, 1, 5, 8, 45, 456, 423, 13, 47, 78, 7, 13, 14, 6123, 1, 0, 1, 4, 46, 461]
le = len(list1)
print(le)
for i in range(le-1, 0, -1):
    for n in range(0, i):
        if list1[n] > list1[n+1]:
            list1[n], list1[n+1] = list1[n+1], list1[n]
print(list1)



a = [1,2,3,4,5,67,8,9]
print(a[0],a[7])

# 99乘法表
# for i in range(1, 10):
#     for l in range(1, i+1):
#         print(f'{i}X{l}={i*l}', end='\t')
#     print('')
#

