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