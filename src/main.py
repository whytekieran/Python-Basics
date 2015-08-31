import math #math class
import time #time class
import CustomModule #importing my own custom module
from CustomClassModule import Employee #Importing a custom module called CustomClassModule and in that module import the Employee class

emp = Employee("Kieran", 26)#Creating an object of class employee
emp.setAge(25)              #using some of the functions
emp.printDetails()          #output employees name and age

print("{0}".format(hasattr(emp, 'age')))    # Returns true if 'age' attribute exists
print("{0}".format(getattr(emp, 'age')))    # Returns value of 'age' attribute
setattr(emp, 'age', 8)                      #Set attribute 'age' at 8
emp.printDetails()
emp.setAge(25)                              #Set age attribute back to 25 with custom made function
emp.printDetails()
delattr(emp, 'age')                         #Delete attribute 'age' for this object

#Using function that is define in my custom module
print()
CustomModule.Welcome()

print()
print("Using strip() to remove newline character \n from end of the following string string")
line = "Hey everybody its......kieran here\n"
line = line.strip()
#line = line.strip("Hey") would remove the word "Hey" from start of string
#strip can be used to move any characters from start or end of a string
#The split() function will break a string. eg "Hi im Kieran" into a list like this ['Hi', 'im', 'Kieran'] Then we can reference an element
#in the list to get a particular value
print(line)

#Getting input and using variables
print("Accepting input and Outputting, formatted and Unformatted")

name = input("What is your name?")
age = input("What is your age?")

print("Name is " + name + " and age is " + age)            #unformatted output
print("Name is {0} and age is {1}".format(name, age))      #formatted output
print("Name is {1} and age is {0}".format(name, age))      #formatted output switched arguments
print("Name is {0:10} and age is {1}".format(name, age))   #formatted output with defined spacing "name" has minimum 10 spaces
print("Formatted number: {0:3.2f}".format(34.6756443))                          #Set to two decimal places
print(str(39))                                                                 #printing number as a string 
print(str(age))                                                                #printing number as a string 
print("Printing string variables first three letters: {0}".format(name[0:3]))   #Printing specific part of a string (prints 0, 1, 2)

#Updating a string
print()
print("Updating a portion of a string")
var1 = 'Hello World!'
print("String :- {0}", var1)                                                       
print("Updated String :- {0}", var1[:6] + 'Python') #From letter 7 in this string, add the word "Python" counts like 0,1,2,3,4,5 (6)
del var1

#Use triple qoutes for multiple line strings
var1 = """My name is kieran and im from ireland, im writing this to give an example of a multiple line string so im just going to continue 
waffling on until it reaches more than a line. Oh wait its more than a line now thats pretty cool. Maybe if i keep talking i can get it to
reach two lines. Mission Accomplished. :D"""
del var1

#example of using the 'in' and the 'not in' keywords
print()
if('i' in name):
    print("This name contains the letter i")
elif('i' not in name):
    print("This name does not contain the letter i")

del name    #used to delete variables and free memory
del age     #important to note that python comes with garbage collection and will remove unessasary objects

print()
print("Importing math and using math function") #math class function example
a = 10
a = 12              #changing the value of a number type (int, float, double etc) results in a newly created object
b = pow(a, 6)                                       #example of math class function
print("A to the power of B is: {0}".format(b))        #print answer
del a, b                                                #delete variable a and b
print()



#looping over something and printing
#remember Python is delimited by whitespace NOT semicolun ; like in java. spacing and tabs are important.
print("Printing out number formatted text")

for i in range(1, 11):
    print("{:2d} {:3d} {:4d}".format(i, i*i, i*i*i)) #doesn't use 11. uses 10 and stops max number will be 2, 3, and 4 numbers in size
    
print()
                                                     
#simple while loop with if/else   
i = 0
while(i < 10):
    print(i)
    
    if(i == 7):
        print("Wow lucky number 7!")
    elif(i == 9 and i != 7):            #example of using the "and" operator like && in java. Also can use "or" like || in java
        print("Last Number")
    else:
        print("Your nothing special")
    
    i += 1                              #increment counter like this (NOT ++i)

#simple total product cost product calculation
total = 0.00
while(True):
    answer = input("Want to enter product prices? Enter Y(yes) or N(No)")

    if(answer == 'Y'):
        product = input("Enter price: ")
        total += float(product) #important to convert str value entered from user into float value. also an int() to convert int
    elif(answer == 'N'):
        break
    else:
        print("Invalid input try again")
        
print("Total price of good entered is: ${0:5.2f}".format(total))
        
print()

#simple for loop
print("Looping over a simple list(array)")
people = ["Kieran", "Michael", "Colin"]

for person in people:
    print("{0} is in the people list".format(person))        
 
print()    

