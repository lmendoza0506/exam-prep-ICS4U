# 1) Map vs Filter Iteration - They both apply a given function (lambda) to each item in an iterable (usually a list)
temps_C = [10, 20, 25, 30, 45, 40]  # In celsius

# MAP - Convert from celsius to fahrenheit
temps_F = list(map(lambda x : (x * (9/5) + 32), temps_C))
print(temps_F)
## Returns a new iterable containing the resulting values after the function is applied

# FILTER - Extract only the even values
temps_even = list(filter(lambda x : x % 2 == 0, temps_C))
print(temps_even)
## Returns a new itrable containing only the items that satisfy the function's condition

# 2) Reduce Iteration
from functools import reduce
nums = [1, 2, 3, 4, 5]

# REDUCE - Find the factorial of the numbers in the list
fact = reduce(lambda x, y: x * y, nums)
print(fact)
## Returns a single, accumulated result after taking a binary function (takes two arguments) and apply it cumulatively to the items in an iterable

# 3) Import Collections
import collections
from pprint import pprint

# NAMED TUPLE - Access attribute (field) 'name' of contact1 the namedtuple instance
Contact = collections.namedtuple('Contact', ['name', 'email', 'phone'])

contact1 = Contact('Sloppy Joe', 'joe@gmail.com', 123456789)
contact2 = Contact('Graham Cracker', 'graham@outlook.com', 987654321)

print(contact1.name)

# 4) Advantages of Functional Programming Paradigm; Where is the data stored?

## IMMUTABLE DATA - Cannot be modified once it is created; Does NOT depend on variable state
## PURE FUNCTIONS - Does NOT destroy original data structure when data is passed through; Always same output for same input
## Allows faster processing via multi-threading

# 5) Lambda Functions vs Regular Functions

# LAMBDA - 'In-line' function used for simple operations and convenience

# 6) List Comprehensions: Applications and Structure

## Pythonic way to filter, map, and reduce - Create a NEW list from an existing list based on an applied expression
## Structure: 
# I) For Loop: 
# list = []
# for item in iterable:
    # if condition:
        # list.append(expression)
# II) Concise:
# list = [expression for item in iterable if condition]

## LIST COMPREHENSION - New list that contains the squares of only the odd numbers in the original list
og_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list_1 = []
for x in og_list:
    if x % 2 != 0:
        new_list_1.append(x ** 2)
print(new_list_1)

new_list_2 = [x ** 2 for x in og_list if x % 2 != 0]
print(new_list_2)