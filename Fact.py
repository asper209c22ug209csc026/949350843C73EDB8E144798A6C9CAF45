print("PROGRM TO FIND FACTORIAL OF A GIVEN NUMBER")
print("******************************************")
def factorial(n):  
    # single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
num=int(input("Enter a number :"))
print("Factorial of",num,"is",factorial(num))
