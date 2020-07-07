# 封装
class aaa():

    pub_res = '公有变量'
    __pri_res = '私有变量1'
    _pri_res = '私有变量2'

    def pub_function(self):
        print('公有方法')

    def _pri_funtion(self):
        print('私有方法1')

    def __pri_function(self):
        print('私有方法2')


print(aaa.pub_res)
print(aaa._pri_res)
print(aaa().pub_function())
print(aaa()._pri_funtion())


# 继承
class Parent():

    money = 10000000000
    house = 800
    __clothes = '衬衫'

    def skill(self):
        print('点石成金')


class Child(Parent):
    hobby = '花钱'
    pass


c = Child()
print(c.house)
print(c.hobby)
print(c.money)
print(c.skill())


