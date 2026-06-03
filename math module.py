#----Math----  calls, square root , ceil, floor, pi, triangles(sin,cos,..), power, factorial, exponential



#------calls(cals)---------
import math
def cals():
    print("hello");  #calls the value  (hello)
cals()


import math
def cals(a,b):
    print(a+b);     # a+b=5
cals(3,2)           #calls the values(3,2)


#------square root (sqrt)------------
import math
print(math.sqrt(49))   #square root of (7) is 49
print(math.sqrt(36))   #square root of (6) is 36


#------ceil---> up to the nearest integer
import math
print(math.ceil(4.4))    # 4.4 up to the nearest value is 5
print(math.ceil(3.2))    # 3.2 up to the nearest value is 4


#-----floor---> down to the nearest integer
import math
print(math.floor(4.4))  # 4.4 down to the nearest value is 4
print(math.floor(3.2))  # 3.2 down to the nearest value is 3


#-----pi------>
import math
print(math.pi)          # pi = 3.14
#for example - Area of circle
import math
radius=5
area= math.pi*radius*radius
print(area)                  # area = 78.539


#----Triangles-------
import math
print(math.sin(0))      # sin(0)=0
print(math.cos(0))      # cos(0)=1


#----power----
import math
print(math.pow(3, 2))    # 3 power 2 is (9) like 3*3=9
#or
print(3**2)              # (9)


#----factorial----
import math
print(math.factorial(3))  # 3!=3*2*1 = (6)



#----Exponential-----
import math
print(math.exp(1))       # e^1 = 2.7182
print(math.exp(2))       # e^2 = 7.3890
