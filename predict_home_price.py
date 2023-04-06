# make database sqlite3 and connect python to sqlite3 database using the ‘db-sqlite3‘ module.

import sqlite3


def insert_data(number_badrom, number_bath, area, property_address, price):
    connection = sqlite3.connect('./feature_home.db')
    curser = connection.cursor()
    curser.execute("INSERT INTO feature_home VALUE (?,?,?,?,?)", (number_badrom, number_bath, area, property_address, price))
    connection.commit()
    connection.close()


connection = sqlite3.connect('./feature_home.db')
curser = connection.cursor()
print('DB Init')

#   CREATE TABLE
sql = """
    CREATE TABLE IF NOT EXISTS feature_home(
        number_badrom INTEGER ,
        number_bath (60),
        area VARCHAR (60),
        property_address INTEGER 
        price INTEGER
    );
    """
curser.execute(sql)

# connection.commit()
# connection.close()


    