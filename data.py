#Data Types 
#Numbers 1, 2, 3
def add():
    print(1+2)
    add (1,2)

#string "a,b,c"
name = "Mark"
def greeting(person):
    print(person)
greeting(name)
#1 and "1" are not the same thing
#add("1","2")
#undefined/null

#booleans

tenure = True
def is_tenured(status):
    if(status == True):
        print ("They have tenure")
    else: 
        print("they are not tenured")
        
is_tenured(tenure)

#Challenge 1
number = input("Enter a number: ")
if (number == '3'):
    print('odd')
else:
    print('even')

#Challenge 2
bill = 100
if bill > 25:
    print ('great')
elif bill == 20:
    print('okay')
elif bill == 15: 
    print('bad')
    
#Challenge 3
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if(x % i == 0):
           print(i)

number = 45

print_factors(number)

#Challenge 4
def gcf(x, y):
    if(y == 0):
        return abs(x)
    else:
        return gcf(y, x % y)
 
x = 45
y = 50
 

print(gcf(45, 50))