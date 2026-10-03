# list literal
fruits = ["apple", "mango", "orange"] 
print(fruits)

# tuple literal
numbers = (1, 2, 3) 
print(numbers)

# dictionary literal
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
print(alphabets)

# set literal
vowels = {'a', 'e', 'i' , 'o', 'u'} 
print(vowels)


# print with end whitespace
print('Good Morning!', end= ' ')

print('It is rainy today')


print('New Year', 2023, 'See you soon!', sep= '. ')

print('Programiz is ' + 'awesome.')

x = 5
y = 10

print('The value of x is {} and y is {}'.format(x,y))

# using input() to take user input
num = input('Enter a number: ')

print('You Entered:', num)

print('Data type of num:', type(num))

x = 15
y = 4
print('x + y = ',x+y)
print('x - y = ',x-y)
print('x * y = ',x*y)
print('x / y = ',x/y)
print('x % y = ',x%y)
print('x // y = ',x//y)
print('x ** y = ',x**y)



x = 10
y = 12
print('x > y  is',x>y)
print('x < y  is',x<y)
print('x == y is',x==y)
print('x != y is',x!=y)
print('x >= y is',x>=y)
print('x <= y is',x<=y)

x = True
y = False
print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x)

# Direct usage of complex literals
voltage = 3 + 4j
current = 1 + 2j

# Multiplying complex numbers directly
impedance = voltage * current
print(impedance)  # Output: (-5+10j)

x = True
y = False
print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x)

x = 10
y = 4

# Variables for binary operations
# a = 5 -> Binary: 0101
# b = 3 -> Binary: 0011
a = 5
b = 3

number = 10
print(f"{number:b}")  
# Output: 1010


print(f"Initial Values: a = {a} (bin: {bin(a)[2:]:>04}), b = {b} (bin: {bin(b)[2:]:>04})\n")

# 1. Bitwise AND (&)
# 0101 & 0011 = 0001
res_and = a & b
print(f"1. Bitwise AND (a & b)       : {res_and}  (Binary: {bin(res_and)[2:]:>04})")

# 2. Bitwise OR (|)
# 0101 | 0011 = 0111
res_or = a | b
print(f"2. Bitwise OR (a | b)        : {res_or}  (Binary: {bin(res_or)[2:]:>04})")

# 3. Bitwise XOR (^)
# 0101 ^ 0011 = 0110
res_xor = a ^ b
print(f"3. Bitwise XOR (a ^ b)       : {res_xor}  (Binary: {bin(res_xor)[2:]:>04})")

# 4. Bitwise NOT (~)
# Formula: ~x = -(x + 1). For 5, it becomes -(5 + 1) = -6
res_not = ~a
print(f"4. Bitwise NOT (~a)          : {res_not} (Binary: {bin(res_not)})")

# 5. Bitwise Left Shift (<<)
# 0101 << 1 = 1010 (Decimal 10). Shifts bits left, multiplies by 2^n.
res_lshift = a << 1
print(f"5. Bitwise Left Shift (a << 1): {res_lshift} (Binary: {bin(res_lshift)[2:]:>04})")

# 6. Bitwise Right Shift (>>)
# 0101 >> 1 = 0010 (Decimal 2). Shifts bits right, divides by 2^n (floor division).
res_rshift = a >> 1
print(f"6. Bitwise Right Shift (a >> 1): {res_rshift}  (Binary: {bin(res_rshift)[2:]:>04})")

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)

x = 'Hello world'
y = {1:'a',2:'b'}
print('H' in x)
print('hello' not in x)
print(1 in y)
print('a' in y)

# 0 is False

print("bool()")
print(bool(0))

# Non-zero value is True
print(bool(12))

# Non-empty string is True
print(bool("Python"))
print(bool("False"))  # True

# Empty string is False
print(bool(""))

age = 22
status = "Adult" if age >= 18 else "Minor"
print(status)

# Iterate from i = 1 to i = 10
for i in range(1, 11):
    print(f"Displaying product {i}")

    
language = 'Python'
revstr = ""
for x in language:
    revstr = x + revstr
print(revstr)

stock = ['Laptop', 'Keyboard', 'Mouse']

order = input("Enter the product you want to buy: ")

for product in stock:
    if product == order:
        print(f"{order} is available. Adding to cart.")
        break
else:
    print(f"Sorry, {order} is out of stock.")
    