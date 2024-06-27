# SQLITE - What is it?
#   1. Sqlite is a relational database management system
#   2. Sqlite can be used by using the sqlite3 module in python
#   3. "lite" refers to how light the database is for managing setup,
#       admin, and resources

# SQLITE - Why is it unique?
#   1. Sqlite is serverless, when normally a RDBMS does
#   2. Sqlite databases are locally stored. Accessing and manipulating
#      data is therefore extremely quick
#   3. No special installation or server configuration needed.

# SQLITE - Self Contained
#   1. Doesn't require many external libraries, therefore sqlite is
#      quite compatible with a variety of platforms

# SQLITE - ACID Complaint
#   1. ACID or Atomic, Consistent, Isolated, and Durable
#   2. When transactions (a set of queries) are made they resemble a
#      series of actions that all take place at once
#   3. Being ACID complaint means that the database will never be in a
#      half completed state (either all queries were successful or none were)

# SQLITE - Data Types
#   Full List at: https://www.w3schools.com/sql/sql_datatypes.asp
#   1. String Data Types
#       a. CHAR(size) --> Fixed length string. "size" specifies the column 
#          length in characters which can be from 0-255. Default is 1
#       b. TEXT(size) --> Holds a string with a max length of 255 chars.
#   2. Numeric Data Types
#       a. TINYINT(size) --> Very small integer. Signed range is -128 to 128.
#          Unsigned range is from 0 to 255. "size" is max display width.
#       b. INT(size) --> Medium integer. Signed ranged is -2147483648 to 2147483647
#          unsigned ranged is 0 to 4294967295. "size" specifics the max display width
#       c. BOOL or BOOLEAN --> "Zero" or "0" is considered "FALSE". Any nonzero value
#          is considered true.

# from bs4 import BeautifulSoup
# import requests 
# import os
# import sqlite3
# Establishes initial DB connection
# NOTE: Creates DB if not already
# connection = sqlite3.connect('learning.db') 

# Cursor object acts as a transaction facilitator
# cursor = connection.cursor() 

# SQL commands are encased in triple quotes
# cursor.execute('''CREATE TABLE IF NOT EXISTS Learning 
#               (Description TEXT, Price TEXT, Location TEXT, Mileage TEXT, Link TEXT)''')
                # TINYTEXT        # TINYTEXT  # TINYTEXT     #TINYTEXT     #TEXT

# Use the DELETE command to clear all entries in a specific table
# cursor.execute('''DELETE FROM Learning''')

# Use the INSERT command to actually input data. If there isn't a check to first see if the 
#   entry exists or not, this line of code will keep adding copies
# cursor.execute('''INSERT INTO Learning VALUES('2005 Toyota Prius', '$5000', 'St. Paul', '125k', 'https://www.lol.com')''')

# Use the INSERT
# postings = [('2006 Toyota Camry', '$10000', 'Minneapolis', '50k', 'https://www.lol1.com'),
#             ('2012 Toyota Corolla', '$12000', 'Coon Rapids', '30k', 'https://www.lol2.com'),
#             ('2019 Toyota Rav4', '$15000', 'Hopkins', '20k', 'https://www.lol3.com'),
#             ('2000 Toyota Tacoma', '$3000', 'Plymouth', '180k', 'https://www.lol4.com')]
# cursor.executemany('INSERT INTO Learning VALUES(?,?,?,?,?)', postings)   

# SELECT Command issues a "pointer" to something. The below command tells the cursor 
#   to point to the collection of entries in the Learning DB. This pointer is then 
#   actionable later
# cursor.execute('''SELECT * FROM Learning''')

# "fetchone()" will pull the first entry from the original list
# "fetchall()" will pull all entries from what the cursor is pointing at
# print(cursor.fetchall())

# Once a set of queries is set, we tell the connection to commit these changes
# connection.commit()

# Once committed, close the connection
# connection.close()


#TEST_URL = "https://quotes.toscrape.com/"

### TESTING ###
#webpage_html = requests.get(TEST_URL)
#soup = BeautifulSoup(webpage_html.text, "html.parser")
#quotes = soup.findAll("span", attrs={"class":"text"})
#authors = soup.findAll("small", attrs={"class":"author"})

#for quote in quotes:
#    print(quote.text)
#for author in authors:
#    print(author.text)