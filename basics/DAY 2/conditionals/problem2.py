# day = input("what is the day today : ")
# age1 = input("what is the age of the person : " )
# age = int(age1)
# if age <18 :
     
#     if day != "wednesday" or "Wednesday":
#         print("the price is $8 only ")
#     else :
#         print("the price is $6 only ")
# else : 
#     if day != "wednesday" or "Wednesday":
#         print("the price is $12 only ")
#     else :
#         print("the price is $10 only ")


age = 4
day = "wednesday"
#learning in solution 2

price = 12 if age >= 18 else 8 
if day == "wednesday":
    price = price-2     # or price-=2


print("ticket price for you is $ :" , price)