username  = "chaiaurcode"

def func():
    # username = "chai"
    print(username)

print(username)
func() # as the function didn't get the username so it printed the global username variable 
# # this is legb rule 
# | Letter | Full Form | Meaning                 |
# | ------ | --------- | ----------------------- |
# | L      | Local     | Inside current function |
# | E      | Enclosing | Inside outer function   |
# | G      | Global    | Outside all functions   |
# | B      | Built-in  | Python’s default names  |

x = 99  # global  variable
# def func2(y):
#     z = x+y
#     return z

# result = func2(1)
# print(result)


# def func3():
#     # global x 
#     # x=12  this should not be done , this is a bad coding practice

# # func3()
# print(x)

def f1():
    x = 88
    def f2():
        print(x)
    return f2

myResult = f1()
myResult()

def chaicoder(num):
    def actual(x):
        return x**num
    return actual


# this is known a closures
f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))


