# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# with open("Input/Letters/starting_letter.txt") as file:
#     content = file.readlines()
# print(content)


PLACEHOLDER = "[name]"

# You can use readlines() method instead of splitlines() method. But I recommend to use splitlines() as it doesn't take \n space or blah blah blah...

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.read().splitlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)
