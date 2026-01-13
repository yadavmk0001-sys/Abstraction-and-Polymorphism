class animal:
    def sound(self):
        print("Animal makes a sound")
    
class dog(animal):
    def sound(self):
        print("Dog barks")

class cat(animal):
    def sound(self):
        print("Cat meow")
    
a = animal()
d = dog()
c = cat()

a.sound()
d.sound()
c.sound()