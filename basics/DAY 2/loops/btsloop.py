import time 
print("chai is here")
username = "hitesh"
test = ""
if not test: 
    print("chai")
print(username)

my_list = [1,2,3,4,5]

I = iter(my_list)  # it assignes a memory location to the list object 
print(I)
print(I.__next__())
print(I) # memory reference doesn't change  , it will still point to the start of the list , it is just __next()__ who does all the work 
print(I.__next__())
print(I)
print(I.__next__())
print(I)
print(I.__next__())

