#Exercise 1 : Hello World
#Instructions
#Print the following output in one line of code:

#Hello world
#Hello world
#Hello world
#Hello world

#print('''
      #Hello World 
      #Hello World 
      #Hello World 
      #Hello World
      #''')

#Exercise 2 : Some Math
#Instructions
#Write code that calculates the result of: (99^3)*8 
#(meaning 99 to the power of 3, times 8).

#print((99 ** 3) * 8)

#Exercise 3 : What Is The Output ?
#Instructions
#Predict the output of the following code snippets:

#snippet1 = 5 < 3
#snippet2 = 3 == 3
#snippet3 = 3 == "3"
# #snippet4 will raise a TypeError, that's why commenting it out
# #snippet4 = "3" > 3
#snippet5 = "Hello" == "hello"

#print(snippet1)
#print(snippet2)
#print(snippet3)
# #print(snippet4)
#print(snippet5)

# Exercise 4 : Your Computer Brand
#Instructions
#Create a variable called computer_brand which value is the 
#brand name of your computer.
#Using the computer_brand variable print a sentence that states 
#the following: "I have a <computer_brand> computer".

#computer_brand = "acer"
#print(f'I have a {computer_brand} computer')

#Exercise 5 : Your Information
#Instructions
# 1.Create a variable called name, and set it’s value to your name.
# 2. Create a variable called age, and set it’s value to your age.
# 3. Create a variable called shoe_size, and set it’s value to your shoe size.
# 4. Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# 5. Have your code print the info message.
# 6. Run your code

#name = "Anna"
#age = 38
#shoe_size = 34
#info = f"Hi there! My name is {name}, I am {age} years old, \
#and my shoe size is {shoe_size}."
#print(info)

#Exercise 6 : A & B
#Instructions
#Create two variables, a and b.
#Each variable value should be a number.
#If a is bigger then b, have your code print Hello World.

#a = 12
#b = 6
#if a > b:
#    print("Hello World")

# Exercise 7 : Odd Or Even
#Instructions
#Write code that asks the user for a number and determines 
#whether this number is odd or even.

#please_write = input("Enter the number: ")
#try:
    #number = int(please_write)
    #if number % 2 == 0:
       # print(f"{number} - even")
    #else:
        #print(f"{number} - odd")
#except:
    #print("Sorry, it's incorrect input. Please enter a number.")

# Exercise 8 : What’s Your Name ?
#Instructions
#Write code that asks the user for their name and determines whether or
#not you have the same name, print out a funny message based on the outcome.

#user_name = input("What's your name? ")
#my_name = "Anna"

#if user_name.lower() == my_name.lower():
    #print("Wow, we have the same names! This name is only for the cutest people!")
#else:
    #print("Nice to meet you! Although we have different names,\
#we probably have a lot in common!")


#Exercise 9 : Tall Enough To Ride A Roller Coaster
#Instructions
#Write code that will ask the user for their height in inches.
#If they are over 145cm print a message that states they are 
#tall enough to ride.
#If they are not tall enough print a message that says they need to 
#grow some more to ride.

#user_height_inches = float(input("Enter your height in inches: "))
#user_height_cm = user_height_inches * 2.54
#height_limit_cm = 145
#if user_height_cm >= height_limit_cm:
#    print("You're tall enough to ride!")
#else:
#    print("Sorry, you need to grow up a little to ride.")


#Exercises XP Gold

#Exercise 1 : Hello World-I Love Python
#Instructions
#Print the following output in one line of code:
#Hello world
#Hello world
#Hello world
#Hello world
#I love python
#I love python
#I love python
#I love python

#print('''
      #\033[92mHello\033[0m world
      #\033[92mHello\033[0m world
      #\033[92mHello\033[0m world
      #\033[92mHello\033[0m world
      #\033[92mI\033[0m love python
      #\033[92mI\033[0m love python
      #\033[92mI\033[0m love python
      #\033[92mI\033[0m love python
      #''')

#print('''
    #  Hello world
    #  Hello world
    #  Hello world
    #  Hello world
    #  I love python
    #  I love python
    #  I love python
    #  I love python
    #  ''')

#Exercise 2 : What Is The Season ?
#Instructions
#Ask the user to input a month (1 to 12).
#Display the season of the month received :
#Spring runs from March (3) to May (5)
#Summer runs from June (6) to August (8)
#Autumn runs from September (9) to November (11)
#Winter runs from December (12) to February (2)

