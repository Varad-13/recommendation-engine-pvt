import sqlite3
import random
import sys
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Fetch all users
cursor.execute("SELECT * FROM core_userprofile")
users = cursor.fetchall()

# Fetch all posts
cursor.execute("SELECT * FROM core_post")
posts = cursor.fetchall()

# Get the number of interactions from command line arguments
if len(sys.argv) > 1:
    num_interactions = int(sys.argv[1])
else:
    num_interactions = 100

# Generate random interactions
for _ in range(num_interactions):
    for user in users:
        post = random.choice(posts)
        action = "click"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Insert the interaction into the database
        cursor.execute("INSERT INTO core_interaction (user_id, post_id, action, timestamp) VALUES (?, ?, ?, ?)", (user[0], post[0], action,timestamp))
        cursor.execute("INSERT INTO core_logs (user_id, post_id, action, timestamp) VALUES (?, ?, ?, ?)", (user[0], post[0], action,timestamp))
# Commit the changes and close the database connection
conn.commit()
conn.close()

print(f"Generated {num_interactions} random interactions.")
