#Arithmetic Operators
#Q1
m=int(input("Enter a number"))
n=int(input("Enter second number"))
sum=m+n
print("Sum",sum)
differ=m-n
print("Difference",differ)
multiply=m*n
print("Product",multiply)
division=m/n
print("Quotient",division)

#Q2
m=15
n=4
floor=15//4
power=15**4
rem=15%4
print("Floor Division:",floor)
print("Power:",power)
print("Remainder:",rem)

#Q3
pen_price=15
notebook_price=40
total_cost=(3*pen_price)+(2*notebook_price)
print(total_cost)

#Q4
sum=0
for i in range(0,5):
    num=int(input("Enter the number"))
    sum=sum+num
avg=sum/5
print("Avg",avg)

#Q5
import math
a=int(input("Enter a number to calculate square"))
square=a**2
cube=a**3
print("Square:",square)
b=int(input("Enter the number to calculate square root"))
print("Square Root",math.sqrt(b))
c=int(input("Enter the number to calculate cube"))
print("Cube:",cube)

# Q6:convert seconds
sec=int(input("Enter the seconds"))
min=sec//60
seconds=sec%60
print("The seconds will be converted as:",min,"min(s) and",seconds,"second(s)")

#Q7:calculate speed
dist=120
time=3
speed=float(dist/time)
print("Speed will be:",speed)

# Q8: check whether first number is multiple of second number
first=int(input("Enter first number"))
second=int(input("Enter second number"))
if(first%second==0):
    print("The first element is multiple of second number")
else:
    print("The first number is not a multiple of second number")
    
# Q9: calculate Simple Interest
principle=float(input("Enter the principle amount"))
rate=float(input("Enter the rate"))
time=float(input("Enter the time in years"))
simpleinterest=(principle*rate*time)/100
print("The simple interest on given principal amount is:",simpleinterest)

