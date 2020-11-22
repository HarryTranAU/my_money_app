import psycopg2


connection = psycopg2.connect(
    database="my_money_app",
    user="postgres",
    password="1234",
    host="localhost"
)

cursor = connection.cursor()

cursor.execute("create table if not exists books (id serial primary key, title varchar);")
connection.commit()