#adding to an array/list it can hold different values int string etc
print("Adding to and looping over a simple list(array)")
numberList = []
for i in range(10):
    if(i == 9):
        numberList.append("Larry")
    else:
        numberList.append(i)
        
for number in numberList:
    print("{0} is in the numberlist".format(number))
    

newList = ["Kieran", 26, 44.6, 'c']     #list can hold many different elements
totalList = numberList + newList        #can add list together 
print(totalList)                        #print out the two lists added together

j = 1
for element in totalList:               #you can loop over the list with different types (Python wont differentiate)
    print("Element {0} is: {1}".format(i, element))
    j += 1                              #You must increment/ decrement counters like this. ++ and -- wont work. You += -= *= /=


print()
print("Two dimensional lists(arrays)")    
twoDimList = [[1,2,3],[4,5,6],[7,8,9]]              #two dimensional list (each row is a list)

#looping over and printing each ROW
print("Printing each row") 
for row in twoDimList:
    print(row)                                      #printing each ROW
    
print()
    
print("Row 1: {0} ".format(twoDimList[0]))                    #printing 1st ROW
print("Row 2: {0}" .format(twoDimList[1]))                    #printing 2nd ROW
print("Row 3: {0}".format(twoDimList[2]))                     #printing 3rd ROW
print("Row 1 Column 1: {0} ".format(twoDimList[0][0]))        #printing 1st ROW and 1st COLUMN
print("Row 3 Column 2: {0} ".format(twoDimList[2][1]))            #printing 3rd ROW and 2nd COLUMN
twoDimList[2][1] = 250
print("Row 3 Column 2: {0} ".format(twoDimList[2][1]))

#Useful nested for loop to simply looping over 2D data  
print("Simple loop and print of 2D data")      
for row in twoDimList:    #simple loop through 2D array outer loop for each row (variable "row")
    for element in row:   #then loop over each row (using "row" variable and "element" variable for each element)
        print(element)    #printing each element

print()
        
#Nested for loop to loop through 2D array AND uses variable "index" to reference each elements index number in the array
#enumerate() needed here
print("Loop and print of 2D data also gets index to referance")
for row in twoDimList:                       #Outer for loops through row (each row represented by variable "row")
    for index, element in enumerate(row):    #Inner for loops through each "element" in row and "index" used as index for each element
        row[index] = math.pow(element, 2)    #each element in the matrix is equal to itself to the power of 2.
                                                
#looping over and printing each updated ROW
print()
print("Printing each updated row") 
for row in twoDimList:
    print(row)                                      #printing each ROW
    
print()                                             #line break

print("Creating and printing 2D array initialized to 0's (long way)")
#long way to create and print 2D array of zero's 10x10
dim = 10
row = [0] * dim                     # row now equals [0,0,0,0,0,0,0,0,0,0]
m = []

for _ in range(dim):                 #No variable used as a counter, simple loop 10 times. (dim = 10)
    m.append(list(row))              #loop 10 times and append list to each row gives us 10X10 list (append a list) list()
    
for row in m:
    print(row)                        #printing the 10x10 2D list (array)      
    

print()

print("Creating 2D array of zeros short way")
#shorthand way to initialize 2D list of zeros
Matrix1 = [[0 for x in range(10)] for x in range(10)]  

for row in Matrix1:
    print(row)
    
print()

print("Creating 2D array of strings short way")
#shorthand way to initialize 2D list of zeros
Matrix2 = [["Name" for x in range(10)] for x in range(10)]  

for row in Matrix2:
    print(row)                                                            

del Matrix1, Matrix2                                        #deleting these 2D lists

print()

#tuples
print("Tuples")
tup1 = ('physics', 'chemistry', 1997, 2000) #Similar to lists but use () not [] like lists. Also can't change or update the elements
tup2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tup3 = "a", "b", "c", "d"
tup4 = ()                                                     #empty tuple
tup5 = (50,);                                                 #tuple's with one element must still include a comma
print("3rd tuple element: {0}".format(tup3[2]))               #can be accessed and printed like regular list elements
print("2nd to the 4th{0} tuple elements".format(tup2[1:5]))   #can also access and print a range of the tuple
del tup3                                                      #deleting a tuple

print()

print("Simple looping over a tuple")                          #looping over a tuple  
for tupElement in tup2:
    print(tupElement)
    
#dictionaries
print()
dict1 = {"Name": 'Zara', "Age": 7, "Class": "First"}          #examples of dictionary declaration (key/value) similar to hashmap java
dict2 = {1: "Kieran", 2: "Peter", 3: "David"}
dict3 = {}                                                    #empty dictionary declaration

print("Dictionaries")
print("Printing dictionary key/values: {0} ".format(dict1))

dict2[4] = "Mary"               #examples of adding key/value to a dictionary. Key is inside square braces and value to the 
dict3["Name"] = "Aimee"         #right of it. Also the keys/values data type clearly don't have to remain the same (unlike a hashmap)
dict3[18] = "Daly"

