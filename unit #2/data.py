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
   print("The factors of",'x',"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

# for i in range(1, x + 1) starts at 1 and finds the factor that would go along with 1 (+1) to end up with the product, and so on (for the rest of the factors)(no comma with x so that x is included in the list).
# if(x % i == 0) uses the value of i to even divide x evenly, and IF true (==0), then the factors will be printed out.

number = 45

print_factors(number)

#Challenge 4
def gcf(x, y):
   if(x > y):
       x,y = y,x
   for i in range(x,0,-1):
       if((x % i == 0) and (y % i == 0)):
           return i

# if x is greater than y, then y is also greater than x. This function makes both variables have something in common with one another, no matter how big or small they may be. This is done by saying that both x and y are great and are also small. 
# by claiming this, it allows the x to justify its position as it is being used in the function.
# for i in range(x,0,-1) starts at x and transitions to (0) find the gcf down in the list of factors (-1).
# if(x % i == 0) and (y % i == 0) uses the value of i that is found in both x and y and evenly divides out both of them.
# by return, we have also justified and proved how the statements (IFs) are true and found out the gcf.
       
print("The gcf is", gcf(45, 50))

gcf = 'i'
x = 45
y = 50


