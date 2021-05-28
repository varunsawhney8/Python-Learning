# Tuples- Tuples are another ordered collection of objects like lists,
# excepts for 2 properties where they differ:
# Tuples are immutable
# Tuples are defined using parenthisis instead of square brackets.

x=(1,2,'s')
type(x)

y=(3,5)

# Concatenate
z=x+y

z

# Multiply

z*3

# in operator

1 in z

# Slicing

z[:]
z[1:]
z[::-1]

# Access Tuple

x[1]

t=(1,2,3,'cat')
x=(1,) # defining single object tuple
x

y=(1)
y
type(y)



# Access tuples is sames as list

t[1]
t[1:]
t[::-1]


# Why do we use tuples- tuples are more efficient if you want to create an ordered list of objects
# that doesn't need any modifications.
# When we use dictionary.



# Tuples packing and unpacking

t=(1,2) #Packing
(a,b)=t #Unpacking

# a is assigned as 1
a

# b is assigned as 2
b

(a,b,c)=(4,5,6)
a
b
c

x,y,z=1,2,3
x
type(x)

