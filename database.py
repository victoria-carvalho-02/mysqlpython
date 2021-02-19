import mysql.connector
# 0. local computer so local host, username and pwd of the mysql db
mydb = mysql.connector.connect(
	host ="localhost", 
	user ="root",
	passwd ="addyourpasswprd",
	database = "testdb"
	)


# 1. lets see if it works (an object will be created at a memory loc)

print(mydb)

# 2. create a cursor to select 
my_cursor = mydb.cursor()

# 3. Create a database 
my_cursor.execute("CREATE DATABASE testdb")

# 4. Comment 3 and check from python the databases
my_cursor.execute("SHOW DATABASES")
print(my_cursor)

# 5. Comment 1,3,4 and lets loop 4 since there will be lots of dbs
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
	print(db)

# 6. Comment 5 after checking the db's now we want to only use db as testdb, so  at 0. in mydb add database as testdb

# 7. CREATE a table

my_cursor.execute("CREATE TABLE users (name varchar(50), email varchar(255), age integer(10),user_id integer auto_increment PRIMARY KEY)")
#Show tables
my_cursor.execute("SHOW TABLES")
for table_in in my_cursor:
#returns tuple form -(tablename)
	print(table_in[0])


# 8. INSERT into the table - ie inserting one record into a table - Type 1
sql_insert = "INSERT INTO users (name,email,age) VALUES (%s, %s , %s)"
record_1 = ("Judit", "judit@gmail.com",26)

#Pass the values to the cursor
my_cursor.execute(sql_insert,record_1)

#commit it to the database because the above line will not save it
mydb.commit()


# 9. INSERT Multiple Records
sql_insert = "INSERT INTO users (name,email,age) VALUES (%s, %s , %s)"
#Arrays in python are called Lists. In this list add the values () in brackets

record_multiple = [ ("Ruben", "rubendcruz@gmail.com",89), ("Leora", "leorademello@gmail.com",56), ("Lara", "lararose@gmail.com",45), 
("Rose", "roseleo@gmail.com",46)] 
#Pass the values to the cursor and since we are executing many executemany
my_cursor.executemany(sql_insert, record_multiple)

#commit it to the database bz the above line will not save it
mydb.commit()


# 10. SELECT
my_cursor.execute("SELECT email from users")

select_record = my_cursor.fetch()

for rows in select_record:
	print(rows)

# 11. SELECT and WHERE Clause

my_cursor.execute("SELECT email from users where user_id = 5")

select_record = my_cursor.fetchall()

for rows in select_record:
	print(rows[0])

# 12. Formatting 

my_cursor.execute("SELECT * from users")

select_record = my_cursor.fetchall()
print("NAME\tAGE\tID\tEMAIL")
print("-----"*10)
for rows in select_record:
	print("{}\t{}\t{}\t{}".format(rows[0], rows[2], rows[3], rows[1]))


# 13. SELECT and BETWEEN 

my_cursor.execute("SELECT * from users")
select_record = my_cursor.fetchall()
for rows in select_record:
	print(rows)

print("---------Between Keyword------------")
my_cursor.execute("SELECT * from users where age between 40 and 50 ")

select_record = my_cursor.fetchall()

for rows in select_record:
	print(rows)

# 14. AND 

my_cursor.execute("SELECT * from users")
select_record = my_cursor.fetchall()
for rows in select_record:
	print(rows)

print("---------And Keyword------------")
my_cursor.execute("SELECT * from users where age = 45 and name like 'L%' ")

select_record = my_cursor.fetchall()

for rows in select_record:
	print(rows)

# 15. UPDATE
my_cursor.execute("UPDATE users SET email = 'samsmith@gmail.com' WHERE user_id = 5") 
mydb.commit()

my_cursor.execute("SELECT * FROM users")

for rows in my_cursor:
	print(rows)

# 16. LIMIT & ORDERING
#offset is skip the 1st row
my_cursor.execute("SELECT * FROM users LIMIT 3 OFFSET 1 ")
result = my_cursor.fetchall()
for rows in result:
	print(rows)


# 17. DELETE a row
my_cursor.execute("DELETE FROM users WHERE user_id = 4")
mydb.commit()

# 18. DROP TABLE
my_cursor.execute("DROP TABLE users ")

# 18.1 DROP TABLE if exists
my_cursor.execute("DROP TABLE IF EXISTS users ")
