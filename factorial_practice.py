'''def max(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3
m=max(4,5,6)
print(m)'''

'''def far(cel):
    return(cel*(9/5)) + 32
c=0
f=far(c)
print(f)'''
#recurin
'''n=int(input("enter a number"))
def sum(n):
    if n==1:
     return 1
    else:
        return n+sum(n-1)
print(sum(n))'''
'''n=6
for i in range(3):
    print("*" *(n-i))'''

'''def mul(n):
    for i in range(1,11):
     print(n,'x',i,'=',n*i)
n=(5)
mul(n)''' 
x=4   
for i in range(1,11):
    
    print(str(x)+"x"+str(i)+"="+str(x*i))

