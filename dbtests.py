import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rambo@123",
    database="subscribersdb",
    port=3307  #  Important: You are using port 3307, not 3306
)

cursor = conn.cursor()

# Validate the subscriber table has expected columns
cursor.execute("DESCRIBE subscriber")
columns = cursor.fetchall()

required_columns = ["id", "email", "subscription_date"]
existing_columns = [column[0] for column in columns]
missing = [col for col in required_columns if col not in existing_columns]

if missing:
    raise Exception(f" Missing column(s): {', '.join(missing)}")

print(" Schema is valid!")

conn.close()

conn.close()


