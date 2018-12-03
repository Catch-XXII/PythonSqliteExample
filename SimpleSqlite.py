import sqlite3
import re

name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
phone = input('Please enter your phone number: ')
email = input('Please enter your email: ')
addressToVerify = email
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
if match is None:
    print('Not a valid E-mail address')
    raise ValueError('Not a valid E-mail address')


connection = sqlite3.connect('playerdb.db')

cursor = connection.cursor()

'''For the first time you have to uncomment below section in order to create a table with following properties '''
# cursor.execute('create table player(id integer primary key, name text not null, '
#                'age integer not null, email text unique not null, phone text unique not null);')

'''After creation of table you have to comment out the code section above again if you are using PyCharm 
the key combination is for ctrl + /
'''

cursor.execute('insert into player (name, age, email, phone) values(?, ?, ?, ?)', (name, age, email, phone))
connection.commit()


cursor.execute('select * from player')
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()


'''
Two things are important here first don't forget the commit after insert and the second one is don't forget the
close connection after select. in the first if you don't commit after insertion you will lose all your data.
in the second statement if you forget the close the connection it will suck your memory maybe not in this 
particular example obviously we don't have too much data which needs to be stored in the memory but if you have a huge
database an open connection will drain your memory. 
So, 
1 => commit after insertion
2 => close connection after select
'''
