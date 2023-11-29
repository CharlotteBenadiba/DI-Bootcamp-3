# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints one sentence 
# telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

#def display_message():
#    print("I'm learning in developers.institute.")

#display_message()

# Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when 
# calling the function.

#def favorite_book(title):
#    print("One of my favorite books is " + title)

# favorite_book("Alice in Wonderland")

# Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city 
# and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

#def describe_city(city, country="Some country"):
#    print(city + " is in " + country)

# describe_city("Reykjavik", "Iceland")
# describe_city("Rio")

# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates 
# another number randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, display a success message, 
# otherwise show a fail message and display both numbers.

# import random

#def compare_numbers(user_number):
#    random_number = random.randint(1, 100)
#    print("Generated random number:", random_number)

#    if user_number == random_number:
#        print("Success! The numbers match.")
#    else:
#        print("Fail! The numbers don't match.")
    
#    print(f"User's number: {user_number}, random number: {random_number}")

#user_input = int(input("Enter a number between 1 and 100: "))
#compare_numbers(user_input)

# Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text 
# of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt 
# and the message printed on it, such as "The size of the shirt is <size> 
# and the text is <text>"
# Call the function make_shirt().
# Modify the make_shirt() function so that shirts are large by default 
# with a message that reads “I love Python” by default.
# Make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.
# Bonus: Call the function make_shirt() using keyword arguments.

#def make_shirt(size="large", text="I love Python"):
#    print(f"The size of the shirt is {size} and the text is '{text}'")

#make_shirt()
#make_shirt(size="medium")
#make_shirt(size="small", text="Python is cool!")

# Bonus:
#make_shirt(text="I love developers.institute!", size="extra-large")

#  Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# Create a function called show_magicians(), which prints the name of each 
# magician in the list.
# Write a function called make_great() that modifies the original list 
# of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.

#def show_magicians(magicians):
#    for magician in magicians:
#        print(magician)

#def make_great(magicians):

#    for i in range(len(magicians)):
#        magicians[i] += " the Great"

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# show_magicians(magician_names)

# make_great(magician_names)
# show_magicians(magician_names)

# Exercise 7 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), 
# selected at random.
# Test your function to make sure it generates expected results.
# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store 
# its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature 
# right now is 32 degrees Celsius.”
# Let’s add more functionality to the main() function. Write some friendly 
# advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40
# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between 
# -10 and 40, set lower and upper limits based on the season, eg. if season 
# is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that 
# we can call the function correctly. Ask the user to type in a season - 
# ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().
# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the 
# month (1 = January, 12 = December). Determine the season according to the month.

# import random

#def get_random_temp(input_value):
#    valid_seasons = ['summer', 'autumn', 'fall', 'winter', 'spring']

#    if input_value.isdigit() and 1 <= int(input_value) <= 12:
#        month = int(input_value)
#        if 6 <= month <= 8: 
#            return round(random.uniform(16, 40), 1)
#        elif 9 <= month <= 11 or 1 <= month <= 2:  
#            return round(random.uniform(0, 23), 1)
#        elif 12 <= month <= 2 or 3 <= month <= 5:  
#            return round(random.uniform(-10, 16), 1)
#        elif 6 <= month <= 8 or 9 <= month <= 11:  
#            return round(random.uniform(0, 23), 1)
#    elif input_value.lower() in valid_seasons:
#        season = input_value.lower()
#        if season == 'summer':
#            return round(random.uniform(16, 40), 1)
#        elif season == 'autumn' or season == 'fall':
#            return round(random.uniform(0, 23), 1)
#        elif season == 'winter':
#            return round(random.uniform(-10, 16), 1)
#        elif season == 'spring':
#            return round(random.uniform(0, 23), 1)
#    else:
#        return None

#def main():
    
    #input_value = input("Enter the season ('summer', 'autumn', 'winter', 'spring') or the number of the month (1-12): ")
    #temperature = get_random_temp(input_value)

    #if temperature is not None:
    #    print(f"The temperature right now is {temperature} degrees Celsius.")

    #    if temperature < 0:
    #        print("Brrr, that's freezing! Wear some extra layers today.")
    #    elif 0 <= temperature < 16:
    #        print("Quite chilly! Don't forget your coat.")
    #    elif 16 <= temperature < 23:
    #        print("It's a pleasant day. Enjoy the weather!")
    #    elif 24 <= temperature < 32:
    #        print("Warm weather! Stay hydrated.")
    #    elif 32 <= temperature <= 40:
    #        print("Hot day! Consider staying indoors or using sunscreen.")
    #    else:
     #       print("There are no recommendations for this temperature.")
    #else:
    #    print("Incorrect input. Please write a valid season or month.")

# main()

 # Exercise 8 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives 
# different messages depending on how well they did on the quiz.
# Here is an array of dictionaries, containing those questions and answers

# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.

# import random

# data = [
#    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
#    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
#    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
#    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
#    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
#    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
#]

#def quiz():
#    correct_answers = 0
#    incorrect_answers = 0
#    wrong_answers = []

#    random.shuffle(data) 

#    for question_data in data:
#        question = question_data["question"]
#        correct_answer = question_data["answer"]

#        user_answer = input(question + " ")
#        user_answer = user_answer.strip()

#        if user_answer.lower() == correct_answer.lower():
#            print("Correct!\n")
#            correct_answers += 1
#        else:
#            print(f"Incorrect. The correct answer is {correct_answer}.\n")
#            incorrect_answers += 1
#            wrong_answers.append({"question": question, "user_answer": user_answer, "correct_answer": correct_answer})

 #   show_results(correct_answers, incorrect_answers, wrong_answers)

#def show_results(correct, incorrect, wrong_answers):
#    print("=== Quiz Results ===")
#    print(f"Correct Answers: {correct}")
#    print(f"Incorrect Answers: {incorrect}")

#    if incorrect > 0:
#        print("\n=== Questions You Answered Incorrectly ===")
#        for wrong_answer in wrong_answers:
#            print(f"Question: {wrong_answer['question']}")
#            print(f"Your Answer: {wrong_answer['user_answer']}")
#            print(f"Correct Answer: {wrong_answer['correct_answer']}\n")

#    if incorrect > 3:
#        print("You had more than 3 wrong answers. Consider playing again.")

# quiz()









