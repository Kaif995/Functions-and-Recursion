def factorial_calc(n):
    fact=1
    for i in range(1, n+1):
        fact *=i
    print(fact)     
n=int(input("Enter a Number to find factorial: "))   
factorial_calc(n)

#We can also do this by Recursion Method!
def factorial_calc(n):
    if(n== 0 or n==1):
        return 1
    else:
        return n* factorial_calc(n-1)
n=int(input("Enter a Number to find factorial: "))   
print(factorial_calc(n))