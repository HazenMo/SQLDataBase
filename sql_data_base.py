#######################################################################
# SQL Data Base
# Author: Mosiah Hazen
# This will be a simple data base for an equipment lending company. It 
# will be written using SQLite. 
#######################################################################

from asyncio.windows_events import NULL
from multiprocessing import connection

# Importing the library for SQLite.
import sqlite3

# "Connecting" to database.
connection = sqlite3.connect('records.db')
cursor = connection.cursor()

# Creating a table if there is not one.
cursor.execute("CREATE TABLE IF NOT EXISTS resources(item_name TEXT, item_id TEXT, barcode REAL, value REAL, condition TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS patrons(patron_name TEXT, patron_id_number REAL, phone_number TEXT, email TEXT, standing TEXT)")


def display_menu():
    print("1) Display Equipment")
    print("2) Add Equipment")
    print("3) Update Condition")
    print("4) Delete Equipment")
    print("5) Quit")

def display_equipment():
    cursor.execute("SELECT * FROM resources")
    print("{:>14}  {:>17}  {:>16}  {:>16}".format("Name", "ID", "Value", "Condition"))
    for record in cursor.fetchall():
        print("{:>20}  {:>14}  {:>14}  {:>15}".format(record[0], record[1], record[3], record[4]))

def add_equipment():
    equipment_name = input("Name > ")
    equipment_id = input("Unique ID > ")
    barcode = input("Barcode > ")
    value = float(input("Value > "))
    condition = input("Condition > ")
    values = (equipment_name, equipment_id, barcode, value, condition)
    cursor.execute("INSERT INTO resources VALUES (?, ?, ?, ?, ?)", values)
    connection.commit()

def update_condition():
    unique_identifier = input("ID or Barcode > ")
    values1 = (unique_identifier, unique_identifier)
    cursor.execute("SELECT condition FROM resources WHERE item_id = ? OR barcode = ?", values1)
    print("Current Condition: {}".format(cursor.fetchone()[0]))
    condition_note = input("Condition Note > ")
    values = (condition_note, unique_identifier, unique_identifier)
    cursor.execute("UPDATE resources SET condition = ? WHERE item_id = ? OR barcode = ?", values)
    connection.commit()

def delete_equipment():
    unique_identifier = input("ID or Barcode > ")
    values1 = (unique_identifier, unique_identifier)
    cursor.execute("DELETE FROM resources WHERE item_id = ? OR barcode = ?", values1)
    connection.commit()

def add_patron():
    print

def display_patrons():
    print

def show_contact_info():
    print

def main():
    userInput = NULL
    while(userInput != 5):
        display_menu()
        userInput = int(input("> "))
        print()
        match userInput:
            case 1:
                display_equipment()
            case 2:
                add_equipment()
            case 3:
                update_condition()
            case 4:
                delete_equipment()

        print()
    connection.close()


main()
