import sqlite3
import pandas as pd

# 1. CONNECT to the database (Creates 'shop.db' file)
conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

# PRO TIP: Reset the table so we don't get duplicate data if we run this twice
cursor.execute('DROP TABLE IF EXISTS sales')

# 2. CREATE A TABLE (The "Filing Cabinet")
cursor.execute('''
    CREATE TABLE sales (
        id INTEGER PRIMARY KEY,
        item_name TEXT,
        price REAL,
        quantity INTEGER
    )
''')

# 3. INSERT DATA (Stuffing the cabinet)
# We are inserting: Name, Price, Quantity Sold
sample_data = [
    ('Coffee', 4.00, 100),   # 4.00 * 100 = $400 Revenue
    ('Muffin', 3.50, 50),    # 3.50 * 50  = $175 Revenue
    ('Latte', 5.50, 80),     # 5.50 * 80  = $440 Revenue
    ('Water', 2.00, 30)      # 2.00 * 30  = $60 Revenue
]

cursor.executemany('INSERT INTO sales (item_name, price, quantity) VALUES (?, ?, ?)', sample_data)
conn.commit()

# ---------------------------------------------------------
# THE ANALYST'S JOB: SQL QUERY
# ---------------------------------------------------------

print("--- SQL Query Result ---")

# The Boss asks: "Show me items where Revenue is > $300, ordered from best to worst."
query = '''
    SELECT item_name, (price * quantity) as total_revenue
    FROM sales
    WHERE (price * quantity) > 300
    ORDER BY total_revenue DESC
'''

# Run the query and load it into a clean Pandas Table
df = pd.read_sql_query(query, conn)
print(df)

# Close the connection
conn.close()