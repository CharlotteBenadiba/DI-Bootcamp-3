# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores 
# the indexes of each letter in a list.
# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
# Examples
# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }
# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }
# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}

# word = input("Enter a word: ")
# letter_indexes = {}

#for index, letter in enumerate(word):
#    letter = letter.lower()

#    if letter in letter_indexes:
#        letter_indexes[letter].append(index)
#    else:
#        letter_indexes[letter] = [index]

# print(letter_indexes)


# Challenge 2
# Create a program that prints a list of the items you can afford in the 
# store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Examples
# The key is the product, the value is the price
# items_purchase = {
#  "Water": "$1",
#  "Bread": "$3",
#  "TV": "$1,000",
#  "Fertilizer": "$20"
#}
# wallet = "$300"
# ➞ ["Bread", "Fertilizer", "Water"]
# items_purchase = {
#  "Apple": "$4",
#  "Honey": "$3",
#  "Fan": "$14",
#  "Bananas": "$4",
#  "Pan": "$100",
#  "Spoon": "$2"
#}

# wallet = "$100" 
#➞ ["Apple", "Bananas", "Fan", "Honey", "Spoon"]
# items_purchase = {
#  "Phone": "$999",
#  "Speakers": "$300",
#  "Laptop": "$5,000",
#  "PC": "$1200"
#}
# wallet = "$1" 
# ➞ "Nothing"

# Example 1
# items_purchase1 = {
#    "Water": "$1",
#    "Bread": "$3",
#    "TV": "$1,000",
#    "Fertilizer": "$20"
#}
# wallet1 = "$300"

# wallet_amount1 = int(wallet1[1:])
# affordable_items_list1 = []

#for item, price in sorted(items_purchase1.items()):
#    item_price = int(price[1:].replace(",", ""))
#    if item_price <= wallet_amount1:
#        affordable_items_list1.append(item)
#        wallet_amount1 -= item_price

# result1 = sorted(affordable_items_list1) if affordable_items_list1 else "Nothing"
# print(result1)

# Example 2
#items_purchase2 = {
#    "Apple": "$4",
#    "Honey": "$3",
#    "Fan": "$14",
#    "Bananas": "$4",
#    "Pan": "$100",
#    "Spoon": "$2"
#}
# wallet2 = "$100"

# wallet_amount2 = int(wallet2[1:])
# affordable_items_list2 = []

#for item, price in sorted(items_purchase2.items()):
#    item_price = int(price[1:].replace(",", ""))
#    if item_price <= wallet_amount2:
#        affordable_items_list2.append(item)
#        wallet_amount2 -= item_price

#result2 = sorted(affordable_items_list2) if affordable_items_list2 else "Nothing"
#print(result2)

# Example 3
#items_purchase3 = {
#    "Phone": "$999",
#    "Speakers": "$300",
#    "Laptop": "$5,000",
#    "PC": "$1200"
#}
#wallet3 = "$1"

#wallet_amount3 = int(wallet3[1:])
#affordable_items_list3 = []

#for item, price in sorted(items_purchase3.items()):
#    item_price = int(price[1:].replace(",", ""))
#    if item_price <= wallet_amount3:
#        affordable_items_list3.append(item)
#        wallet_amount3 -= item_price

#result3 = sorted(affordable_items_list3) if affordable_items_list3 else "Nothing"
#print(result3)
