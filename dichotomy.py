x1 = float(input("Enter the x1 : "))
x2 = float(input("Enter the x2 : "))
n = int(input("Enter the n : "))
eq = input("Enter the function : ")

def equation(x):
    return eval(eq.replace("x",str(x)))

x = (x1+x2)/2

if equation(x1)*equation(x2)<0:
    for i in range(n):
        if equation(x1)*equation(x)<0:
            x2 = x
            x = (x1+x2)/2
        else:
            x1 = x
            x = (x1+x2)/2
    print("The result is : ",str(x))
else:
    print("change the interval !")