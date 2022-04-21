import psycopg2

conn = psycopg2.connect(database="user_info", user="postgres", password="19960926", host="localhost")

cur = conn.cursor()
cur.execute("select * from users")
rows = cur.fetchall()
print(rows)
conn.commit()
conn.close()
# laige
