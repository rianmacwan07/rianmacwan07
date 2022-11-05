number=int(input("enter the number"))
for i in range(1,11):
    print(str(number)+"x"+str(i)+"="+str(i*number))
l1=['harry','sohan','sachin','lata']
for name in l1:
    if name.startswith("s"):
       print("hello"+name)
num=int(input("enter the value" ))
count=1
while count<=10:
    num=num*1
    print(num,'x',count,"=",(count*num))
count+=1
num=int(input("enter the number:"))
prime=True
for i in range(2,num):
    if(num%i==0):
       prime=False
       break
    if prime:
       print("this number is prime")
    else:
        print("this number is not prime")
num=int(input("enter the number"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print("the factorial of given number is",+factorial)
#n=4
for i in range(4):
    print("*"*i)
n=3
for i in range(3):
    print("  *  ",i)
    print(" * ",i)
    print("*",i)