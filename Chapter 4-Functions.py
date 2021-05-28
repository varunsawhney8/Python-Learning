# Functions  define and default parameters

# Syntax

# def functaion name:
#    operation/return something

def add_num(a,b):
    return a+b
    
add_num(5,1)

# Default parameters should be written after the non default parameters

def add_num(a,b,c=None):
    if c==None:
        return a+b
    else:
        return a+c+b
    
add_num(5,1)



def num_opr(a,b,kind='add'):
    if kind=='add':
        return a+b
    elif kind=='multiply':
        return a*b
    elif kind=='sub':
        return a-b
    else:
        return a/b
    
num_opr(5,5,'multiply')


# Define a function to return greatest number between two

def max(a,b):
    if a>b:
        return a
    return b

max(5,8)


# Define a function to return greates number between three

def max_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

max_three(5,8,7)


# Check a number is palindrome or not


def is_pal(x):
    s=str(x)
    if s==s[::-1]:
        print("No. is palindrom")
    else:
        print("No. is not palindrom")


x=int(input("Enter any no. to check whether it is palindrom or not: "))


is_pal(x)


# Print Fibonaci series

def fibo(x):
    if x==1:
        print(x)
    elif x==2:
        print("0\n1")
    else:
        a=0
        b=1
        print(f"{a}\n{b}")
        i=1
        for i in range(x-2):
           c=a+b
           print(f"{c}")
           a=b
           b=c
           
fibo(1)
fibo(2)
fibo(7)
