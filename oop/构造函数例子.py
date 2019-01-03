class Person():
    # 对Person类进行实例化的时候
    # 姓名要确认
    # 年龄要确认
    # 地址要有
    def __init__(self):
        self.name = "jj"
        self.name = 18
        self.address = "home"

# 实例化一个人
p = Person()

# 构造函数的调用顺序 -1
# 如果子类没有写构造函数，则自动向上查找，直到找到位置
class A():
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")

class C(B):
    pass

# 此时，首先查找C的构造函数
# 如果没有，则向上按照MRO顺序查找父类的构造函数，直到找到位置

c = C()