print(dict3)
print(dict2)

value1 = dict2.get(1)                      #can use get() function will return corresponding value. 
value2 = dict2.get(879, "No Key Found")    #can also use get function like this, if key isnt found can set to return a default value     
                                          
print(value1)
print(value2)

print("Looping over a dictionary")
i = 1
for key in dict2: #for every key in the dictionary
    
    value = dict2.get(key, "none") #get the value and if there is no key match return "none"
    
    if(value != "none"):                            #a little validation and output
        print("Value {0} is {1}".format(i, value))
    else:
        print("none")
    
    i += 1                          #incrementing a counter

#To loop over a dictionary to retrieve both key and value in the for loop stage do the following
print()
for key, value in dict2.items():                            #items() used to retrieve both values
    print("Key is {0} and Value is {1}".format(key, value))


#Time and date class and functions
print()   
#Python handles time data as a TimeTuple containing 8 fields, similar to time structure in C programming 
localtime = time.localtime(time.time())
print("Local current time: {0}".format(localtime))  #There are many more time and date functions, use as needed

print()
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970: {0}".format(ticks))#Seconds(ticks) since epoch January 1st 1970 .time()
localtime = time.asctime( time.localtime(time.time()))  #prints the date/time in readable format
print("Local current time: {0}".format(localtime))      #there are many more time and date functions and a calender class and functions
                                                              
#Functions
#Simple function with an argument
def outputName(str):  # @ReservedAssignment
    print("The name you entered is {0}".format(str))
    return

strName = input("Enter your name: ")
outputName(strName)                     #calling the function

#Functions, passing by reference and value
#All parameters in Python are passed by reference but its possible to get pass by value effect
#Following example passes by reference
#value of mylist inside and outside function will be the same
print()
print("Function passing by reference")
def changeme1(mylist):
    mylist.append([1,2,3,4])                                                    #passed in parameter gets values appended to it
    print ("Values inside the function: {0}".format(mylist))
    return

mylist = [10,20,30]                                                             #creating a list
changeme1(mylist)                                                               #passing to function
print ("Values outside the function:{0}".format(mylist))

#The following is an example of how we can end up with a pass by value effect
print()
#Firstly a simple example of how when we declare a list and then declare it again, the original values are overriden
list10 = [1,2,3,4]
list10 = [6,77,1,23]
print(list10) #outputs the second value 6, 77, 1, 23

print("Function passing by value")
def changeme2(mylist):
    mylist = [1,2,3,4]; #Here we are creating a NEW variable reference that is local to this function. Parameter to function is ignored.
    print ("Values inside the function: {0}".format(mylist)) #outputting the local variable. 
    return

mylist = [10,20,30];
changeme2(mylist);
print ("Values outside the function: {0}".format(mylist)) #Output here will be different to value outputted from the function

#Simple function that uses the "return" key word to return a value
print()
print("Function that uses the return keyword to return a value")
def returnValue(variable):
    print("Value is {0}".format(variable))
    return variable
    
#Using the function
receivedValue = input("Enter some data: ")
returnedValue = returnValue(receivedValue)
print("Returned value is: {0}".format(returnedValue))

#Function with keyword arguments
print()
print("Function that uses keyword arguments")
def printinfo1( name, age ):
    print("Name: ".format(name))
    print("Age ".format(age))
    return

#Here we call the function using keyword arguments, use the parameter name and assign it a value. Using this way the ordering of
#the arguments doesnt need to match the ordering of the parameters in the function declaration.
printinfo1(age=50, name="miki")

#Function that uses default arguments
def printinfo2( name, age = 35 ):
    print("Name: {0}".format(name))
    print("Age {0}",format(age))
    return;

#Two examples of calling the function
printinfo2(age=50, name="miki")#the call first gives a value of 50
printinfo2(name="miki") #the second call only provides one argument, usually illegal but this time the defualt argument is used

#Function that uses variable length arguments, very useful if you think this function might have to take more arguments than 
#originally defined, here is an example.
#arg1 represents the parmeter the function will take, the *vartuple is a actually a tuple, only used if your trying to pass in more
#than the argument defined.
print()
print("Function that uses variable length arguments")
def printinfo( arg1, *vartuple ):
    print("Output is: ")
    print(arg1)                 #if arg1 is used as argument
    for var in vartuple:        #if more than one argument is passed in we use vartuple
        print(var)
    return

printinfo(10)              #using the arg1 argument (above) is used
printinfo(70, 60, 50)      #passing in more than one value so the vartuple parameter (above) takes over.

#CONTINUE ON WITH A LITTLE MORE CLASSES/OBJECTS THEN ONWARDS TO FILE I/O

print("Bye")





