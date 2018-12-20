class Person():
    name = "kk"
    __age = 18

p = Person()
# name是公有变量
print(p.name)
# __age是私有变量
p._Person__age = 19
print(p._Person__age)