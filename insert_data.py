
import pysqlite3 as sqlite3


# Connect to the SQLite database
conn = sqlite3.connect('giftergenie.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Insert a new blog post
cursor.execute('''
INSERT INTO blog_posts (title, content, affiliate_link, category)
VALUES (?, ?, ?, ?)
''', ('Best Gifts for Mother\'s Day', 
      'Here are the best gifts for Mother\'s Day...', 
      'https://www.amazon.com/dp/123456789?tag=youraffiliateID', 
      'Mother\'s Day'))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Blog post added successfully!")
