class student:
    def __init__(self,name,age,department): ##initialize the variables in the constructor mathod.
        self.name=name   ##name variable of object
        self.age=age  ##age variable of object
        self.department=department ##department variable of object

    def introduction(self):  ## method itr will be prrint the introductions
        print(f"My name is {self.name}.I am {self.age} years old  and I am from {self.department} department")

student1=student("Hodan",20,"CSE") ##object1
student2=student("sohan",22,"EEE") ##object2

student1.introduction() #function call
student2.introduction()
