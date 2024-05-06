names = ["Nina", "Max", "Rose", "Jimmy"]
my_list = [] # empty list
for name in names:
    my_list.append(len(name))
print(my_list)


# List comprehension
my_list = [name for name in names if len(name) % 2 == 0]
print(f"After: {my_list}")

# Generator
my_list = (name for name in names if len(name) % 2 == 0)
