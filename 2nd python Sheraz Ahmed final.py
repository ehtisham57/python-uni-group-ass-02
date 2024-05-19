# Define the list of strings to evaluate  Question 3.17

expressions = [
    '2 * 3 + 1',
    'hello',
    "'hello' + ' ' + 'world!'",
    "'ASCII'.count('I')",
    'x = 5'
]
for expression in expressions:
    print(f"Evaluating: {expression}")
    try:
        result = eval(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
    print()

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

#   for loop that iterates over a list of strings Question 3.20

lst = ['January', 'February', 'March']
for word in lst:
    print(word[:3])

lst = [2, 3, 4, 5, 6, 7, 8, 9]

# Iterate over each number in the list Question 3.21

for number in lst:
    if number % 2 == 0:
        print(number)

lst = [2, 3, 4, 5, 6, 7, 8, 9]

# Iterate over each number in the list Question 3.22
for number in lst:
    square = number ** 2
    if square % 8 == 0:
        print(number)

# Iterate over each number in the list Question 3.23

for num in range(2):
    print(num, end=' ')
for num in range(1):
    print(num)
for num in range(3, 7):
    print(num, end=' ')
for num in range(1, 2):
    print(num)
for num in range(0, 4, 3):
    print(num, end=' ')
for num in range(5, 22, 4):
    print(num, end=' ')
