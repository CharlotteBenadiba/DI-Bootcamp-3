# Daily Challenge : Web API To DB

# Instructions
# Using this REST Countries API, create the functionality which will write 10 random 
# countries to your database.
# These are the attributes which you should populate your tables with: name, capital, 
# flag, subregion, population.

import requests
import psycopg2
from psycopg2 import sql

# Function to create a connection to the PostgreSQL database
def create_connection():
    try:
        connection = psycopg2.connect(
            user="ydpnhhtn",
            password="xKC5RZQDmkScFFsyvw7iIkPKib_Q-CO_",
            host="berry.db.elephantsql.com",
            port="5432",
            database="ydpnhhtn"
        )
        return connection
    except psycopg2.Error as e:
        print("Error: Unable to connect to the database")
        print(e)
        return None

# Function to insert country data into the database
def insert_country_data(connection, country_data):
    try:
        cursor = connection.cursor()

        insert_query = sql.SQL("""
            INSERT INTO countries (name, capital, flag, subregion, population)
            VALUES (%s, %s, %s, %s, %s)
        """)

        cursor.execute(insert_query, country_data)
        connection.commit()

        print(f"Inserted: {country_data[0]}")

    except psycopg2.Error as e:
        print("Error: Unable to insert data into the database")
        print(e)

# Fetch data from the REST Countries API
api_url = "https://restcountries.com/v3.1/all"
response = requests.get(api_url)

if response.status_code == 200:
    countries_data = response.json()

    # Connect to the PostgreSQL database
    db_connection = create_connection()

    if db_connection:
        # Insert 10 random countries into the database
        for _ in range(10):
            random_country = countries_data.pop()
            country_data = (
                random_country['name']['common'],
                random_country.get('capital', ''),
                random_country.get('flags', {}).get('png', ''), 
                random_country.get('subregion', ''),
                random_country.get('population', 0)
            )
            insert_country_data(db_connection, country_data)

        # Close the database connection
        db_connection.close()

else:
    print("Error: Unable to fetch data from the API")
    print(response.status_code)
