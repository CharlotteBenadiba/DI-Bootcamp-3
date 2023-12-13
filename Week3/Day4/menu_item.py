# Exercise 1 : Restaurant Menu Manager
# Instructions
# Description: Create a restaurant menu management system for a manager. 
# The program should allow the manager to view the menu, add an item and delete an item.

# PART 1
# In this exercise we will use PostgreSQL and Python.
# Create a new database and a new table in pgAdmin (or in psql). The table is named 
# Menu_Items and contains the columns

# In the file menu_item.py, create a new class called MenuItem, the attributes should 
# be the name and price of each item.

# Create several methods (save, delete, update) these methods will allow a user to save, 
# delete and update items from the Menu_Items table. The update method can update the 
# name as well as the price of an item.

import psycopg2

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        try:
            connection = psycopg2.connect(
                user="ydpnhhtn",
                password="xKC5RZQDmkScFFsyvw7iIkPKib_Q-CO_",
                host="berry.db.elephantsql.com",
                port="5432",
                database="restaurant"
            )
            cursor = connection.cursor()

            # Inserting the item into the Menu_Items table
            cursor.execute("INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
                           (self.name, self.price))
            connection.commit()

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

        finally:
            if connection:
                cursor.close()
                connection.close()

    def delete(self):
        try:
            connection = psycopg2.connect(
                user="ydpnhhtn",
                password="xKC5RZQDmkScFFsyvw7iIkPKib_Q-CO_",
                host="berry.db.elephantsql.com",
                port="5432",
                database="restaurant"
            )
            cursor = connection.cursor()

            # Deleting the item from the Menu_Items table
            cursor.execute("DELETE FROM Menu_Items WHERE item_name = %s", (self.name,))
            connection.commit()

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

        finally:
            if connection:
                cursor.close()
                connection.close()

    def update(self, new_name, new_price):
        try:
            connection = psycopg2.connect(
                user="ydpnhhtn",
                password="xKC5RZQDmkScFFsyvw7iIkPKib_Q-CO_",
                host="berry.db.elephantsql.com",
                port="5432",
                database="restaurant"
            )
            cursor = connection.cursor()

            # Updating the item in the Menu_Items table
            cursor.execute("UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s",
                           (new_name, new_price, self.name))
            connection.commit()

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

        finally:
            if connection:
                cursor.close()
                connection.close()



