chai_types = {"Masala":"Spicy", "Ginger":"Zesty","Green":"Mild"} 
# we can use "dict" key word also to create the dictionary  
# or we can use the curly braces 
print(chai_types)
print(chai_types["Masala"]) # we have to give the key to get the data 
#we can use get method and remove the squared brackets
print(chai_types.get("Ginger"))


# diff between get and the normal bracket syntax 
# print(chai_types.get("gingery")) 
# print(chai_types["Masalaa"]) # the error will be different  in both the cases 

print(chai_types)

#changing the value in the dictionary 
chai_types["Green"] = "Fresh" # the data of the key green will be changed to fresh \
print(chai_types)



for chai in chai_types:
        print(chai)  # only key will be printed ,not the value or the data


# to print the values - 
for chai in chai_types:
        print(chai, chai_types[chai]) # we know chai_types[key] => will give data 

 
#in case of Dictionary we can  iterate with two variable if 
for key , value in chai_types.items(): # using .items method we bring all the items here 
            print(key,value) # the results will be same 


if "Masala" in chai_types:
            print("I have masala chai")


# length of the dictionary 
print(len(chai_types)) # it will give the no. of items in the dictionary 
        


#adding another key and value inside the dicitonary 
chai_types["Earl Grey"] = "Cirtus"
print(chai_types)


#POP method - in dictionary we have to provide the key  to remove 
chai_types.pop("Ginger")
print(chai_types)

#Popitems - in this we dont have to add any parameter , it pop the last item 
chai_types.popitem()
print(chai_types)

#delete key word - it removes directly from the memory 
del chai_types ["Green"]
print(chai_types)

# We can have dicrionaries inside the dictionaries 
chai_types_copy = chai_types.copy()

# as we make list inside the list 
# similary we can make dictionaries inside a  dictionary
tea_shop ={
        "chai":{"Masala":"Spicy", "Ginger":"Zesty"},
        "Tea" :{"Green":"Mild","Black":"Strong"}
}
print (tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["Ginger"])


squared_num = {x:x**2 for x in range(6)}
print(squared_num)

squared_num.clear() # it clears the whole dictiionary 
print(squared_num)


#constructing  a dictinory using  list and a string 
keys = ["Masala","Ginger","Lemon"]
default_value = "Delicious"

#constructing the dictionary 
new_dict = dict.fromkeys(keys,default_value)
print(new_dict)
















