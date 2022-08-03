********counting************

x = [24,25,26,64,12,75,624,254]
count = 0

for i in x:# if we pass as "for in range (x)'The answer is that you are passing your list as the input argument to range, which expects an integer. Don't do that. Say for i in myList instead.
    if i%4==0:
        count = count+1
print('list contains',count,'numbers that are divisibel by 4')

###############################################################################
************Concept of counting******************************

from random import *

#enter 10 numbers that are divisible by 18
count = 0
error = 0
for i in range(10):
    x=int(input('please enter a number that are divisible by 18: '))
    if x%18==0:
        print('the entered number is dividble by 18')
        count = count+1
    else:
        print('the value is not divisible by 18')
        error= error+1
print('total correct: ', count)
print('total incorrect :',error)


#summing and storing in outer loop variables

s = 0
for i in range(1,101):
    s= s+i
    print(s,end="/")

s = 0
for i in range(10):
    x = int(input("please enter a number :"))
    s = s+x

print("sum of all the value is :",s)

#Flag Variables

# so how this works is when the given statement true it takes flag =1 and  in next statement flag ==1 is " is not a prime number",so fi the given statement is  not true the value of flag which we predermined  as zero is not equal to 1 hence  it moves to next statement, if we didnt mention the value of flag to zero if it is a prime number it will not execute and gives as error = 'flag' is not defined. Did you mean: 'float'?


x = int(input("please enter a number"))

for i in range(2,x):
    if x%i==0:
        flag = 1  # so how this works is when the given statement true it takes flag =1 and  in next statement flag ==1 is " is not a prime number",so fi the given statement is  not true the value of flag which we predermined  as zero is not equal to 1 hence  it moves to next statement, if we didnt mention the value of flag to zero if it is a prime number it will not execute and gives as error = 'flag' is not defined. Did you mean: 'float'
if flag == 1:
    print('it is not a prime number')
else:
   print ('it is a prime number')
