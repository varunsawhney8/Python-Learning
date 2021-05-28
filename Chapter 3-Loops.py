# Chapter-3 Loops, conditional statements


# If statement

age=int(input(" Enter your age: "))

if age>10:
    print(" You are pro")
    
# Error    
# x=18
# if x>18:

    
x=18
if x>18:
    pass

# IF else


age=int(input(" Enter your age: "))

if age>10:
    print(" You are pro")
else:
    print(" You need practice")
    
    
    
    
# Use of and and or operator
# and - &
# Or  - |
# ==


x=5
y=7

x>4 and y<10

x>5 and y<10
x>5 or y<10


if (x>4 and y<10):
    print("condition true")
else:
    print(" condition false")

    
if (x>5 and y<10):
    print("condition true")
else:
    print(" condition false")
    
  
    
# Check EMpty Strings

a=input("enter a name: ")

if a:      # True when there is something in sting
    print(f"Hello {a}")
else:
    print("NO Input")
    


# Elif Statements

a=5
b=8
c=9

if a>b and a>c:
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
else:
    print("c is greatest")


# While Loops


print("Hello"*100)


# While loop requires iteration variable to end the loop


i=0
while i<=10:
    print(i)
    i+=1
    
    


# For Loop with range function


# Exercise sum of 1 to 10
s=0
for i in range(1,10):
    print(i)
    s+=i
    i=i+1
    
s

# Exercise practice sum of all digits in a number


# Convert integer to string and do the math operation

x=input(" ENter any number for which ypu want to calculate sum of digits: ")

for i in str(x):
   s+=int(i)
   
print(s)


# Check the count of each character in a string

x=input("Enter any name")

for i in x:
    print(f" {i}:{x.count(i)}")


# Break and Continue Statements


# Break- breaks the loop
# Continue- Takes back to the loop






