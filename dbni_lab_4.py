# -*- coding: utf-8 -*-
"""DBnI Lab 4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NLLZYZ17X0LQDWpj5L-yFuMnpM3tgc9h
"""

# Nevaeh Johnson
import sqlite3

# connect to SQLite database
conn = sqlite3.connect('memory:')
cursor = conn.cursor()

print("establish in-memory database connection")

# create users table
cursor.execute(''' CREATE TABLE IF NOT EXISTS users (
                    id INTERGER PRIMARY KEY,
                    name TEXT,
                    balance REAL
                )''')

# add/insert data
cursor.execute("INSERT INTO users (name, balance) VALUES (?, ?)", ('Marci', 100000.0))
cursor.execute("INSERT INTO users (name, balance) VALUES (?, ?)", ('Vaeh', 7000.0))

# function to handle transfer funds transaction
def transfer_funds(sender, recipient, amount):
    try:
        # check if transaction is active
        if not conn.in_transaction:
          # start transaction
          conn.execute("BEGIN")

        # check if sender has sufficient balance
        cursor.execute("SELECT balance FROM users WHERE name=?", (sender,))
        sender_balance = cursor.fetchone()[0]
        if sender_balance < amount:
            raise ValueError("Insuffienct funds")

        #update sender's balance
        cursor.execute("UPDATE users SET balance = balance - ? WHERE name=?", (amount, sender))

        # update recipient's balance
        cursor.execute("UPDATE users SET balance = balance + ? WHERE name=?", ( amount, recipient))

        # commit transaction
        if not conn.in_transaction:
          # commit only if not already in transaction
          conn.commit()
        print("Transaction successful")
    except Exception as e:
        # rollback transaction if any error occurs
        if not conn.in_transaction:
            # rollback only if not alrady in a transaction
            conn.rollback()
        print("Created function to handle transfer of funds")

# perform a fund transfer
transfer_funds('Marci', 'Vaeh', 1000.0)

# display balances after transaction
cursor.execute("SELECT name, balance FROM users")
print(cursor.fetchall())

# close database connection
conn.close()

print("close database connection")