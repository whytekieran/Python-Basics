#Creating a simple class
class Employee:
    name = ""
    age = 0
    
    #The __init__() function is a special function, it acts as the constructor for the class
    #We dont need to specify the __init__ function. If we dont a defualt contructor will be generated automatically Employee()
    #Otherwise if specified we must use it. 
    def __init__(self, name, age):
        self.name = name    #the "self" keyword is like the "this" keyword in java, also included as a parameter in python
        self.age = age
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def setName(self, name):
        self.name = name
        
    def setAge(self, age):
        self.age = age
        
    def printDetails(self):
        print("Employee Details")
        print("Name: {0} Age: {1}".format(self.name, self.age))
        
        
        
        
        
        
    