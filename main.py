#identation
if 5 > 2:
    print("Five is greater than two")

#variables
userage = 100
username= "Andrew"
print(userage)
print(username)

#typesofvariables
myVariableName= "Camel Case Andrew"
MyVariableName= "Pascal Case Andrew"
my_variable_name= "Snake Case Andrew"
print(myVariableName)
print(MyVariableName)
print(my_variable_name)

#printfunction
x = "My Name is Andrew, First of his Name, Ruler of Egypt, Leader of the universe"
print(x)

a = "John Snow"
b = "is"
c = "cool"
print (a,b,c)

#typefunction
digit = 5
print(digit)
print(type(digit))

digit2 = 1.5
print(digit2)
print(type(digit2))

digit3 = 2j
print(digit3)
print(type(digit3))
#randomlibrary
import random
print(random.randrange(1,100))

#CASTING
#integers
y = int (1)
z = int (1.5)
t = int ("1")
print(type(y))
print(type(z))
print(type(t))
#float
b = float(1)
c = float(2.0)
d= float("3")
e = float("4.0")
print(type(b))
print(type(c))
print(type(d))
print(type(e))
#string
f = str(1)
g = str(1.0)
print(type(f))
print(type(g))

#strings
string1 = "I am the strongest, the brightest, the most awesome teacher in the world"
print(string1)
print(type(string1))

#concatenation
string2 = " He is also a super hero - Spider Man"
string3 = string1+string2
print(string3)

#python booleans
digit4 = 10
digit5 = 50
if digit5 > digit4:
    print("Digit 5 is more than Digit 4")
else:
    print("Digit 4 is less than Digit 5")

#arithmetic operaters
h = 20
i = 30
#sum
j = h+i
print(j)
#subtraction
k = i-h
print(k)
#multiplication
l = h * i
print(l)
#division
m = i/h
print(m)
#modulus
n = i%h

#list
thislist = ["Apple","Banana","Cherry","Potato","Avocado"]
print(thislist)
#Accesslists
print(thislist[0])
#NegativeIndexing
print(thislist[-1])
#Rangeofindexes
print(thislist[1:4])

#whileloop
o = 1
while o < 6:
    print(o)
    o+=1

#breakstatement
p = 1
while p <6:
    print(p)
    if p==3:
       break
    p+=1

#elsestatement
q = 1
while q <6:
    print(q)
    q+=1
else:
    print("q is more than 1")

#forloop
cars = ("Toyota","Subaru","VolksWagon","Nissan","Mazda")
for x in cars:
    print(x)

#function
def myfunction():
    print("This is a function")
myfunction()

#input
name = input("What is your name:")
print("Your name is:"+name )



