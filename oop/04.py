class Teacher():
    name = "kk"
    age = 18

    def say(self):
        self.name = "yaona"
        self.age = 17
        print("My name is {0}".format(self.name))
        print("My name is {0}".format(self.age))
    def saykk():
        print(__class__.name)
        print(__class__.age)
        print("Hello, nice to meet you")


t = Teacher()
t.say()
# 调用绑定类函数使用类名
Teacher.saykk()