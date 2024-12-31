import pysqlite3 as sqlite3

# Connect to the database
conn = sqlite3.connect('giftergenie.db')
cursor = conn.cursor()

# Query to retrieve all blog posts
cursor.execute("SELECT * FROM blog_posts")

# Fetch all results
blog_posts = cursor.fetchall()

# Close the connection
conn.close()

# Display the blog posts
for post in blog_posts:
    print(f"Title: {post[0]}")
    print(f"Content: {post[1]}")
    print(f"Date: {post[2]}")
    print("-" * 50)
