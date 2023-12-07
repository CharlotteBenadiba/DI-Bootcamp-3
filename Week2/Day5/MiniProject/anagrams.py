import os

#print("Current working directory:", os.getcwd())

from anagram_checker import AnagramChecker

def get_user_input():
    return input("Enter a word (type 'exit' to quit): ").strip()

def validate_input(word):
    if len(word.split()) > 1:
        print("Error: Only a single word is allowed.")
        return False
    elif not word.isalpha():
        print("Error: Only alphabetic characters are allowed.")
        return False
    else:
        return True

def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    word_list_path = os.path.join(script_directory, "sowpods.txt")
    
    checker = AnagramChecker(word_list_path)

    while True:
        user_input = get_user_input()

        if user_input.lower() == 'exit':
            break

        user_input = user_input.strip()

        if validate_input(user_input):
            if checker.is_valid_word(user_input):
                anagrams = checker.get_anagrams(user_input)
                print(f"\nYOUR WORD: \"{user_input.upper()}\"\nThis is a valid English word.")
                if anagrams:
                    anagram_str = ', '.join(anagrams)
                    print(f"Anagrams for your word: {anagram_str}.")
                else:
                    print("No anagrams found for your word.")
            else:
                print(f"\nYOUR WORD: \"{user_input.upper()}\"\nThis is not a valid English word.")
        print("\n" + "-" * 40)

if __name__ == "__main__":
    main()