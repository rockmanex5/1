class Animal():
   def __init__(self):
       print("kk")
class Paxing(Animal):
    def __init__(self):
        print("kjfkdsjf")

class Dog(Paxing):

    # __init__就是构造函数
    # 每次实例化的时候，第一个被调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print("I am init in dog")
# 实例化的时候，括号内的参数需要跟构造函数参数匹配
# 因为找到了构造函数，则不在查找父类的构造函数
kk = Dog()

class Cat(Paxing):
    pass
# 此时应自动调用构造函数，因为Cat没有构造函数，则查找父类构造函数
c = Cat()