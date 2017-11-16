#!usr/bin/env/python
# -*- coding: utf-8 -*-
"""Assignment 10 for IS211"""


import sqlite3 as lite
import sys


con = lite.connect('pets.db')

with con:
    while True:
        person_id = int(raw_input("Enter a person's ID number: "))
        cur = con.cursor()
        results_one = cur.execute("SELECT * FROM person WHERE id =?", (person_id,))
        row_one = cur.fetchone()

        if row_one:
            first_name = row_one[1]
            last_name = row_one[2]
            results_two = cur.execute("SELECT pet.* FROM pet INNER JOIN person_pet ON pet.id = person_pet.pet_id "
                                      "WHERE person_id=?", (person_id,))
            print first_name + ' ' + last_name + " is " + str(row_one[3]) + ' years old.'
            row_two = cur.fetchall()
            for row in row_two:
                if row[4] == 1:
                    print first_name + ' ' + last_name + " owned " + row[1] + ', a ' + row[2] + ', who was ' + \
                        str(row[3]) + ' years old.'
                else:
                    print first_name + ' ' + last_name + " owns " + row[1] + ', a ' + row[2] + ', who is ' + \
                          str(row[3]) + ' years old.'
        elif person_id < 0:
            sys.exit()
        else:
            print "Error! Not a valid ID number."

con.close()
