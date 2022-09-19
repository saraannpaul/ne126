#W2D1--intro demo

#this is a comment in Python; anything after a # is considered comment or documentation

#comments are used to:
#  *explain code to others (or self!)

#documentation is NOT python code: it is not read or processed by the machine! you can write whatever/however you like

print("hello world") 
#OUTPUT--> "put out of the program" this is what is displayed to the console (to the user) 

#print() is the output statement in Python
#"hello world" is a literal string/message to the user

#*everything* inbetween the " " will be displayed literally
print("hello           world")
print() #this displays a blank line 
print()
print()
print()
print()
print()

#assignent occurs from right to left
classSize=15

#display stored value
print(classSize)

#display stored value with message
print("The class size of SE116 is:", classSize)
print(classSize, "is the class size of SE116")

#process/manipulate stored value 
doubleClass= classSize * 2

#display new value
print("the class doubled is:", doubleClass)

#revalue classSize
classSize= classSize + 3 
print(classSize, "is the NEW class size of SE116")

