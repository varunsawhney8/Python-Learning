# Chapter 2.

# Strings-  imMUTABLE

fname= "varun"
lname="sawhney"

# general string operation

fullname=fname+lname
fullname

# concatenation
fullname=fname+" " +lname
fullname

# Multiplication on strings

fullname*5

# in operator

'varun' in fullname


# Functions

# like things can be added or subtracted exception for int and float

# The output will show error

fullname+8


# we can remove the error

fullname+ '8'

# type conversions

int('8')
str(8)
float(5)

# input 

x=input("enter a no.: ")
x
type(x)

# converting string to int

type(int(x))

# Exercise: Input two numbers and show in the print command

a=int(input(" ENter first number: "))
b=float(input(" ENter second number: "))
print("total is",a+b)

# Exercise: Take two input from user simulatneosly using split function

a,b=input(" Enter two numbers seprated by commas: ").split(",")
print(int(a)+int(b))

# split function can work by passing what criteria we need to split

# sting formatting

a=5
b=15

print("Sum of 2 numbers is {}, multiplication of 2 numbers is {}".format(a+b,a*b))

print(f"Sum of 2 numbers is {a+b}, multiplication of 2 numbers is {a*b}")


# Indexing and Accessing

word = "Keep Adapting"

letter=word[4]

print(letter)

# length 
word = "Keep Adapting"

len(word)

letters = "wenf bwehfwfnewfje    "
len(letters)

#finding
'''
'''
word = "Keep Adapting"
print(word.count('p')) # count how many times p is in the string

word.count("e")

print(word.find("keep")) # find the word t in the string
print(word.index("Adapting")) # find the letters Adapting in the string

s = "The world won't care about your self-esteem. The world will expect you to accomplish something BEFORE you feel good about yourself."

print(s.count('  '))

#Slicing
y="             "
print(y.count(' '))

word1 = "_$_the internet frees us from the responsibility of having to retain anything in our long-term memory@_."

print (word1[0])
print(word1[-1]) #get one char of the word
print (word1[0:1]) #get one char of the word (same as above)
print (word1[0:3]) #get the first three char
print (word1[:3]) #get the first three char
print (word1[-3:]) #get the last three char
print (word1[3:]) #get all but the three first char
print (word1[:-3]) #get all but the three last character
print (word1[3:-3]) #get all 


# spliting
word3 = 'Good health is not something we can buy. However, it can be an extremely valuable savings account.'

a = word3.split(' ')
a # Split on whitespace
['Good','health','is','not','something','we','can','buy.','However,','it','can','be','an','extremely','valuable','savings','account.']
type(a)

# Startswith / Endswith
word3 = 'Remain calm, because peace equals power.'
word3.startswith("R")
word3.endswith("e")
word3.endswith(".")

# Repeat string 

print( " * "* 10 )# 

# Replacing

word4 = "Live is HapLive is funny"

#              Replaced, replaced with 
word4.replace("Live", "Lead Life")

dir(word4)

# Find


word4.find('is')

# To find after a certain position
word4.find('is',6)

# Reversing
string = "eert a tsniaga pu mih deit yehT .meht htiw noil eht koot dna tserof eht otni emac sretnuh wef a ,yad enO "

print (''.join(reversed(string)))



# Step Argument

a="PYTHON IS NOT DIFFICULT"

# start: end: step/jump
a[::2]
a[::-1]


a.lower()
a.upper()
a.title()

# Center Function

# We need output as **varun**

name='varun'
name.center(9,"*")
name.center(6,'*')



name[4]
name[4]='t'
