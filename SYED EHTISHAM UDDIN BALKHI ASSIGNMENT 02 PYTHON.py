#line break
print("\n ex 3.17 \n  ")

# Define the list of strings to evaluate  Question 3.17

exp = [
    '2 * 3 + 1',
    'hello',
    "'hello' + ' ' + 'world!'",
    "'ASCII'.count('I')",
    'x = 5'
]

# For loop for evaluate this

for exp in exp:
    print(f"Evaluating: {exp}")
    try:
        result = eval(exp)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
    print()
    
#line break
print("\n ex 3.18,3.19 \n  ")
#  defined in the interactive shell Question 3.18 , 3.19

a, b, c = 3, 4, 5

# (a) If a is less than b

if a < b:
    print('OK')
else:
    print('NOT OK')

# (b) If c is less than b

if c < b:
    print('OK')
else:
    print('NOT OK')

# (c) If the sum of a and b is equal to c

if a + b == c:
    print('OK')
else:
    print('NOT OK')
    
# (d) If the sum of the squares a and b is equal to c squared

if a**2 + b**2 == c**2:
    print('OK')
else:
    print('NOT OK')

#line break
print("\n ex 3.20 \n  ")

#   for loop that iterates over a list of strings Question 3.20

lst = ['January', 'February', 'March']
for word in lst:
    print(word[:3])

lst = [2, 3, 4, 5, 6, 7, 8, 9]

# Iterate over each number in the list Question 3.21

#line break
print("\n ex 3.21 \n  ")


for numb in lst:
    if numb % 2 == 0:
        print(str(numb))

lst = [2, 3, 4, 5, 6, 7, 8, 9]


#line break
print("\n ex 3.22 \n  ")

# Iterate over each number in the list Question 3.22

for num in lst:
    square = num ** 2
    if square % 8 == 0:
        print(str(num))


#line break
print("\n ex 3.23 \n  ")

# Iterate over each number in the list Question 3.23

for num in range(2):
    print(num, end = ' ')
for num in range(1):
    print(num, end=' ')
for num in range(3, 7):
    print(num, end=' ')
for num in range(1, 2):
    print(num, end=' ')
for num in range(0, 4, 3):
    print(num, end=' ')
for num in range(5, 22, 4):
    print(num, end=' ')
