'''
定义一个类Human(人类),定义函数input_human录入信息,main调用显示信息
有三个属性: 姓名name,年龄age,家庭住址address (可以省略没有)
有方法: show_info 用来显示人的信息,update_age用来让这个人的年龄增加一岁
'''
class Human:
    total_count = 0
    def __init__(self, name, age, address = None):
        self.name = name
        self.age = age
        self.address = address
        self.__class__.total_count += 1

    def show_info(self):
        print("姓名:%s，年龄%s，住址%s"%(self.name, self.age, self.address))

    def update_age(self):
        self.age += 1

    @classmethod
    def get_human_count(cls):
        return cls.total_count

    def __del__(self):
        self.__class__.total_count -= 1


def input_human():
    L = []
    while True:
        name = input('输入姓名:')
        if not name:
            break
        age = int(input('请输入年龄:'))
        address = input('请输入地址:')
        s = Human(name, age, address)
        L.append(s)
    return L


def main():
    L = input_human()
    for obj in L:
        obj.show_info()
    for obj in L:
        obj.update_age()
    for obj in L:
        obj.show_info()
    print('当前的人数是%s'%Human.get_human_count())

if "__main__" == __name__:
    main()