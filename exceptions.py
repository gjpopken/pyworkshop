# exceptions.py

# this will throw an exception!
try:
    int("a")
except ValueError:
    print('An exception happened.')
except KeyError:
    print('A key error happened.')

print("End of the program.")
