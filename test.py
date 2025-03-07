# age = int(input("Inter your age:"))
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")

##Loops
numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total += num

print("Total sum for :", total)

numbers = [10, 20, 30, 40, 60]

total = 0
i     = 0

while i < len(numbers):  
    total += numbers[i]
    i += 1

print("Total sum while:", total)