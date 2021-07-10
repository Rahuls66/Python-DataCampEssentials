# Generators creates a generator object on creation, while list comprehension creates a list which will stored in memory
# Genrators can be iterated over as well using next() or loops.

# Create generator object: result
result = (num for num in range(0,31))

# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Print the rest of the values
for value in result:
    print(value)

'''
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
''' 
