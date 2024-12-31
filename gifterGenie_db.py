
import pysqlite3 as sqlite3


# Connect to SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('giftergenie.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table to store blog posts
cursor.execute('''
CREATE TABLE IF NOT EXISTS blog_posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    affiliate_link TEXT,
    category TEXT
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")
