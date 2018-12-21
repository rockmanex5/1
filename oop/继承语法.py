# 在python中，任何类都有一个共同的父类叫object
class Person():
    name = "NoName"
    age = 18
    __score = 0 # 考试成绩是秘密，只有自己知道
    _petname = "sec"  #小名，是保护的，子类可以用，但不能公用
    def sleep(self):
        print("Sleeping... ...")


# 父类写在括号内
class Teacher(Person):
    teacher_id = "9527"
    name = "ff"
    def make_test(self):
       print("attention")

class KK(Person):
    age = 0
    ace = 46

t = Teacher()
print(t.name)
print(t._petname)
t.sleep()
print(t.teacher_id)
t.make_test()

print("*" *20)

k = KK()
print(k.ace)
print(KK.name)
print(k.age)
