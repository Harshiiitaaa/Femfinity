import mysql.connector

# Establish a connection to the MySQL server
conn = mysql.connector.connect(
    host="localhost",         # Replace with your MySQL host
    user="root",     # Replace with your MySQL username
    password="root"  # Replace with your MySQL password
)

cursor = conn.cursor()

# Create the database 'femfinity' if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS femfinity")
print("Database 'femfinity' created successfully or already exists!")

# Connect to the 'femfinity' database
conn.database = "femfinity"

# Create the Users table in the 'femfinity' database
create_table_query = """
CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Auto-incrementing ID
    full_name VARCHAR(255) NOT NULL,        -- Full name of the user
    email_id VARCHAR(255) NOT NULL UNIQUE,  -- Email ID (unique)
    password VARCHAR(255) NOT NULL          -- Password
);
"""

cursor.execute(create_table_query)
print("Users table created successfully in the 'femfinity' database!")

# Close the connection
cursor.close()
conn.close()
