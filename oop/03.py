class Student():
    name = "dana"
    age = 18

    def say(self):
        self.name= "aaaa"
        self.age =200
        print("My name is {0}".format(self.name))
        print("My name is {0}".format(self.age))

kk = Student()
kk.say()