#Q10: rounded quotient
num1=float(input("Enter the  first number"))
num2=float(input("Enter the second number"))
div=(num1//num2)
print("The rounded quotient is:",div)

#Comparison Operators
#Q1
num1=int(input("Enter a number"))
num2=int(input("Enter second number"))
if(num1==num2):
    print("The given numbers are equal")
else:
    print("Not equal")
    
#Q2
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
if(num1>num2):
    print("The first number is greater")
else:
    print("The second number is greater")
    
#Q3
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
    
#Q4
marks=int(input("Enter your marks"))
if(marks>=40):
    print("Pass")
else:
    print("Fail")
    
#Q5
age=int(input("Enter your age"))
if(age>=18):
    print("Eligible to vote")
else:
    print("Not Eligible")
    
#Q6
num=int(input("Enter the number"))
if(num%2==0):
    print("The given number is even")
else:
    print("The given number is odd")
    
#Q7: compare words
word1=input("Enter the first word")
word2=input("Enter second word")
if(word1==word2):
    print("Both words are same")
else:
    print("Both are different")
    
#Q8: compare salary of two employees
A=float(input("Enter the first employee's salary"))
B=float(input("Enter the second employee's salary"))
if(A>B):
    print("Employee A earns more")
else:
    print("Employee B earns more or equal")
    
# Q9:inclusive numbers between 10 & 50
num=int(input("Enter the number"))
if(num>10 and num<50):
    print("Yes,it lies between 10 and 50")
else:
    print("Not lies between 10 and 50")
    
# Q10:check leap year
year=int(input("Enter the year"))
if(year%400==0):
    print("This is leap year")
elif(year%100==0):
    print("This is not a leap year")
elif(year%4==0):
    print("This is a leap year")
else:
    print("Not a leap year")
    
#Logical Operators
#Q1
maths=int(input("Enter your maths marks"))
science=int(input("Enter your science marks"))
if(maths>40 or maths==40 and science>40 or science==40):
    print("Pass")
else:
    print("Fail")
    
#Q2
amt=int(input("Enter the purchase amount"))
card=input("Verify if you have membership card(yes or no)")
if((amt>1000)or (card.lower)=="yes"):
    print("You are eligible for discount")
else:
    print("You are not eligible for discount")
    
#Q3
num=int(input("Enter the number"))
if((num%3)!=0):
    print("The number is not divisible by 3")
else:
    print("The number is divisible by 3")
    
#Q4
age=int(input("Enter your age"))
if(age>=13 and age<=19):
    print("Teenager")
else:
    print("Not a Teenager")
    
#Q5
age=int(input("Enter your age"))
if(age>=18):
    print("You are eligible to vote")
else:
    print("Not eligible to vote")
if(age>=18 and age <=70):
    print("Eligible to drive")
else:
    print("Not eligible to drive")
    
#Q6:Check Exam eligibility
attend=float(input("Enter your attendance"))
assignment=input("Have you submitted your assignments:(yes/no)")
if(attend>=75 and assignment.lower==yes):
    print("You can sit for exam")
else:
    print("You cannot sit for exam")
    
#Q7:leap year using logical operators
year=int(input("Enter the year"))
if(year%4==0 and year%100!=0) or (year%400==0):
    print("It's a leap year")
else:
    print("It's not a leap year")
    
#Q8
day=input("Enter the day")
h=input("Tell is it a holiday?(yes/no)")
if(day.lower()=="sunday" or h.lower()=="yes"):
    print("Relax")
else:
    print("Keep doing work")
    
#Q9
num=int(input("Enter the number"))
if(num%3==0 and num%5==0):
    print(num,"number is divisible by both 3 and 5")
else:
    print("Not divisible")
    
#Q10:match login username and password
user=input("Enter the username")
password=input("Enter the password")
if(user.lower()=="admin" and password=="1234"):
    print("Login Successful")
else:
    print("Login failed")
    
#Assignment Operators
#Q1
num=10
print(num)

#Q2
num=int(input("Enter a number"))
num+=5
print(num)

#Q3
num=int(input("Enter a number"))
num-=3
print(num)

#Q4
num=int(input("Enter a number"))
num*=4
print(num)

#Q5
num=int(input("Enter a number"))
num/=2
print(num)

#Q6
num=int(input("Enter a number"))
num//=3
print(num)
#Q7
num=int(input("Enter a number"))
num%=7
print(num)

#Q8
num=int(input("Enter a number"))
num**=3
print(num)

#Loops
#Q1
print("The numbers upto 10 are:")
for i in range(1,11):
    print(i)
    
#Q2
sum=0
i=1
while(i<11):
    sum+=i
    i+=1
print(sum)

#Q3
num=int(input("Enter the number for required table"))
for i in range(1,11):
    print(num*i)
    
#Q4
num=int(input("Enter the number for factorial "))
i=1
fact=1
print("Factorial is")
while(i<num):
    fact*=i
    i+=1
print(fact)

#Q5
n=int(input("Enter the number"))
rev=0
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("The reverse of given number is",rev)

#Q6
print("The even numbers between 1 and 50 are:")
for evens in range(1,51):
    if(evens%2==0):
        print(evens)
        
#Q7
num=int(input("Enter a number"))
sum=0
while(num!=0):
    rem=num%10
    sum+=rem
    num//10
print(sum)

#Q8:Fibonacci Series upto first 10 terms
first=0
sec=1
i=0
while(i<8):
    sum=first+sec
    print(sum)
    first=sec
    sec=sum
    i+=1
    
#Data Structure
#List
#Q1
x=[1,4,8,9,12,14,18]
print(x[0])
print(x[-1])
print(len(x))

#Q2
sum=0
for i in range(len(x)):
    sum+=x[i]
print(sum)
print("Average is:",(sum/len(x)))

##Q3
fruits=["Litchi","Grapes","Mango","Guava","Kiwi"]
fruits.append("Banana")
fruits.insert(2,"Strawberry")
print(fruits)

#Q4
fruits=["Litchi","Grapes","Mango","Guava","Kiwi"]
fruits.remove("Litchi")
print(fruits)
print(fruits.pop())

#Q5
x=[1,2,4,5,6,3,4,2,4]
print(x.count(4))

#Q6
x=[1,2,3,4,5,6,7]
print(x)
find=int(input("Enter the element you want to search"))
for i in x:
    if(i==find):
        print("The element exists")
        break
else:
    print("The element does not exists")

#Q7
y=[3,4,8,9,1,2,3]
print(y.index(4))

#Q8
List=[3,4,8,9,1,2,3]
List.sort()
List.sort(reverse=True)
print(List)

#Q9
List=[3,4,8,9,1,2,3]
List.reverse()
print(List)

#Tuple
#Q1
t=(1,2,3,4,5)
print(t[0])
print(t[-1])

#Q2
t=(1,2,3,4,5)
print(len(t))

#Q3
fruits=("Mango","Banana","Litchi","Apple")
for i in fruits:
    print(i)
    
#Q4
fruits=("Mango","Banana","Litchi","Apple")
find=input("Enter the required element")
if find in fruits:
    print("The required fruit exists")
else:
    print("The element doesn't exists")
    
#Q5
fruits=("Mango","Banana","Litchi","Apple")
fruit=("Strawberry","Kiwi")
t=fruits+fruit
print(t)

#Q6
t=(3,4,5,6,3,2,1,3)
print(t.count(3))

#Q7
tup=(2,3,4,5,6,7,8,0,1,2)
print(tup.index(4))

#Q8
List=[3,4,5,6,7,12,18]
print(tuple(List))

#Q9
tup=(2,3,4,5,6,7,8,0,1,2)
List=list(tup)
List.remove(6)
List.append(10)
print(tuple(List))

#Q10
tup=((2,3),(3,8),19)
print(tup)

