# make database sqlite3 and connect python to sqlite3 database using the ‘db-sqlite3‘ module.
import csv
import sqlite3


def insert_data(number_bedrooms, number_bath, area, property_address, price):
    connection = sqlite3.connect('./feature_home.db')
    curser = connection.cursor()
    curser.execute("INSERT INTO feature_home VALUES (?,?,?,?,?)", (number_bedrooms, number_bath, area, property_address, price))
    connection.commit()
    connection.close()


def select_all_records(cursor):
    sql = "SELECT * FROM feature_home"
    cursor.execute(sql)
    print(cursor.fetchall())  # or use fetchone()
    print("\nHere is a listing of the rows in the table\n")
    for row in cursor.execute("SELECT * FROM feature_home"):
        print(row)
        

def export_database_to_csv_file(file_name, data):       
    try:
        with open(file_name, 'w', newline='')as f:
            writer = csv.writer(f)
            writer.writerow([
                'Number_bedrooms',
                'number_bath',
                'area',
                'property_address',
                'price'
            ])
            writer.writerow(data)
            print("export database to csv file successful ...")
    except:
        print("can not export database to csv file ...")
    
        
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

# show all data in table feature home
select_all_records(curser)

# export all data table feature home to 
data = curser.execute("SELECT * FROM feature_home")
export_database_to_csv_file('output_data_feature_home.csv', data)
