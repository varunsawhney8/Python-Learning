# List- Mutable

# Ordered collection of data
# Can store anything in a list- integer, float, string, independent list


x=[1,2,3,'a']

y=[1,4,[5,6]]

y

# Access list, splicing


x[1]

x[1:]
x[::-1]
x[:]
x[2:]

# Changes in list
y=[1,2,3,4]

y[2]=[8]

y

# Append
x.append(5)

# Extend,
x=[4,5,6]
y=[8,7,9]

x.extend(y)
x

# Insert Function

y=[1,2,3,4]


y.insert(2, 10)

y


# Delete from list- pop,del,remove


# Pop- deletes last value from the list

x=[2,5,8,7,9]

x.pop()

# Deletes a value of the index
x.pop(2)

# Del
x=[10,20,30,40]

del x[3]
x


# remove function- remove values

x=[5,78,59,746,5613]

x.remove(746)
x

# count,sort,reverse,sorted,clear,copy

fr=['or','ap','pr','ba','ki','ap','ba']

# Count

fr.count('ap')

# sort, sorted

# Copy

f=['a','b','d','c']

f1=f
f2=f.copy()

f1=f.sort()

dir(f)

# delete a list

del f

# List comparison

f=[1,4,8]
f1=[4,8,1]

f==f1

# String split

str1="varun sawhney"

a=str1.split(" ")
a

# Join a lsit to a string

str1="varun sawhney"

a=str1.split(" ")
a

print(' '.join(a))


# List               Vs   Array

# Ordered               # Ordered 
# Flexible data type    # Fix Data Types
#                         Good Performance
#                         Not much Used, numpy array are used inplace of array



# List          Vs      String

# Immutable         # Mutable


# Loop in List

fr=['or','ap','pr','ba','ki','ap','ba']

for i in fr:
    print(i)

i=1
while i<= len(fr):
    print(fr[i])
    i+=1
   
    
    
# List inside List


m=[[1,2,3],[4,5,6],[7,8,9]] # 2 D Array


len(m)
type(m)

# Accessig matrix

m[1][2]

# Accessing each variable seprately in array mode

for i in m:
    for j in i:
        print(j)


# Generate a list with range function


n=list(range(1,10,1))
n


# Index function- Provides position of the value

n.index(5,1,10)


# reverse function-


n1=n.reverse()
n1



# Define a function in a list and returns a negative value

def neg_list(l):
    neg=[]
    for i in l:
        neg.append(-1*i)
    return neg
        
        
list1=[1,2,3]

neg_list(list1)




# Reverse each word of list

def rev_word_list(l):
    neg=[]
    for i in l:
        neg.append(i[::-1])
    return neg
        


l=['abc','def']

rev_word_list(l)



# Seprate odd and even number in list




# INput 2 list and output common elements


# min in list and max in list

# Count how many lists are inside a list


