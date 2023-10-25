import csv
import sqlite3

# Open a connection to the SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Create the core_tag table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS core_tag (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tag TEXT,
        category TEXT
    )
''')

# Read data from the CSV file and insert it into the table
with open('tags.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        tag = row['Tag']
        category = row['Category']
        cursor.execute("INSERT INTO core_tag (tag, category) VALUES (?, ?)", (tag, category))

# Commit the changes and close the database connection
conn.commit()
conn.close()
