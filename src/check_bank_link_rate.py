import sqlite3

conn = sqlite3.connect("data/fintech.db")
cursor = conn.cursor()

cursor.execute("""
SELECT 
    COUNT(*) as total_users,
    SUM(link_success) as successful_links
FROM bank_links
""")

total_users, successful_links = cursor.fetchone()

print("Total users:", total_users)
print("Successful bank links:", successful_links)
print("Bank link rate:", successful_links / total_users)

conn.close()

