# Write a class called Dog that has two properties: name and age. Write a constructor that takes three arguments self, name and age and set these to the object properties.
# Now write a function sayHI(dog) where dog is the dog class object that returns a Hi, my name is <dog’s name> and I am <age> years old!

# sayHi(d1) # Hi, my name is Dot and I am 4 years old!
# sayHi(d2) # Hi, my name is Elf and I am 3 years old!

class SayHi(object):
    def __init__(self,name,age):
        self.age=age
        self.name=name

    def sentence(self):
        print(" Hi, my name is "+ self.name + " and I am " + str(self.age) +" years old!")

data1=SayHi("Dot",4)
data2=SayHi("Elf",3)
data1.sentence()
data1.sentence()
