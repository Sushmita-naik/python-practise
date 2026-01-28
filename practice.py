
print("Sushmita")
print(10 + 20)
print("Python practice")


while True:
    n = int(input("Enter number (0 to stop): "))
    if n == 0:
        break
    print("You entered", n)
fruits = ["apple", "banana", "mango"]
print(fruits[0])   # apple
fruits.append("orange")
print(fruits)

def greet(name):
    print("Hello world")
greet("Sushmita")
greet("Python learner")

name=input("Enter your name")
print(name)
print("Hello",name)

number=int(input("Enter the number"))
print(number)
if number%2==0:
    print("even")
else:
    print("Odd")

num1=int(input("Enter the num1"))
num2=int(input("enter the num2"))
if num1>num2:
    print("num1 is greater", num1)
else:
    print("Num2 is greter", num2)


for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()
a=0
b=1
sequence=int(input("Enter the number of sequenses:"))
for i in range(sequence):
    c=a+b
    print(c)
    a=b
    b=c

sequence=int(input("Enter the number of sequences:"))
num=(input("Enter the numbers:"))
for i in range(sequence):
        
 if num == num[::-1]:
        print("Palindrome")
 else:
        print("Not palindrome")

num = input("Enter a word: ")
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

num=int(input("Enter the number:"))
if num<=1:
    print("Not prime")
else:
    for i in range(2,num):
        if num%i==0:
            print("Not prime")
            break
    else:
         print("Prime")

name=input("Enter the name:")
print(name)
print(name[::-1])

num=int(input("Enter the number:"))
rev =0

while(num>0):
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)

sum=0
n=int(input("Enter how many number"))
for i in range(n):
    num=int(input("Enter a number:"))
    sum=sum+num
print(sum)

sum = 0
n = int(input("Enter how many numbers: "))

for i in range(n):
    num = int(input("Enter a number: "))
    sum = sum + num

print("Sum =", sum)

count=0
word=input("Enter the word:")
for ch in word:
    if ch in "aeiou":
        count=count+1
print(count)

n1=int(input("Enter the n1"))
print(n1)
n2=int(input("Enter n2:"))
print(n2)
for i in range(n1,n2,2):
    print(i)
print("These are even numbres")
for i in range(n1,n2+1):
    if i%2 !=0:
        print(i)
print("these are odd numbers:")

year=int(input("Enter a year:"))
if year%4==0 and year%100!=0 or year%400==0:
    print("Leap year")
else:
    print("Not a leap year")

fact=1
n=int(input("Enter the number:"))
print(n)
for i in range(1,n+1):
    fact=fact*i
print(fact)

import random

secret = random.randint(1, 20)

while True:
    guess = int(input("Guess a number between 1 and 20: "))

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct! You guessed it 🎉")
        break

for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()


# lists tuples and dictionary
marks=[14,45,67.7,99.9]
print(marks)
print(type(marks))
print(marks[2])
print(len(marks))

# list slicing 
marks=[99, 90, 0.99, 78.8]
print(marks)
print(marks[1:4])
print(marks[-4:-1])

# list methods
student=["Sushmita","Sharanya","Sammu","Nishmi","Ranju"]
print(student)
student.append("sharadvi")
print(student)

marks=[99.9, 89,9, 78.8, 67,8]
print(marks)
marks.reverse()
print(marks)
marks.insert(3,100)
print(marks)
print(marks.sort())
print(marks.sort(reverse=True))

nums=[10,20,30,40,50]
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[-1])
print(nums[-2])
print(nums[1:])
print(nums[0:7])
print(nums[2:5])
print(nums[0:7:2])
print(nums[1:7:2])
print(nums[0:7:2])
print(nums[::-1])
print(nums[-1:-5])

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[-4:])
print(letters[0:5])
print(letters[-5:][::-1])
print(letters[-6:-2])

data=[5,10,15,20,25,30,35,40]
data.pop(7)
data.pop(6)
print(data)
print(data[0:4])
print(data[4:])
print(data[0:4]+data[4:])
print(data[::-1])

text="PYTHONPROGRAM"
print(text[0:6])
print(text[-7:])
print(text[0:14:2])
print(text[::-1])
print(text[6:])

# hiding numbers
phoneno=input("Enter your phone no:")
markes=phoneno[:2]+"*" * (len(phoneno)-4) +phoneno[-2:]
print("The phone no is", markes)

emailid=input("Enter your mail ID:")
print(emailid)
username=emailid[0:12]
print(username)
Domain=emailid[12:]
print(Domain)

name=input("Enter your input:")
print(name)
reverse=name[::-1]
print(reverse)

word=input("Enter the word:")
correct=word[0:]
print(correct)
reverse=word[::-1]
print(reverse)
if correct==reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

creditcard=input("Enter the credit card no:")
last4=creditcard[-4:]
hidden_length=len(creditcard)-4
stars="*" * hidden_length
hide=stars+last4
print("hided card number is:", hide)


tuple in python
tuple=(1,2,3,4,56)
print(type(tuple))
print(tuple[0])
print(tuple[1])
tup=()
print(tup)
tup=(1)
print(type(tup))
slicing
tup=(12,34,56,78)
print(tup[2:4])
print(tup.index(56))
print(tup.count(12))

list=[]
for i in range(3):
   movies=input("Enter 3 favorite movies")
   print(movies)
   list.append(movies)
   print(list)

list1=[1,2,3,2,1]
list2=[5,6,7,8,9]
copy_list1=list.copy()
copy_list1.reverse()

if list==copy_list1:
    print("palindrome")
else:
    print("Not a palindrome")


tuple=("C","D","A","A","B","B","A")
print(tuple.count("A"))

list=["C","D","A","A","B","B","A"]
list.sort()
print(list)

numbers=(4,8,1,9,2)
print(len(numbers))
print(max(numbers))
print(min(numbers))

student=("Sushmita",17,"Airtificial Imtelligence")
print("Name",student[0],", Age",student[1],", Branch",student[2])

a=5
b=10
a,b=b,a
print(a)
print(b)

marks=[23,45,67,89,90]
marks_tuple=tuple(marks)
print(marks_tuple)
print(type(marks_tuple))

marks=(23,45,67,89,90)
marks_list=list(marks)
print(marks_list)
print(type(marks_list))

data=(10,20,30,40,50)
data_list=list(data)
print(data_list)
print(type(data_list))
index_of_30=data_list.index(30)
data_list[index_of_30]=300
print(data_list)
data=tuple(data_list)
print(data)

student = ("Sushmita", 17, "A", 89.5)
print(student[0],"is",student[1],"years old and scored",student[3])

temps = (32, 35, 31, 30, 33, 36, 34)
avg_temp=sum(temps)/len(temps)
print(avg_temp)
print(max(temps))
for t in temps:
    if t>33:
        print(t)

products = (
    ("Pen", 10),
    ("Notebook", 50),
    ("Bag", 500),
    ("Bottle", 120)
)
print("Products name")
for product in products:
    print(product[0])
print("Products costing more than 100:")
for product in products:
    if product[1]>100:
        print(product[0]," ",product[1])
total_cost=0
for product in products:
    total_cost=total_cost+product[1]
print("The total cost is:", total_cost)




        
    







