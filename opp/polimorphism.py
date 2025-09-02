class Animal:  #parenet class
    def sound(self): #absract method
        print("Animal makes a sound")


class Dog(Animal): #child class
    def sound(self): #implement the abstract method 
        print("Gheu gheu")

class Cat(Animal):
    def sound(self):
        print ("Mew mew")


animals=[Dog(),Cat()] #objects
for animal in animals:
    animal.sound() #function call


    #ekhane same method ba function vibinno class e vibinno bebohar kortece ,,,,,etae holo polymorphism.