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