animals = ["Zebra", "Camel", "Ape"]
animal = [animals[0]]
#start count at 0, reference each element with []
#print (animals[0])
#for animals in animals:
#   print(animal)

#for animal in animals:
#   if (animal == "Camel"):
#       print("We're in the desert")

#Strings operate like lists 
x = "Hello Freshmen"
#print(x[0])
#y = x.upper()
#print(y)
words_list = x.split(",")
print(len(words_list))

for animal in animals:
    if (animal == "Zebra"):
       print("Hello Safarians")
       
       
x = "Hello Safarians"
y = x.upper()

#y makes the words capiltalized.

for animals in animals:
    print(x[0])
    print(y)


x = "Hello Safarians"
words_list = x.split()
print(len(words_list))

for animals in animals:
    print(words_list)
    print(len(words_list))
    print(len(x))
    
# print(words_list) separate the words
# print(len(words_list)) counts how many words are within that sentence
# print(len(x)) counts how many letters are within that sentence
