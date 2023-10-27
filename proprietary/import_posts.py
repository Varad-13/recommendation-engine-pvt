import csv
import sqlite3
from datetime import datetime
import random
from slugify import slugify

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("DELETE from core_post_tag")
cursor.execute("DELETE from core_post")
with open('cleaned_dataset.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data_to_insert = []

    for row in csv_reader:
        title = row['title']
        description = row['description']
        skills = row['skills'].split(', ')
        fixed_price = int(row['fixed_price'].replace('$', '').replace(',', ''))
        link = slugify(title).replace(' ', '-')
        freelancer = int(random.randint(1, 7))

        # Insert into core_post
        cursor.execute("INSERT INTO core_post (name, description, freelancer_id, link, amount, images) VALUES (?, ?, ?, ?, ?, ?)",
                       (title, description, freelancer, link, fixed_price, None))
        post_id = cursor.lastrowid

        cursor.execute("SELECT id FROM core_tag")
        tag_ids = cursor.fetchall()
        
        for tag_id in tag_ids:
            cursor.execute("INSERT INTO core_post_tag (post_id, tag_id, score) VALUES (?, ?, ?)",
                           (post_id, tag_id[0], 0))

        tag_ids = []
        for skill in skills:
            cursor.execute("SELECT id FROM core_tag WHERE tag = ?", (skill,))
            result = cursor.fetchone()
            if result:
                tag_id = result[0]
                tag_ids.append(tag_id)

        # Insert into core_post_tag
        for skill in tag_ids:
            cursor.execute("UPDATE core_post_tag SET score = 10 WHERE post_id = ? AND tag_id = ?",
                           (post_id, skill))

# Commit changes and close the database connection
conn.commit()
conn.close()
