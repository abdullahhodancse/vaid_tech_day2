class BankAccount:
    def __init__(self,name,balance): #initialize the variables in the constructor mathod
        self.name=name
        self._balance=balance    #privete variable


    def deposite(self,amount): #method for deposite money
        self._balance+=amount  

    def show(self): # meethod for show balance
        print(f"{self.name} Your balance is {self._balance}") 

account1=BankAccount("korim",5000) #object 
account1.deposite(300)
account1.show()
