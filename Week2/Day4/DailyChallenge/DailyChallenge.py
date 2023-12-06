# Daily Challenge : Text Analysis
# Instructions :
# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.

# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.

# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

# Implement a classmethod that returns a Text instance but with a text file:

#    >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.

# Now, use the provided the_stranger.txt file and try using the class you created above.

# Bonus:
# Create a class called TextModification that inherits from Text.

# Implement the following methods:
# a method that returns the text without any punctuation.
# a method that returns the text without any english stop-words (check out what this is !!).
# a method that returns the text without any special characters.
# Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)

# import string
# import requests
# from collections import Counter
# import os

#class Text:
#    def __init__(self, text):
#        self.text = text

#    def word_frequency(self, word):
#        words = self.text.lower().split()
#        return words.count(word.lower())

#    def most_common_word(self):
#        words = self.text.lower().split()
#        return max(set(words), key=words.count)

#    def unique_words(self):
#        return list(set(self.text.lower().split()))

#    @classmethod
#    def from_file(cls, file_url):
#        response = requests.get(file_url)
#        if response.status_code == 200:
#            return cls(response.text)
#        else:
#            raise FileNotFoundError(f"File not found at URL: {file_url}")

#class TextModification(Text):
#    def remove_punctuation(self):
#        translator = str.maketrans("", "", string.punctuation)
#        return self.text.translate(translator)

#    def remove_stop_words(self):
#        stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",
#                      "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself',
#                      'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them',
#                      'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll",
#                      'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
#                      'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because',
#                      'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
#                      'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out',
#                      'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where',
#                      'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no',
#                      'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just',
#                      'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren',
#                      "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn',
#                      "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't",
#                      'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't",
#                      'won', "won't", 'wouldn', "wouldn't"]
#        words = self.text.lower().split()
#        return ' '.join([word for word in words if word not in stop_words])

#    def remove_special_characters(self):
#        return ''.join(char for char in self.text if char.isalnum() or char.isspace())

# file_url = 'https://raw.githubusercontent.com/devtlv/theStranger_text_W5D4PY/master/the_stranger.txt'
# text_part_i = Text("A good book would sometimes cost as much as a good house.")
# text_part_ii = Text.from_file(file_url)

# print("Part I:")
# print("Frequency of word 'good':", text_part_i.word_frequency("good"))
# print("Most common word:", text_part_i.most_common_word())
# print("Unique words:", text_part_i.unique_words())

# print("\nPart II:")
# print("Frequency of word 'stranger':", text_part_ii.word_frequency("stranger"))
# print("Most common word:", text_part_ii.most_common_word())
# print("Unique words:", text_part_ii.unique_words())

# text_modification = TextModification("Hello, this is an example sentence!")

# print("\nText Modification:")
# print("Remove Punctuation:", text_modification.remove_punctuation())
# print("Remove Stop Words:", text_modification.remove_stop_words())
# print("Remove Special Characters:", text_modification.remove_special_characters())
