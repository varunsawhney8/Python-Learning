# Dictionary Comprehension

square={1:1,2:4,3:9}


#        Key:Values
square1={num:num**2 for num in range(1,11)}
square1


# Square of 1: 1


square2={f"Square of {num} is":num**2 for num in range(1,11)}
square2

for k,v in square2.items():
    print(f"{k}:{v}")
    
    
    
# Count a characheter in string


# "Harshit"

str1="varuna"
word_count={char:str1.count(char) for char in str1}
word_count

# If Else in Dictionary

#Output={1:odd,2:Even}



d1={num:('Even' if num%2==0 else 'Odd')for num in range(1,4)}
d1




# Sets comprehension

# s={}



s={k**2 for k in range(1,11)}
s


names=['Varun','sawhney']

s={i[0] for i in names}
s








