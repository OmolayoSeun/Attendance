import sqlite3

# Establish connection to the database
connection = sqlite3.connect('my_database.db')

# Create cursor object
cursor = connection.cursor()

# Table name and column name to fetch data from
table_name = 'my_table'
column_name = 'my_column'

# Specific value to filter data
filter_value = 'my_value'

# Construct SQL query to fetch data
query = f"SELECT {column_name} FROM {table_name} WHERE {column_name} = '{filter_value}';"

# Execute the query
cursor.execute(query)

# Fetch results
results = cursor.fetchall()

# Check if results are empty
if not results:
    print(f"No data found for '{column_name}' with value '{filter_value}'.")
else:
    for row in results:
        print(row[0])  # Print the first column of the fetched data

# Close connection to the database
connection.close()
