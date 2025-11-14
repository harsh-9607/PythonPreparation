class pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("I dont know what to say")

class dog(pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color
    def speak(self):
        print("WOOF WOOF")

class cat(pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color= color
    def speak(self):
        print("meow")
class fish(pet):
    pass

p= pet("Tim",19)
p.show()

c = cat("Bill",6)
d = dog("buddy",13)
f = fish("Bubbles",10)
c.show()

d.show()
f.speak()