# Dictionaries are another type of composite data types and are also a collection
# of objects like tuples and lists.
# Like lists they are also mutable, dyanmic and can be nested.
# However a key difference is that they are unordered.


# Dictionaries are paired using keys unlike in lists and tuples where each item is assigned an index.

# Defining a dictionary

# A dictionary is defined within curly braces. Each key-value pair is separated using commas, 
# the key and values themselves are separated by colon.

d={'banana':'yellow','apple': 'red','grapes':'green'}
d

# You can use dict function as well.

d=dict([('banana','yellow'),('apple','red')])
d

# Each keys should have different values, python avoid duplicacy and takes the most recent value.

# Values can be put same 
