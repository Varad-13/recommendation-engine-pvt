import sqlite3
import pandas as pd

# Load the dataset from the CSV file
df = pd.read_csv('cleaned_dataset.csv')

# Initialize an empty set to store distinct skills
distinct_skills = set()

# Extract distinct skills from the "skills" column
for skills in df['skills']:
    if isinstance(skills, str):
        skills_list = skills.split(', ')
        distinct_skills.update(skills_list)

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Create the "core_tag" table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS core_tag (
        tagid INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        tag TEXT
    )
''')

# Prepare the data for bulk insert
data_to_insert = [('RandomCategory', skill) for skill in distinct_skills]

# Use executemany to bulk insert the distinct skills
cursor.executemany('INSERT INTO core_tag (category, tag) VALUES (?, ?)', data_to_insert)

# Commit the changes and close the database connection
conn.commit()
conn.close()