#month = int(input("Enter a month (1 to 12): "))
#if 3 <= month <= 5:
#    season = "Spring"
#elif 6 <= month <= 8:
#    season = "Summer"
#elif 9 <= month <= 11:
#    season = "Autumn"
#elif month == 12 or 1 <= month <= 2:
#    season = "Winter"
#else:
#    season = "There is no such month. Try again - write a number from 1 to 12."

#print(season)

#Exercises XP Ninja
#Exercise 3 : Outputs
#Instructions
#Predict the output of the following code snippets:
    #>>> 3 <= 3 < 9
    #>>> 3 == 3 == 3
    #>>> bool(0)
    #>>> bool(5 == "5")
    #>>> bool(4 == 4) == bool("4" == "4")
    #>>> bool(bool(None))
    #x = (1 == True)
    #y = (1 == False)
    #a = True + 4
    #b = False + 10

    #print("x is", x)
    #print("y is", y)
    #print("a:", a)
    #print("b:", b)

#1. This checks whether 3 is greater than or equal to 3 and less than 9. 
#The result is True.
#2. This checks whether 3 is equal to 3 and 3 is equal to 3. 
#The result is True.
#3. Bool()The  function converts the integer 0 to boolean. The result is False.
#4. This checks whether 5 is equal to the string "5". The result 
#is False because the types are different.
#5. This compares two boolean values (bool(4 == 4) and bool("4" == "4")) 
#for equality. Both are True, so the result is True.
#6. The inner bool(None) evaluates to False, and then the outer bool(False) evaluates to False.
#7. x is True because 1 == True is True. y is False because 1 == False is False.
# a is 5 because True is equivalent to 1, so True + 4 is 1 + 4 which is 5.
# b is 10 because False is equivalent to 0, so False + 10 is 0 + 10 which is 10.

# Exercise 4 : How Many Characters In A Sentence ?
#Instructions
#Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).
#my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           #sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           #Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           #laboris nisi ut aliquip ex ea commodo consequat. 
           #Duis aute irure dolor in reprehenderit in voluptate velit 
           #esse cillum dolore eu fugiat nulla pariatur. 
           #Excepteur sint occaecat cupidatat non proident, 
           #sunt in culpa qui officia deserunt mollit anim id est laborum.

#my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
           #sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
           #Ut enim ad minim veniam, quis nostrud exercitation ullamco \
           #laboris nisi ut aliquip ex ea commodo consequat. \
           #Duis aute irure dolor in reprehenderit in voluptate velit \
           #esse cillum dolore eu fugiat nulla pariatur. \
           #Excepteur sint occaecat cupidatat non proident, \
           #sunt in culpa qui officia deserunt mollit anim id est laborum."
#print(len(my_text))

#Exercise 5: Longest Word Without A Specific Character
#Instructions
#Keep asking the user to input the longest sentence they can without the character “A”.
#Each time a user successfully sets a new longest sentence, print a congratulations message.

#longest_sentence = ""

#while True:
    #user_variant = input("Enter a sentence without the letter 'A': ")
    
    #if not user_variant:
        #break

    #if 'A' not in user_variant.upper():
        #if len(user_variant) > len(longest_sentence):
            #longest_sentence = user_variant
            #print("Congratulations! You have written the new longest sentence without the letter 'A'")


# Daily Challenge: Build Up A String
#Instructions
#Using the input function, ask the user for a string. The string must be 10 characters long.
#If it’s less than 10 characters, print a message which states “string not long enough”.
#If it’s more than 10 characters, print a message which states “string too long”.
#If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

#Then, print the first and last characters of the given text.

#Using a for loop, construct the string character by character: Print the first character, 
#then the second, then the third, until the full string is printed

#user_string = input("Enter a string (10 characters long): ")
#if len(user_string) < 10:
    #print("string not long enough")
#elif len(user_string) > 10:
    #print("string too long")
#else:
    #print("perfect string")

#print("First character:", user_string[0])
#print("Last character:", user_string[-1])
#print("\nConstructing the string character by character:")
#for i in range(1, len(user_string) + 1):
#    print(user_string[:i])

#Bonus: Swap some characters around then print the newly 
#jumbled string (hint: look into the shuffle method). 
# Bonus: Swap some characters around and print the newly jumbled string
    #char_list = list(user_string)
    #random.shuffle(char_list)
    #jumbled_string = ''.join(char_list)
    #print("\nJumbled string:", jumbled_string)