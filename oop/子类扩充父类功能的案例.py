class Person():
    name = "no"
    age = 18
    __score = 0 # 考试成绩是秘密，只有自己知道
    _petname = "sec" # 小名，是保护的，子类可以用，但不能公用
    def sleep(self):
        print("Sleep... ...")
    def work(self):
        print("make some money")

# 父类写在括号内
class Teacher(Person):
    teacher_id = "9527"
    name = "jojo"
    def make_test(self):
        print("attention")

    def work(self):
        # 扩充父类的功能只需要调用父类相应的函数
        #Person.work(self)
        #self.make_test()
        # 扩充父类的另一种方法
        # super代表得到父类
        super().work()
        self.make_test()

t = Teacher()
t.work()