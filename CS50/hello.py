# Ask user for their name
name = input("What's yout name? ").strip().title()

#remove whitespace from str
#name = name.strip()

# Capitilize user's name
#name = name.capatilize()

# Title capitilize user's name
#name = name.title()

# Remove whitespace from str and capitilize user's name
#name = name.strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
#print('Hello, ', name)
print(f"Hello, {first}")

#print("Hello, \"friend\"")

