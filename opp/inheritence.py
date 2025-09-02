class Animal: #parent class
    def sound(self): #methos
        print("Animal makes a sound")


class Dog(Animal): # child class parent class e inherite korce mane Animal er property se use korte parbe.
    def bark(self):
        print("Ghue hue")

dog=Dog()
dog.sound() #ai je animal er method sound() se use korte partece.Aita e holo inheritence
dog.bark()
      
    