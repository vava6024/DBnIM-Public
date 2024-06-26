# -*- coding: utf-8 -*-
"""DBnI #1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BnIIa66wQDMxhQNjnhfAuTdYyYSeS9Wv
"""

#Nevaeh Johnson
import sqlite3

# establish connection
conn = sqlite3.connect('demo.db')

#used to execute SQL commands
cursor = conn.cursor()

# creat 'User' Table
cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                  user_ID INTEGER PRIMARY KEY,
                  username TEXT UNIQUE,
                  email TEXT UNIQUE,
                  password TEXT,
                   create_at TIMESTMP DEFAULT CURRENT_TIMESTAMP
                   )''')

# create ' UserActivites' Table
cursor.execute(''' CREATE TABLE IF NOT EXISTS UserActivites (
                   activity_id INTEGER PRIMARY KEY,
                   user_id INTEGER,
                   activity TEXT,
                   activity_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                   FOREIGN KEY (user_id) REFERENCES Users(user_id)
                   )''')

# create 'UserConnections' Table
cursor.execute('''CREATE TABLE IF NOT EXISTS UserConnections (
                  connection_id INTEGER PRIMARY KEY,
                  user1_id INTEGER,
                  user2_id INTEGER,
                  connection_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  FOREIGN KEY (user1_id) REFERENCES Users(user_id)
                  FOREIGN KEY (user2_id) REFERENCES Users(user_id)
                )''')

# create indexes for data retrieval
cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_id ON UserActivites(user_id)")

cursor.execute("CREATE INDEX IF NOT EXISTS idx_user1_user2 ON UserConnections(user1_id, user2_id)")

# commit (save) changes
conn.commit()

# add (insert) data into User Table
cursor.execute("INSERT INTO Users (username, email, password) VALUES (?, ?, ?)", ('Vaeh','Vaeh804@example.com','Unicornmath'))

cursor.execute("INSERT INTO Users (username,email,password) VALUES (?, ?, ?)", ('Marci','bubblegum@example.com','finnndjake24'))

# add (insert) data into UserActivities Table
cursor.execute("INSERT INTO UserActivites (user_id, activity) VALUES (?,?)", (1, 'Logged in'))

cursor.execute("INSERT INTO UserActivites (user_id, activity) VALUES (?,?)", (2,'Posted a comment'))

# add (insert) data into UserConnections Table
cursor.execute("INSERT INTO UserConnections (user1_id, user2_id) VALUES (?,?)", (2,1))

# commit (save) changes
conn.commit()

# query and print data from the Users Table
print("Users:")
cursor.execute("SELECT * FROM Users")
for row in cursor.fetchall():
     print(row)
# query and print data from UserActivites
print("/nUser Activities:")
cursor.execute("SELECT * FROM UserActivites")
for row in cursor.fetchall():
     print(row)

# query and print from the UserConnecctions Table
print("/nUser Connections:")
cursor.execute("SELECT * FROM UserConnections")
for row in cursor.fetchall():
     print(row)

# close the database connection
conn.close()

