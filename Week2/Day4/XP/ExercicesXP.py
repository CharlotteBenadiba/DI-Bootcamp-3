# Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.
# Hint : The generated sentences do not have to make sense.

# Download this word list
# Save it in your development directory.
# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.
# Create a function called main which will:
# Print a message explaining what the program does.
# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

# import random
# import os

#def write_words_to_file(file_path, words):
#    with open(file_path, 'w') as file:
#        for word in words:
#            file.write(word + '\n')

#def get_words_from_file(file_path):
#    if not os.path.exists(file_path):
#        return []  

#    with open(file_path, 'r') as file:
#        words = file.read().splitlines()
#    return words

#def get_random_sentence(length, words):
#    if length < 2 or length > 20:
#        raise ValueError("Sentence length should be between 2 and 20.")
    
#    random_words = random.sample(words, length)
#    sentence = ' '.join(random_words).lower()
#    return sentence

#def main():
#    print("Welcome to the Random Sentence Generator!")
#    print("This program will generate a random sentence based on the provided word list.")

#    dir_path = os.path.dirname(os.path.realpath(__file__))
#    file_path = os.path.join(dir_path, 'sowpods.txt')

#    initial_words = ["apple", "banana", "cherry", "elderberry", "fig"]

#    if not os.path.exists(file_path):
#        write_words_to_file(file_path, initial_words)

#    words = get_words_from_file(file_path)

#    try:
#        sentence_length = int(input("How long do you want the sentence to be? (Enter a number between 2 and 20): "))
#        if 2 <= sentence_length <= 20:
#            result_sentence = get_random_sentence(sentence_length, words)
#            print(f"Generated Sentence: {result_sentence}")
#        else:
#            print("Error: Sentence length should be between 2 and 20.")
#    except ValueError:
#        print("Error: Please enter a valid integer for the sentence length.")

#if __name__ == "__main__":
#    main()


# Exercise 2: Working With JSON
# Instructions
# import json
# sampleJson = """{ 
#   "company":{ 
#      "employee":{ 
#         "name":"emma",
#         "payable":{ 
#            "salary":7000,
#            "bonus":800
#         }
#      }
#   }
#}"""

# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.

# import json

#sampleJson = """{ 
#   "company":{ 
#      "employee":{ 
#         "name":"emma",
#         "payable":{ 
#            "salary":7000,
#            "bonus":800
#         }
#      }
#   }
#}"""

# data = json.loads(sampleJson)
# salary_value = data["company"]["employee"]["payable"]["salary"]
# print("Salary:", salary_value)
# data["company"]["employee"]["birth_date"] = "1990-01-01"

#with open("output.json", "w") as json_file:
#    json.dump(data, json_file, indent=4)




