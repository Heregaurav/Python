#compute the factorial of a number using a while loop

input_num = input("write a number :")
input = int(input_num)
factorial = 1

for i in  range(1 , input) :
    factorial = factorial*i
print(factorial)

factorial1 = 1
while  input>0:
    factorial1= factorial*input
    input -=1

print("factorial: ",factorial1)
