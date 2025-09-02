from abc import ABC,abstractmethod   #imported ABC and abstractmethod from abc 

class Vehical(ABC): #abstract class
    @abstractmethod #abstract method
    def start (self): ##abstract method
        pass 

class car(Vehical): #Chils class
    def start(self):#implement the abstract method
        print("Car start") #

car=car() #object
car.start() #function call



##note(Vehicle → বলছে সব গাড়ির start ফাংশন থাকতে হবে, কিন্তু কিভাবে কাজ করবে সেটা বলছে না।আর চাইল্ড ক্লাস গুলোকে সেটা ইমপ্লিমেন্ট করতে হবে।এখন car ক্লাসে start মেথড ইমপ্লিমেন্ট করা হয়েছে।
# ekhon ki vabe gari sart hoilo seta amra jani na...call korlam r calo hoilo,,,,aita e abstraction)