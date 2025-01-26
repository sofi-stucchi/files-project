# Example 1: Print something in the screen
	
# print("Hello, I'm Sofia this is my first code")

# Example 2: Second letter in Sofia

name = input("Enter a name: ")

# Check if the name has at least two characters
if len(name) >= 2:
    first_letter = name[0]
    second_letter = name[1]
    third_letter = name[2]
    print(f"The second letter is: {second_letter}")
    print(f"The third letter is: {third_letter}")
else:
    print("The name is too short to have a second letter.")

# Example 3: My first loop

word = "Sofia"

for letter in word:
    print(letter)


# Example 4: Numbers

for num in range(1, 6):
    print(num)


