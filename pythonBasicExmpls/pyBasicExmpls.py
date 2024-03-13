'''#Arithmetic Operations
print(1+1)
print(1*2)
print(20-20)
print(2**3)
print((2+10)*(10+3))

#Example with variables
my_income = 100
tax_rate = 0.1
my_taxes = my_income*tax_rate
print(my_taxes)

#strings Examples
myVar = "Hello" #using variables
print(myVar)

#methods
myVar = "hello"
print(myVar.upper())

#split method
myVar = "Hello mike how is your dog" #1
print(myVar.split())

myvar = "Hello mike, how is your dog"#2
print(myvar.split(","))

#forward index method
myVar = "Hello mike how is your dog"
print(myvar[0])

#reverse index method
myVar = "Hello mike how is your dog"
print(myvar[-1])

#start and end index
myVar = "Hello mike how is your dog"
print(myvar[0:5])

#f string
fName = "Sathish"
lName = "Leo"
print(f"Hello {fName} {lName}")'''

#python lists["item",0,10.2,"some",myVar]
#ex1:
myVar = 10
myList = [1,2,3,myVar]
print(myList)

#slicing:
myList = [1,2,3,4,5]
print(myList[0:3])

#append():
#adding the element at the end of the list
myVar = "New"
myList = [10,20,30,40,50]
myList.append(myVar)
print(myList)

#insert():we insert the item in particular index
myVar = "new"
myList = [100,200,300,400,500]
myList.insert(1,myVar)
print(myList)

#pop(): By using this we can remove last element from the list
myList = [100,200,300,400,500]
item_removed = myList.pop()
print(myList)
print(item_removed)

#reverse(): By using this to print the reverse in order
myList = [1,2,3,4,5]
myList.reverse()
print(myList)

#sort(): To sort the list which in diff order ex: ascending and discending order
#ascending order
myList = [4,5,7,8,2,3,1,2,3,1,4,9]
myList.sort()
print(myList)
#descending order
myList = [4,5,7,8,2,3,1,2,3,1,4,9]
myList.sort()
myList.reverse()
print(myList)