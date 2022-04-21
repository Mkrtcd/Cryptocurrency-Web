import psycopg2
conn = psycopg2.connect(database="Crypto_app", user="hzha3299", 
                        password="Cs981020", host="cryptodatabase.ccftjy90se8y.ap-southeast-2.rds.amazonaws.com")
cur = conn.cursor()
postgres_select_query = ("UPDATE users SET pw = %s WHERE email = %s")
email = "test1@mail.com"
pw = "asd"
cur.execute(postgres_select_query, (pw, email))
#rows = cur.fetchall()
conn.commit()
conn.close()