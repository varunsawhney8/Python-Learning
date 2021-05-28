# Create a list of Squares from 1 to 10


squares=[]

for i in range(1,11):
    squares.append(i**2)
    

squares


# List Comprehension


# Append... Condition

Squares=[i**2 for i in range(1,11)]



# Create a list from 1 to 10 negative numbers

Neg=[i*-1 for i in range(1,11)]
Neg

# Names 

names=['Varun','rajat','anshu','pranshu']

l1=[i[0] for i in names]
l1



l2=[i[::-1] for i in names]
l2


# Create a function

def rev_str_list(l):
    return [i[::-1] for i in l]
    
a=rev_str_list(names)
a



# List COmprehension with if statement

num=list(range(1,11))

# Seprate Even numbers


nums=[]

for i in num:
    if i%2==0:
        nums.append(i)

print(nums)


even_nums=[ i for i in num if i%2==0]
even_nums    
odd_nums=[ i for i in num if i%2!=0]
odd_nums   
    
    
    
# Define a list which enters any type of data and extract each variable in 
    
    
# input: [False,True,[1,2,3],1,1.0,3]

# output:['1','1.0','3']

def ret_strnum(l):
    return [str(i) for i in l if (type(i)==int or type(i)==float)]

a=[1,2,[1,2,3],1,1.0,3]

a==list
type(a)
ret_strnum(a)    

# List Comprehension with IF Else


nums=list(range(1,11))


# Output [odd*-1,even*2]


new=[i*2 if i%2==0 else -1*i for i in nums]
new


# Nested Lists

example=[[1,2,3],[1,2,3],[1,2,3]]




# Create a nested list with list comprehension

nested_comp=[[i for i in range(1,4)] for j in range(1,4)]
nested_comp



# Summary
#1. 


















#     
    
    
    
    
    
    
    
