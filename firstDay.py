#first program
'''
m=int(input("Enter a number"))
n=int(input("Enter second number"))
sum=m+n
print(sum)
differ=m-n
print(differ)
multiply=m*n
print(multiply)
division=m/n
print(division)'''

#second program
'''
floor=m%n
power=m**n
print(floor)
print(power)
'''
#third program
'''
pen_price=15
notebook_price=40
total_cost=(3*pen_price)+(2*notebook_price)
print(total_cost)
'''
#fourth program
'''
sum=0
for i in range(0,5):
    num=int(input("Enter he number"))
    sum=sum+num
avg=sum/5
print("Avg",avg)
'''
#fifth program
'''
import math
a=int(input("Enter a number"))
square=a*a
print("Square:",square)
b=int(input("Enter the number"))
print("Square Root",math.sqrt(b))
'''
#sixth program
'''
num1=int(input("Enter a number"))
num2=int(input("Enter second number"))
if(num1==num2):
    print("The gven numbers are equal")
else:
    print("Not equal")
'''
#seventh program
'''
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
if(num1>num2):
    print("The first number is greater")
else:
    print("The second number is greater")
'''
#eigth program
'''
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))
if(num1<num2):
    if(num1<num3):
        print(num1,"is smallest")
elif(num2<num3):
    print(num2,"is smallest")
else:
    print(num3,"is smallest")
'''
#ninth program
'''
marks=int(input("Enter your marks"))
if(marks>=40):
    print("Pass")
else:
    print("Fail")
'''
#tenth program
'''
age=int(input("Enter your age"))
if(age>=18):
    print("Eligible to vote")
else:
    print("Not Eligible")
'''
#eleventh program
'''
num=int(input("Enter the number"))
if(num%2==0):
    print("The given number is even")
else:
    print("The given number is odd")
'''
#twelth program
'''
maths=int(input("Enter your maths marks"))
science=int(input("Enter your science marks"))
if(maths>40 or maths==40 and science>40 or science==40):
    print("Pass")
else:
    print("Fail")
'''
#thirteenth program
'''
num=int(input("Enter the number"))
if((num%3)!=0):
    print("The number is not divisible by 3")
else:
    print("The number is divisible by 3")
'''
#fourteenth program
'''
amt=int(input("Enter the purchase amount"))
card=input("Verify if you have membership card(yes or no)")
if((amt>1000)or (card.lower)=="yes"):
    print("You are eligible for discount")
else:
    print("You are not eligible for discount")
    '''
#fifteenth program
'''
age=int(input("Enter your age"))
if(age>=13 and age<=19):
    print("Teenager")
else:
    print("Not a Teenager")
    '''
#sixteenth program
'''
age=int(input("Enter your age"))
if(age>=18):
    print("You are eligible to vote")
else:
    print("Not eligible to vote")
if(age>=18 and age <=70):
    print("Eligible to drive")
else:
    print("Not eligible to drive")
'''
'''
def switch_example(day):
    return {
    1:"Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Thursday",
    5:"Friday",
    6:"Saturday",
    7:"Sunday"
    }.get(day,"Invalid day")
print(switch_example(7))
'''
#seventeenth program
'''
num=int(input("Enter the number"))
if(num>0):
    if(num%2==0):
        print("The given number is even")
    else:
        print("The given number is odd")
else:
    print("Enter a positive number")
'''
#Loop
'''
for i in range(5):
    print(i)
#while loop
count=0
while count<5:
    print(count)
    count+=1
'''
#eighteenth program
'''
for i in range(1,11):
    print(i)
'''
#ninteenth program
'''
sum=0
i=1
while(i<11):
    sum+=i
    i+=1
print(sum)

#twentieth program

num=int(input("Enter the number for required table"))
for i in range(1,11):
    print(num*i)

#21th program
num=int(input("Enter the number for factorial "))
i=1
fact=1
print("Factorial is")
while(i<num):
    fact*=i
    i+=1
print(fact)
'''
#22th program
'''
n=int(input("Enter the number"))
rev=0
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("The reverse of given number is",rev)
#Loops over String
text="Python" 
for words in text:
    print(words)
'''