# Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dict = dict(zip(keys, values))
# print(dict)

# Exercise 2 : Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Given the following object:
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# How much does each family member have to pay ?
# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the 
# provided family variable (Hint: ask the user for names and ages and 
# add them into a family dictionary that is initially empty).

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# total_cost = 0
#for name, age in family.items():
#    if age < 3:
#        cost = 0  
#    elif 3 <= age <= 12:
#        cost = 10 
#    else:
#        cost = 15

#    total_cost += cost
#    print(f"{name}'s ticket cost: ${cost}")

#print(f"Total cost for the family: ${total_cost}")

# Bonus
# family = {}

# while True:
#    name = input("Enter a name (or write 'quit' to finish): ")
#  
#    if name.lower() == 'quit':
#        break
#
#    age = int(input(f"Enter {name}'s age: "))
#    family[name] = age

# total_cost = 0
#for name, age in family.items():
#    if age < 3:
#        cost = 0  
#    elif 3 <= age <= 12:
#        cost = 10  
#    else:
#        cost = 15 

#    total_cost += cost
#    print(f"{name}'s ticket cost: ${cost}")

# print(f"Total cost for the family: ${total_cost}")

# Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#    France: blue, 
#    Spain: red, 
#    US: pink, green

#  Create a dictionary called brand which value is the information from 
# part one (turn the info into keys and values).
# The values type_of_clothes and international_competitors should be a list. 
# The value of major_color should be a dictionary.
# Change the number of stores to 2.
# Print a sentence that explains who Zaras clients are.
# Add a key called country_creation with a value of Spain.
# Check if the key international_competitors is in the dictionary. If it is, 
# add the store Desigual.
# Delete the information about the date of creation.
# Print the last international competitor.
# Print the major clothes colors in the US.
# Print the amount of key value pairs (ie. length of the dictionary).
# Print the keys of the dictionary.
# Create another dictionary called more_on_zara with the following details:
# creation_date: 1975 
# number_stores: 10 000
# Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# Print the value of the key number_stores. What just happened ?

# brand = {
#    "name": "Zara",
#    "creation_date": 1975,
#    "creator_name": "Amancio Ortega Gaona",
#    "type_of_clothes": ["men", "women", "children", "home"],
#    "international_competitors": ["Gap", "H&M", "Benetton"],
#    "number_stores": 7000,
#    "major_color": {
#        "France": "blue",
#        "Spain": "red",
#        "US": {"first": "pink", "second": "green"}
#    }
#}

# Step 3
# brand["number_stores"] = 2

# Step 4
# print("Zara's clients are men, women, children, and home decorators.")

# Step 5
# brand["country_creation"] = "Spain"

# Step 6
# if "international_competitors" in brand:
#    brand["international_competitors"].append("Desigual")

# Step 7
# del brand["creation_date"]

# Step 8
# print(f"The last international competitor is {brand['international_competitors'][-1]}.")

# Step 9
# print(f"The major clothes colors in the US are {brand['major_color']['US']['first']} and {brand['major_color']['US']['second']}.")

# Step 10
# print(f"The number of key-value pairs in the dictionary is {len(brand)}.")

# Step 11
# print(f"The keys of the dictionary are {list(brand.keys())}.")

# Step 12
# more_on_zara = {
#    "creation_date": 1975,
#    "number_stores": 10000
#}

# Step 13
# brand.update(more_on_zara)

# Step 14
# print(f"The updated value of number_stores is {brand['number_stores']}.")

# Exercise 4 : Disney Characters
# Instructions
# Use this list :
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :
#1/
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
#2/
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
#3/ 
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.

# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. 
# disney_users_A = {}
#for index, user in enumerate(users):
#    disney_users_A[user] = index
#print("Result #1:", disney_users_A)

# 2.
# disney_users_B = {}
#for index, user in enumerate(users):
#    disney_users_B[index] = user
#print("Result #2:", disney_users_B)

# 3.
# disney_users_C = dict(enumerate(sorted(users)))
# print("Result #3:", disney_users_C)

# 4-1.
# disney_users_i = {}
# for index, user in enumerate(users):
#    if 'i' in user.lower():
#        disney_users_i[user] = index
#print("Result for 'i':", disney_users_i)

# 4-2.
#disney_users_m_p = {}
#for index, user in enumerate(users):
#    if user[0].lower() in ['m', 'p']:
#        disney_users_m_p[user] = index
#print("Result for 'm' or 'p':", disney_users_m_p)

