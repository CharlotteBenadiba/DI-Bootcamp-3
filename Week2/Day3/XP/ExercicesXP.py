#  Exercise 1: Currencies
# Instructions
#class Currency:
#    def __init__(self, currency, amount):
#        self.currency = currency
#        self.amount = amount

    #Your code starts HERE

# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c3 = Currency('shekel', 1)
# >>> c4 = Currency('shekel', 10)

# >>> str(c1)
# '5 dollars'

# >>> int(c1)
# 5

# >>> repr(c1)
# '5 dollars'

# >>> c1 + 5
# 10

# >>> c1 + c2
# 15

# >>> c1 
# 5 dollars

# >>> c1 += 5
# >>> c1
# 10 dollars

# >>> c1 += c2
# >>> c1
# 20 dollars

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>

#class Currency:
#    def __init__(self, currency, amount):
#        self.currency = currency
#        self.amount = amount

#    def __str__(self):
#        return f'{self.amount} {self.currency}s'

#    def __int__(self):
#        return self.amount

#    def __repr__(self):
#        return f'{self.amount} {self.currency}s'

#    def __add__(self, other):
#        if isinstance(other, (int, float)):
#            return Currency(self.currency, self.amount + other)
#        elif isinstance(other, Currency):
#            if self.currency == other.currency:
#                return Currency(self.currency, self.amount + other.amount)
#            else:
#                raise TypeError(f'Cannot add between Currency type <{self.currency}> and <{other.currency}>')

#    def __iadd__(self, other):
#        if isinstance(other, (int, float)):
#            self.amount += other
#        elif isinstance(other, Currency):
#            if self.currency == other.currency:
#                self.amount += other.amount
#            else:
#                raise TypeError(f'Cannot add between Currency type <{self.currency}> and <{other.currency}>')
#        return self

# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)

# print(str(c1))  
# print(int(c1))   
# print(repr(c1))   
# print(c1 + 5)     
# print(c1 + c2)    
# print(c1)        
# c1 += 5
# print(c1)        
# c1 += c2
# print(c1)        
# print(c1 + c3) # will raise a TypeError


# Exercise 3: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

# import string
# import random

#def generate_random_string(length=5):
#    letters = string.ascii_letters 
#    return ''.join(random.choice(letters) for _ in range(length))

# random_string = generate_random_string()
# print(random_string)



# Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.


# from datetime import datetime

#def display_current_date():
#    current_date = datetime.now().date()
#    print("Current Date:", current_date)

# display_current_date()


# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

# from datetime import datetime, timedelta

#def time_until_january_1st():
#    current_date = datetime.now()
#    january_1st = datetime(current_date.year + 1, 1, 1) 
#    time_remaining = january_1st - current_date
#    days = time_remaining.days
#    hours, remainder = divmod(time_remaining.seconds, 3600)
#    minutes, seconds = divmod(remainder, 60)

#    print(f"The 1st of January is in {days} days and {hours:02}:{minutes:02}:{seconds:02} hours.")
# time_until_january_1st()


# Exercise 6 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice),
# then displays a message stating how many minutes the user lived in his life.

# from datetime import datetime

#def minutes_lived(birthdate):
#    birthdate_object = datetime.strptime(birthdate, "%Y-%m-%d") 
#    current_date = datetime.now()
#    time_lived = current_date - birthdate_object
#    minutes_lived = int(time_lived.total_seconds() / 60)
#    print(f"You have lived for {minutes_lived} minutes.")

# birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
# minutes_lived(birthdate_input)


# Exercise 7 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to 
# properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the
# following keys: name, adress, langage_code. Use faker to populate them with fake data.

# from faker import Faker

# fake = Faker()
# users = []

#def add_user():
#    user = {
#        'name': fake.name(),
#        'address': fake.address(),
#        'language_code': fake.language_code(),
#    }
#    users.append(user)

#for _ in range(5):
#    add_user()

#for user in users:
#    print(user)


