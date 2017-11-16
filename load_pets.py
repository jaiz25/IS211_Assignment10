#!usr/bin/env/python
# -*- coding: utf-8 -*-
"""Assignment 10 for IS211"""


import sqlite3 as lite


con = lite.connect('pets.db')

person = (
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
)

pet = (
    (1, 'Rusty', 'Dalmatian', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
)

person_pet = (
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
)


with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS person")
    cur.execute("DROP TABLE IF EXISTS pet")
    cur.execute("DROP TABLE IF EXISTS person_pet")
    cur.execute("CREATE TABLE person(id INT PRIMARY KEY, first_name TEXT, last_name TEXT, age INT)")
    cur.execute("CREATE TABLE pet(id INT PRIMARY KEY, name TEXT, breed TEXT, age INT, dead INT)")
    cur.execute("CREATE TABLE person_pet(person_id INT, pet_id INT)")
    cur.executemany("INSERT INTO person VALUES(?, ?, ?, ?)", person)
    cur.executemany("INSERT INTO pet VALUES(?, ?, ?, ?, ?)", pet)
    cur.executemany("INSERT INTO person_pet VALUES(?, ?)", person_pet)

