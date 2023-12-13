# In the file menu_manager.py, create a new class called MenuManager
# Create a Class Method called get_by_name that will return a single item from the 
# Menu_Items table depending on it’s name, if an object is not found (there is no 
# item matching the name in the get_by_name method) return None.

# Create a Class Method called all_items which will return a list of all the items from 
# the Menu_Items table.

import psycopg2
from menu_item import MenuItem 

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        try:
            connection = psycopg2.connect(
                user="ydpnhhtn",
                password="xKC5RZQDmkScFFsyvw7iIkPKib_Q-CO_",
                host="berry.db.elephantsql.com",
                port="5432",
                database="restaurant"
            )
            cursor = connection.cursor()

            # Retrieving an item by name from the Menu_Items table
            cursor.execute("SELECT * FROM Menu_Items WHERE item_name = %s", (name,))
            result = cursor.fetchone()

            if result:
                item = MenuItem(result[1], result[2])
                return item
            else:
                return None

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

        finally:
            if connection:
                cursor.close()
                connection.close()

    @classmethod
    def all(cls):
        try:
            connection = psycopg2.connect(
                user="ydpnhhtn",
                password="xKC5RZQDmkScFFsyvw7iIkPKib_Q-CO_",
                host="berry.db.elephantsql.com",
                port="5432",
                database="restaurant"
            )
            cursor = connection.cursor()

            # Retrieving all items from the Menu_Items table
            cursor.execute("SELECT * FROM Menu_Items")
            results = cursor.fetchall()

            items = [MenuItem(result[1], result[2]) for result in results]
            return items

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

        finally:
            if connection:
                cursor.close()
                connection.close()

# item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
# item2 = MenuManager.get_by_name('Beef Stew')
# items = MenuManager.all()