score = input("Enter your marks")
score = float(score)
if 100>=score>=90:
    print("Exellent")
elif  80<=score<90:
    print("very good")
elif  65<=score<80:
    print('good')
elif  50<=score<65:
    print("average")
elif  36<=score<65:
    print("poor")
elif score<36:
    print("Fail")
else:
    print("please enter correct data")