marks1 = input("write the obtained marks :")
marks = int(marks1)

if marks >=101 :
    print("the marks obtained is not valid ")
    exit()

if marks < 60 :
    print("you got F grade ")
elif marks <=69:
    print("you got D grade ")
elif marks <=79:
    print("you got C grade ")
elif marks <=89:
    print("you got B grade ")
else :
    print( "you got A grade")

