class A:
    def work(self):
        print('A.work()被调用')


class B(A):
    def work(self):
        print('B.work()被调用')

    def super_work(self):
        self.work() #B.work()
        super().work() #A.work()
        super(B,self).work()#A.work()
        super(__class__,self).work()#A.work()

b = B()
#在覆盖情况下调用父类
b.__class__.__base__.work(b)
super(B,b).work()
#b.super_work()