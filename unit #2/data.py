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

# for i in range(1, x + 1) uses every one of the 45 numbers, with one being the starting number since it is part of the factor system, and ending at 46
# if(x % i == 0) uses the value of 1 to even divide itself with 45 to get the next factor

number = 45

print_factors(number)

#Challenge 4
    
x = 45
y = 50
common_factors = 1, 5
common_factor1 = 1
common_factor2 = 5

gcf = 5

#Assume we knew what the factors are for 50 by using the same funcion written above to find the factors of 45. Thus, ending up with common factors of 1 and 5.
#gcf always ends up being the last common factor that is the largest of them all.
#So in this case, common_factor2 seems to be the perfect fit for the gcf, for it is the last common factors that is the greatest of all.
#Now, to make this true, I use the function below to show how they are equal to one another and make the function print out 5 as the gcf. (If common_factor2 is equal to 5, so is going to be the gcf.)
#If the gcf is NOT equal to common_factor1, then the gcf will be whatever value that common_factor1 is.
#It is very likely for the function to print out the gcf as 5, for there is enough information to prove it.

if(gcf == 'common_factor2'):
    print('5 is the gcf')
elif(gcf == 'common_factor1'):
    print('1 is the gcf')


