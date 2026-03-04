# x = 2 
# y = 3
# z = 4
# print(x+y)
# print(2**50) #  2 to the power 50 
# print((x+y)*z)
# print(40+2.23)
# print(int(2.453)) #typecasting the decimal value to int 
# print (float(5)) # again typecasting 
# # overloading of operators 
# print("chai"+"code") 
# #here the operator(+) decide how to concatinate 

# print( x, y, z) # as it is coming as paranthesis therefore it is a tuple not a list 

# print(x+1 , y*3) 

# print(z**5)

# print(2**10)

# result = 1/3.0  # important understand this one 
# print(result)

# print(repr('chai')) # understand what is repr function doing here 

# print(str('chai'))
# print('chai')
# print(5.0 == 5.0)
# print(4.0 != 5.0)
# print(x,y,z)
# print(x<y<z)
# # or 
# print (x<y and y<z)
# print (x>y and y<z)
# print (1==2<3) #or 
# print( 1==2 and 2<3)






#  # common library for numbers 

import math 

#floor
print(math.floor(3.5) ) # math.floor() gives the bottom value of that decimal number 
print(math.floor(-3.5))
print(math.floor(3.9))
print(math.floor(3.2))

#trunc
print(math.trunc(2.3))  # math.trunc gives the number closer to the origin(0) in the number line 
print(math.trunc(-2.3)) 

#complex numbers in python 
print(2+1j)
print((2+3j)*4) 

#octa decimal base number 
print(0o20)  # octals are always started by : "0o"
print(oct(64)) # print the octal value of 64 


#hexa decimal 
print(0xff) 
print(hex(64)) # print the hexal value of 64 


#binary values 
print(bin(94))



print(int(3.14))
#the most comman way to conver the number into different base number , be it hexal or octal or binay 
# we can do that  with the following techniques 
print ( int ('64',16))
print(int('64',8))
print(int('10000',2))


# bit wise operation 
# left shift 
x =1 
print(x<<2) #basically it is saying left shift by 2 bits  -- 100 => that is 4






# A random number generator 
import random 

#random.random , random.randint
print(random.random())  # gives a random interger between 0 and 1 
print(random.randint(1, 100)) # random integer between 1 and 100 ( not including 1 and 100 )

#random.choic
l1 = ['lemon','masala','ginger','mint']
print(random.choice(l1))  #randomly choses any value form the list l1 


random.shuffle(l1) # shuffles the l1 list 
print(l1)



print(0.1 + 0.1 + 0.4)
print(0.1 + 0.1 + 0.1)
print(0.1 + 0.1 + 0.1 - 0.3) # this prints some gibrish value basically python computes it incorrectly 


 # therefore we need this library for it's proper functioning 
from decimal import Decimal  #decimal contact manager
print(Decimal('0.1') + Decimal('0.1')+Decimal('0.1')) # this will answer it correctly 
print(Decimal('0.1') + Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))



#similar library for the fraction 
from fractions import Fraction
myfra = Fraction(2,7) # 1st arg is numerator and 2nd arg  is denominator
print(myfra)




# Sets 

setone = {1,2,3,4}
print(setone & {1,3})  # gives the intersection of setone and {1,3}
print(setone|{1,3,8,7}) # gives  union of the setone and {1,3,7,8}
print(setone - {1,3}) # removes those numbers which are intersecting 
print(setone-{1,2,3,4}) #give the empty set  --- set()




#boolean
print(type(True))
print(True is 1 ) #gives false  cause it is not actually a number , although we denote it like 1 
print(True + 4) # here we get the sum to be 5 


