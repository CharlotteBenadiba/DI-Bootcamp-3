# Review Exercises
# Conditions
# 1. Write code that gets three words from a user and inputs them into a sentence using
# F-Strings.
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
word3 = input("Enter the third word: ")

sentence = f"The input sentence is: {word1} {word2} {word3}"
print(sentence)

# 2. Exercise: Write a list that contains 2 strings. Print the second string in uppercase and
# then the first string backwards.
my_list = ["hello", "world"]
print(my_list[1].upper())
print(my_list[0][::-1])


# 3. Write code for a list that contains four names and prints every other name.
names = ["Alice", "Anna", "David", "Michael"]
print("Every other name:", names[::2])


# 4. Write code for a list of numbers. Ask a user for a new number and insert it into the list,
# second from the end.
numbers = [1, 2, 3, 4, 5]
new_number = int(input("Enter a new number: "))
numbers.insert(-2, new_number)
print("Updated list:", numbers)


# 5. Exercise: Create a dictionary containing the following information about you: your name,
# your age, your gender, your favorite food. Be sure to use appropriate keys.
info_about_me = {
    "name": "Anna",
    "age": 38,
    "gender": "Female",
    "favorite_food": "Shawarma"
}
print("My information:", info_about_me)


# 6. Exercise: A user is allowed to drive home if their blood alcohol is less than 0.5 %. Ask a
# user for their blood alcohol level and if they're not sober, tell them to take a cab.
blood_alcohol_level = float(input("Enter your blood alcohol level: "))
if blood_alcohol_level >= 0.5:
    print("It's not safe to drive. Please take a cab.")
else:
    print("You're sober. You can drive.")


# 7. Exercise: If a user is male and over 65 or female and over 60, they may retire. Get a
# gender and age from the user and let them know if it's time to retire.
gender = input("Enter your gender (Male/Female): ").lower()
age = int(input("Enter your age: "))

if (gender == "male" and age > 65) or (gender == "female" and age > 60):
    print("It's time to retire!")
else:
    print("Keep working; it's not time to retire yet.")


# Loops
# 8. Exercise: Write a loop to print every number between 10 and 20.
for num in range(10, 21):
    print(num)

# 9. Exercise: Write a loop to print every odd number between 1 and 20.
for num in range(1, 21, 2):
    print(num)

# 10. Exercise: Write code with a list of five names. Print the names one by one using a loop.
names = ["Anna", "Diana", "Bob", "David", "Michele"]
for name in names:
    print(name)
    
# 11. Exercise: Write a loop that takes numbers from the user until it receives the number 0
# and prints the sum of the numbers received.
sum_numbers = 0
while True:
    num = int(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    sum_numbers += num

print("Sum of numbers:", sum_numbers)
    
# 12. Exercise: Write a loop that takes words from the user until it receives the word 'done' and
# prints the longest word received.
longest_word = ""
while True:
    word = input("Enter a word (enter 'done' to stop): ")
    if word.lower() == 'done':
        break
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)

# Functions
# 13. Exercise: Write a function that takes a string as input and prints its length:
def print_length():
    input_string = input("Enter a string: ")
    length = len(input_string)
    print(f"The length of the string is: {length}")

print_length()

# 14. Exercise: Define a function that takes three numbers and prints their average.
def calculate_average(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    print(f"The average is: {average}")

calculate_average(10, 20, 30)

# 15. Exercise: Define a function that takes two arguments, a string and a number and checks
# if the string has more characters than the number. Example: 'string', 3 prints True since
# string has 5 characters.
def compare_length(string, number):
    result = len(string) > number
    print(result)

compare_length('string', 3) 

# 16. Exercise: Write a function that copies a string a certain number of times, based on the
# input. Set the default amount of copies to be 1.
def copy_string():
    input_string = input("Enter a string: ")
    num_copies = int(input("Enter the number of copies: "))
    result = input_string * num_copies
    print(result)

copy_string()







