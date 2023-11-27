# Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable 
# called our_fav_numbers.

# my_fav_numbers = set([8, 18, 88, 108])
# my_fav_numbers.add(77)
# my_fav_numbers.add(13)
# my_fav_numbers.remove(108)
# friend_fav_numbers = {5, 7, 17, 99}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more 
# integers to the tuple?

# No, it is not possible to add more integers to the tuple. 
# If you need to work with a data structure that allows dynamic changes 
# to its elements, you might want to use a list instead of a tuple. 

# Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# print(basket.count("Apples"))
# basket.clear()
# print(basket)

# Exercise 4: Floats
#Instructions
# Recap – What is a float? What is the difference between an 
# integer and a float?
# Create a list containing the following sequence 
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# Can you think of another way to generate a sequence of floats?

# A float is a data type in Python that represents decimal numbers 
# or floating-point numbers. Floats are used to represent real numbers, 
# and they can include a fractional part.

# The difference between an integer and a float lies in the 
# representation of numbers. Integers are whole numbers without 
# any decimal point, while floats can represent numbers with a decimal point.
# list_a = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 ]
# list_b = [i / 2 for i in range(3, 11)]
# print(list_a)
# print(list_b)

# Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out 
# every element which has an even index.

#for number in range(1, 21):
#    print(number)

# print("---")

# for number in range(1, 21):
#    if number % 2 == 0:
#        print(number)

#  Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user 
# for their name, unless the input is equal to your name.

# my_name = "Anna"
#while True:
#    user_name = input("Enter your name: ")

#    if user_name == my_name:
#        break 
#    else:
#        print("Please enter your name again")

# Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the 
# fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words 
# into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose 
# one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. 
# I hope you enjoy”.

# favorite_fruits = input("Enter your favorite fruit(s) separated by a single space: ")
# favorite_fruits_list = favorite_fruits.split()
# chosen_fruit = input("Enter a name of any fruit: ")

#if chosen_fruit in favorite_fruits_list:
#    print("You chose one of your favorite fruits! Enjoy!")
#else:
#    print("You chose a new fruit. I hope you enjoy.")

# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, 
# when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping 
# to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what 
# the total price is (10 + 2.5 for each topping).

#pizza_toppings = []
#base_price = 10.0
#topping_price = 2.5

#while True:
#    topping = input("Enter a pizza topping (or 'quit' to finish): ")
   
#    if topping.lower() == 'quit':
#        break  
    
#    pizza_toppings.append(topping)
    
#    print(f"Adding {topping} to your pizza.")

#total_price = base_price + len(pizza_toppings) * topping_price
#print("Toppings on your pizza:", pizza_toppings)
#print(f"Total price of your pizza: ${total_price}")

# Exercise 10 : Sandwich Orders
# Instructions
# Using the list below :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich

#sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

#while "Pastrami sandwich" in sandwich_orders:
#    sandwich_orders.remove("Pastrami sandwich")

#finished_sandwiches = []

#while sandwich_orders:
#    current_sandwich = sandwich_orders.pop(0)
#    finished_sandwiches.append(current_sandwich)
#    print(f"I made your {current_sandwich.lower()}")

#print("\nList of sandwiches that were made:")
#for sandwich in finished_sandwiches:
#    print(f"I made your {sandwich.lower()}")