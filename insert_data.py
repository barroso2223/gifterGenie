import pysqlite3 as sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect('giftergenie.db')
cursor = conn.cursor()

# Drop the table if it exists (this is to fix schema issues)
cursor.execute('DROP TABLE IF EXISTS blog_posts')

# Create the blog_posts table with the new column (date)
cursor.execute('''
CREATE TABLE blog_posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT NOT NULL,
    affiliate_link TEXT,
    category TEXT,
    date TEXT NOT NULL
)
''')

# Insert blog posts into the table with the current date
def insert_blog_post(title, content, affiliate_link, category):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get current date and time
    cursor.execute('''
    INSERT INTO blog_posts (title, content, affiliate_link, category, date) 
    VALUES (?, ?, ?, ?, ?)
    ''', (title, content, affiliate_link, category, date))
    conn.commit()
    print(f"Blog post '{title}' added successfully!")

# Example blog posts using the function
insert_blog_post("Best Gifts for Mother's Day", 
                 "Here are the best gifts for Mother's Day...", 
                 "https://www.amazon.com/dp/123456789?tag=youraffiliateID", 
                 "Mother's Day")

insert_blog_post("Gift Ideas for Christmas", 
                 "Explore the best Christmas gift ideas...", 
                 "https://www.amazon.com/dp/987654321?tag=youraffiliateID", 
                 "Christmas")

# Commit the changes and close the connection
conn.close()

print("All blog posts inserted successfully!")

