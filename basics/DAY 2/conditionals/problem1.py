# userscore = input("give me a score value: ")
# print(userscore) # we always have to check whether the input value is input or not 


age1 = input("write your age here : ")
age = int(age1)

if age < 13 :
    print("you are a child")
elif age>=13 and age<=19 :
    print("you are a teenager")
elif age>19  and age <=59 :
    print("you are and adult")
elif age>=60:
    print("you are a senior citizen")

