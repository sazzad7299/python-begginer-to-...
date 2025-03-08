### 1. Variables and Data Types
```python
name = "Alice"  # String
grade = 95       # Integer
height = 5.6     # Float
is_active = True # Boolean
```

### 2. Conditional Statements
```python
age = int(input("Inter your age:"))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```
### 3. Loops
#### a) For Loop
```python
numbers = [10, 20, 30, 40, 50]  

total = 0 

for num in numbers:
    total += num 

print("Total sum:", total)
```
#### b) While Loop
```python
numbers = [10, 20, 30, 40, 60]

total = 0
i     = 0

while i < len(numbers):  
    total += numbers[i]
    i += 1

print("Total sum:", total)
```
### 4. Functions
```python
n = str(input("Enter your name:"))

def greet(name):
    return f"Hello, Nice to meet you, {name}!"

print(greet(n))
```
#### Example 
get  total prime numbers and list of prime number from 0 to given number N
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n ** 0.5) +1):
        if n % i == 0:
            return False
    return True
def count_primes(limit):
    prime_numbers =[num for num in range(limit+1) if is_prime(num)]
    return len(prime_numbers), prime_numbers

num = int(input("Enter a Number"))
prime_count, prime_list = count_primes(num)
print(f"Total prime numbers from 0 to {num} : {prime_count}")
print("prime Numbers:", prime_list)
```
### 5. List Comprehensions
```python
numbers = [x for x in range(10) if x % 2 == 0]
print(numbers)  
# Output: [0, 2, 4, 6, 8]
#example 2
A= [1,3,5,7]
B =[ 2,4,6,8]
cartesian_product = [ (a,b) for a in A for b in B]
print(cartesian_product)
#Output :[(1, 2), (1, 4), (1, 6), (1, 8), (3, 2), (3, 4), (3, 6), (3, 8), (5, 2), (5, 4), (5, 6), (5, 8), (7, 2), (7, 4), (7, 6), (7, 8)]
```
### 6. Dictionary Manipulation
```python
# Initialize a dictionary with user details
user_info = {
    "name": "Alice",
    "age": 28,
    "city": "New York",
    "skills": ["Python", "Django", "Machine Learning"]
}

# Add a new key-value pair
user_info["email"] = "alice@example.com"

# Update an existing value
user_info["age"] += 1  # Increment age

# Append a new skill to the skills list
user_info["skills"].append("Data Science")

# Remove a key using del
del user_info["city"]

# Check if a key exists
if "email" in user_info:
    print("Email:", user_info["email"])

# Iterating over dictionary keys and values
print("\nUser Info:")
for key, value in user_info.items():
    print(f"{key}: {value}")

# Using dictionary comprehension to transform data (Convert all keys to uppercase)
upper_keys_dict = {key.upper(): value for key, value in user_info.items()}
print("\nUppercase Keys Dictionary:", upper_keys_dict)

```

### 7. Exception Handling
```python

try:
    a = int(input("Enter a Number divided for:\n"))
    b = int(input("Enter a Number divided by:\n"))
    print(a/b)
except ValueError as e:
    print("Given Input is wrong,",e)
except ZeroDivisionError as e:
    print(" Divided by 0 is not possible",e)
except Exception as e:
    print("Some went wrong:", e)
finally:
    print("Thank You!!!")
```