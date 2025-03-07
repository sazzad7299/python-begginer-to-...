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
