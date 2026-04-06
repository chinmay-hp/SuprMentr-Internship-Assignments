# Smart Input Program

# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

# Categorizing age using conditionals
if age < 13:
    category = "a Child"
elif age < 20:
    category = "a Teenager"
elif age < 60:
    category = "an Adult"
else:
    category = "a Senior Citizen"

# Printing personalized message
print("\n----- Personalized Message -----")
print(f"Hello, {name}!")
print(f"You are {age} years old, which means you are {category}.")
print(f"It's great that you enjoy {hobby}. Keep having fun and learning new things!")