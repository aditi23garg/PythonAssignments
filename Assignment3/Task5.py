
def factorial(num):
    fact = 1
    for i in range(2,num+1):
        fact = fact * i
    return fact

num = int(input("Enter a number: "))
result = factorial(num)
print("Factorial of",num,"is:",result)
