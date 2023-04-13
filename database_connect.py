# make database sqlite3 and connect python to sqlite3 database using the ‘db-sqlite3‘ module.
import csv
import sqlite3

path_db_ = './feature_home.db'

def get_connection(path_db):
    return sqlite3.connect(path_db)

def get_curser():
    connection = get_connection(path_db_)
    return connection.cursor()



def insert_data(number_bedrooms, number_bath, area, property_address, price):
    connection = sqlite3.connect('./feature_home.db')
    curser = connection.cursor()
    curser.execute("INSERT INTO feature_home VALUES (?,?,?,?,?)", (number_bedrooms, number_bath, area, property_address, price))
    connection.commit()
    connection.close()


def select_all_records():
    cursor = get_curser()
    sql = "SELECT * FROM feature_home"
    cursor.execute(sql)
    print(cursor.fetchall())  # or use fetchone()
    print("\nHere is a listing of the rows in the table\n")
    for row in cursor.execute("SELECT * FROM feature_home"):
        print(row)
        

def export_database_to_csv_file():
    cursor = get_curser()
    cursor.execute("select * from feature_home")
    with open("data.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter="\t")
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)

    
        
curser = get_curser()
print('DB Init')

#   CREATE TABLE
sql = """
    CREATE TABLE IF NOT EXISTS feature_home(
        number_bedrooms INTEGER ,
        number_bath INTEGER,
        area VARCHAR (15),
        property_address VARCHAR (100), 
        price VARCHAR (60)
    );
    """
curser.execute(sql)

# connection.commit()
# connection.close()

# show all data in table feature home
select_all_records()


export_database_to_csv_file()

