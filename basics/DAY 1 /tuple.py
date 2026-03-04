# difference between list and tuple 
# major difference - tuple is immutable whereas  list is mutable 

#list 
fruits = ["apple", "banana", "mango"]

#tuple
fruits = ("apple", "banana", "mango")

# performace 
# Tuple is slightly faster than list.

# Tuple uses less memory.

# Because tuples are immutable, Python optimizes them.




# USE CASE DIFFERENCE 
# | Use List When…               | Use Tuple When…             |
# | ---------------------------- | --------------------------- |
# | Data may change              | Data should not change      |
# | You need to add/remove items | Fixed data                  |
# | Example: shopping cart       | Example: coordinates (x, y) |
 

tea_types = ("Black","Green","Oolong")
print(tea_types)
 
print(tea_types[0])

print(tea_types[-1]) # same as it was in the list 
# slicing stays the same 
print(tea_types[1:3])
# we cannot change the values using indexing the tuple , as it is immutable 
# print(tea_types[0] = "ginger ")# can't cahnge  , and will throw error

print(len(tea_types))
more_tea = ("herbal", "herbal", "lemon")

print(more_tea.count("herbal"))# this will give the count of the "herbal" word 

# assigning the varaible 
print(tea_types)
((Black, Green, Oolong)) = tea_types # every variable is attached to the particular value in the tuple - the no. of variable and  list size
print(Black)

print(type(tea_types))



