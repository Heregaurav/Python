number1 = input("write a number :")
number = int(number1)
even_number = 0
for num in range(1,number+1):
    if num%2 ==0:
        even_number +=1
print(even_number)
