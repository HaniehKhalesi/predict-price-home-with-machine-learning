# make database sqlite3 and connect python to sqlite3 database using the ‘db-sqlite3‘ module.

import sqlite3


def insert_data(number_bedrooms, number_bath, area, property_address, price):
    connection = sqlite3.connect('./feature_home.db')
    curser = connection.cursor()
    curser.execute("INSERT INTO feature_home VALUES (?,?,?,?,?)", (number_bedrooms, number_bath, area, property_address, price))
    connection.commit()
    connection.close()


connection = sqlite3.connect('./feature_home.db')
curser = connection.cursor()
print('DB Init')

#   CREATE TABLE
sql = """
    CREATE TABLE IF NOT EXISTS feature_home(
        Number_bedrooms INTEGER ,
        number_bath INTEGER,
        area VARCHAR (15),
        property_address VARCHAR (100), 
        price VARCHAR (60)
    );
    """
curser.execute(sql)

# connection.commit()
# connection.close()

