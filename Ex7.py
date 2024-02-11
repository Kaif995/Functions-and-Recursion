def Sumofnationalnum_cal(n):
    if(n== 0 ):
        return 0
    else:
        return Sumofnationalnum_cal(n-1)+n
n=int(input("Number of Digits you want to find Sum of Natural Number : "))   
print(Sumofnationalnum_cal(n))