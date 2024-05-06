# in file: hello.py

greetings = ["Hello", "Bonjour", "Hola"]

for greeting in greetings:
    print(f"{greeting}, World!")


# shortcuts for REPL: help(), type(), and dir()

# int, floats, 42j is a complex number
#min(), max(), round()

# list method len() for length

# sets, tuples, dictionaries

# list []

# ! Tuples
# ligth-weight collections used to keep track of related but different items.
# Tuples are immutable. Tuples are sorted
# tuple () with , e.g. (,)
# tuple unpacking, immutable

# ! Sets
# sets: used for storing immutable data types uniquely. They are fast!
# {1, 2, 3} cannot contain duplicate values
# cannot contain mutable data types. If you can't hash() it, then it can't be in a set.
# order doesn't matter
# .add(), .discard() for editing sets. .update() can combine sets

# ! Dictionaries
# Dictionary keys must be immutable, store key/value pairs
# {key:value}
# .get() gets a value if key exists, doesn't throw an exception if that doesn't exist.
#   Can return a defaut if key doesn't exist.
# .update() will combine dictionaries.
# .keys() will return keys, .value() returns values.
# .items() returns all key value pairs, helpful for looping.

# ! Functions
# def my_function(x, y, z=1):
#   return x + y + z
#
# Don't use mutable types as default arguments for functions!

# ! Booleans
# int : 0 is false, all else are true.
# containers : empty is False, containers with items are True.
# None type is always false.
# bool() indicates its truthiness.
# 'is' keyword points to same place in memory

# if, else, elif

# ! Loops
# for color in colors:
#   print(f"The Color is: {color})
