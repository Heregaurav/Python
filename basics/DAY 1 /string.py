print("Gaurav kumar chandravanshi")
name ="Gaurav kumar chandravanshi"
print(name)
print(name[0]) # prints the first character 


slice_name = name[0:6] #taking the part fromm 0 to 5 
print(slice_name) #gives us gaurav 

num_list = "0123456789"
print(num_list[3:])
print(num_list[:7])
print(num_list[0:7:2]) # here 3rd parameter is the hop by what range ( skip 1 number )])]) take the every 2nd value 
print(num_list[0:7:3]) # hop  the 2 value  , and take every third value 


chai = "lemon chai"
print(chai.replace("lemon","ginger")) # original chai variable wont change cause it is immutable 


#converting a string into a list  -- split()
chai_type = "Lemon , Ginger , Masala , Mint"
print(chai_type.split()) # we didnot define the basis of spliting so it will do it randomly  , in this case " " {space} .
print(chai_type.split(", ")) # this is the basis of spliting, we have defined it to be the "," .


chai = "masala chai"
print(chai.find("chai"))
print(chai.find("Chai")) # if it is not found then it will return -1 

chai_count = "Masala chai chai chai"
print(chai_count.count("chai"))


chai_type = "masala"
quantity = 2
order = "I ordered {} cups of {} chai"  # if we have these kind of curly braces in python  we call them placeholders and we can put variable into that 
# to put the value inside those placeholders
print(order.format(quantity , chai_type))

#converting list to string 
chai_variety = ["lemon", "masala", "ginger "]
print(chai_variety)
print("".join(chai_variety))
print(" ".join(chai_variety))
print("_".join(chai_variety))

print(len(chai))

for letter in chai:
        print(letter)

#how to handle double quote 
chai_feedback= "he said , \"Masala chia is awsome\"" # here backslash is relly important 
print(chai_feedback)
 

 # raw string   to to unicode escaping 
chai_r = 'Masala\nChai'
print(chai_r) # both will be printed in the different line 
# but to print the raw string 
chai_r = r"Masala\nchai"
print(chai_r)

chai = "masala chai"
print("masala" in chai )  # checks if chai has the word "masala " in it 

print ( "masalaaa" in chai ) #  gives false 






