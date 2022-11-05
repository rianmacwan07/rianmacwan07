#...................coordinate geometry........................
# distance formula
# general formula
    # X-intercept
    # Y-intercept
# slope of line formula
# two point formula
# slope point formula



class macordinate:
  def distance(self):
    print('************distance formula************ ')
    print('FORMULA')
    print('AB = sqrt((x2-x1)^2+(y2-y1)^2)')
    x2=int(input('enter value of x2='))
    x1=int(input("enter value of x1="))
    y2=int(input("enter value of y2="))
    y1=int(input("enter value of y1="))
    AB=((x2-x1)**2+(y2-y1)**2)**.5
    print(AB)
   
  def slope(self):
   print("************general formula*************")
   a=int(input("enter value of a"))
   b=int(input("enter value of b"))
   slope=-a/b
   print("slope of given number is %d",slope)
  
  def intercept(self,x,y):
   a=int(input("enter value of a"))
   b=int(input("enter value of b"))
   c=int(input("enter value of c"))
   z=a*x+b*y+c
   print(z)
   print("enter(1) to see x intercept")
   print("enter(2) to see y intercept")

   choice=int(input("enter the number (1) or (2)"))
   Xintercept=-c/a

   Yintercept=-c/b
   
   if(choice==1):
     print(Xintercept)
    
   elif(choice==2):
     print(Yintercept)
    
  def twopoints(self,x1,y1,x2,y2,x,y):
    print("enter value of A")
    A=(x1,y1)
    print(A)
    print("enter value of B")
    B=(x2,y2)
    print(B)
        
    point = y-y1/y2-y1 == x-x1/x2-x1
    print(point)

  def slopepoint(m1,x,Y,x1,y1,a):
    m1=("enter value of m1")
    print(m1)
    x1=int(input("enter value of x1"))
    print(x1)
    y1=int(input("enter value of y1"))
    print(y1)
    a=("enter value of a ")
    print(a)
    b=("enter value of b")
    print(b)    
    if(m1==a/b):
     (Y-y1)=m1(x-x1)

m = macordinate()

select=int(input("select your choice"))
if select==1:
  m.twopoints()

elif select==2:
  m.distance()

elif select==3:    
  m.slope()
elif select==4:
  m.intercept()