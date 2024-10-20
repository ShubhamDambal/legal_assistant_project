import sqlite3

# Connect to the database
conn = sqlite3.connect('legal_assistant.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a sample query to fetch tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in the database:")
for table in tables:
    print(table[0])

# Close the connection
conn.close()
