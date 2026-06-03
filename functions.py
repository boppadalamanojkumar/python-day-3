##print(), input(), type(), int(), float(), str(), bool(), len(), range(), list(), tuple(), set(), dict(), max(), min(), sum(), abs(), round(), sorted(), enumerate()

marks=[10,20,30,40]
print("length:",len(marks))                #length:4
print("sum:",sum(marks))                   #sum:100
average=sum(marks)/len(marks)              
print("average:",average)                  #average:25.0
print("highest:",max(marks))               #highest:40
print("lowest:",min(marks))                #lowest:10
marks_str=str(marks)
print("Marks as a string:",marks_str)      #string:[10,20,30,40]
for mark in marks:
    print(mark,"-",type(marks))            #10,20,30,40 -list





#-------EXPLANATION--------------
#Function	Purpose
#print()	Display output
#input()	Get user input
#type()	        Check data type
#int()	        Convert to integer
#float()	Convert to float
#str()	        Convert to string
#len()	        Get length
#list()	        Create/convert to list
#tuple()	Create/convert to tuple
#set()	        Create/convert to set
#dict() 	Create/convert to dictionary
#range()	Generate sequence of numbers
#max()  	Largest value
#min()  	Smallest value
#sum()  	Sum of values
#sorted()	Sort data
#abs()  	Absolute value
#round()	Round numbers
#enumerate()	Get index and value
#zip()  	Combine iterables
