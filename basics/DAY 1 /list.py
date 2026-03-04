tea_varities = ["black","green","Oolong","white"]
print(tea_varities[-1])
print(tea_varities[3])  # both gives the output as white 
print(tea_varities[1:3])
print(tea_varities[1:4:2]) 
tea_varities[3]= "Herbal"
print(tea_varities)
print(tea_varities[1:2])#here we get the output as green  
#now we are changing the green value to the lemon , but we should remember that value is sliced 

# therfore the result would be also sliced
# tea_varities[1:2] = "Lemon" # here the string is being treated as an array and hence we get the  whole thing there as the output 
print(tea_varities)
tea_varities[1:2]=["Lemon"]  # now we are passing it as a block or a single item 
print(tea_varities)

print(tea_varities[1:3])

print(tea_varities[1:1] ) # this gives an empty list 
# therefore we can use this 

tea_varities[1:1] = ["green","ginger"] # other will be shifted by 2 respectively 
print(tea_varities)

# by this logic we can do the reverse operation too 

tea_varities[1:3]=[] # therefore we have changed the list from 1st index to 2nd index with empty list 

print(tea_varities) # we get back the everything same 

for tea in tea_varities:
        print(tea , end="_") # by default it changes the line during every iteration

#conditional statement  
if"ginger" in tea_varities:
            print("\nI have Oolong tea")
else :
            print("\nnot there ")

# appen() method
tea_varities.append("ginger")
print(tea_varities)
if"ginger" in tea_varities:
            print("\nI have ginger  tea")
else :
            print("\nnot there ")


#pop() method  removes the last value directly 
tea_varities.pop()
print(tea_varities)


# insert method 
tea_varities.insert(1, "green") # 1st arg is for position where we want to put  and  2nd arg is for what we want to insert 

tea_varities_copy = tea_varities #this will make both variable having the same object , as we know it is mutable 
# but if we want to  make copy such that the reference is different  then we have to do this
tea_varities_copy2 = tea_varities.copy() # therefore both will be having different reference 

print(tea_varities)
print(tea_varities_copy)
print(tea_varities_copy2)

tea_varities.append("lemon")
print(tea_varities) # this will be chahnged 
print(tea_varities_copy) # this will be changed  cause both has same reference
print(tea_varities_copy2) # this won't be changed cause the refence is different 



print(range(10))
y = range(0,10)
#list comprehension
squared_nums = [x**2 for x in range(10)]
print(squared_nums)  #therefore we can get the whole squared list (array) this simple in python 
cube_num = [y**3 for y in range(10)]
print(cube_num)