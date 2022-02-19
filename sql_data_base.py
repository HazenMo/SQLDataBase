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
cursor.execute("CREATE TABLE IF NOT EXISTS patrons(patron_name TEXT, patron_id_number INTEGER, phone_number TEXT, email TEXT, standing TEXT)")

# First menu user sees.
def display_menu():
    print("1) Equipment Table")
    print("2) Patron Table")
    print("3) Quit")

# If they navigate to the equipment menu.
def display_equip_menu():
    print("1) Display Equipment")
    print("2) Add Equipment")
    print("3) Update Condition")
    print("4) Delete Equipment")
    print("5) Display Total Value")
    print("6) Back to Main")

# If they navigate to the patron menu.
def display_patron_menu():
    print("1) Display Patrons")
    print("2) Add Patron")
    print("3) Display Contact Info")
    print("4) Delete Patron")
    print("5) Back to Main")

# Simple query to display all the resources in the table resources.
def display_equipment():
    cursor.execute("SELECT * FROM resources")
    print("{:>14}  {:>17}  {:>16}  {:>16}".format("Name", "ID", "Value", "Condition"))
    for record in cursor.fetchall():
        print("{:>20}  {:>14}  {:>14}  {:>15}".format(record[0], record[1], record[3], record[4]))

# Inserting rows into the table resources.
def add_equipment():
    equipment_name = input("Name > ")
    equipment_id = input("Unique ID > ")
    barcode = input("Barcode > ")
    value = float(input("Value > "))
    condition = input("Condition > ")
    values = (equipment_name, equipment_id, barcode, value, condition)
    cursor.execute("INSERT INTO resources VALUES (?, ?, ?, ?, ?)", values)
    connection.commit()

# Querying the resources table with a unique value, then updating a
# specific column.
def update_condition():
    unique_identifier = input("ID or Barcode > ")
    values1 = (unique_identifier, unique_identifier)
    cursor.execute("SELECT condition FROM resources WHERE item_id = ? OR barcode = ?", values1)
    print("Current Condition: {}".format(cursor.fetchone()[0]))
    condition_note = input("Condition Note > ")
    values = (condition_note, unique_identifier, unique_identifier)
    cursor.execute("UPDATE resources SET condition = ? WHERE item_id = ? OR barcode = ?", values)
    connection.commit()

# Removing a specific item.
def delete_equipment():
    unique_identifier = input("ID or Barcode > ")
    values1 = (unique_identifier, unique_identifier)
    cursor.execute("DELETE FROM resources WHERE item_id = ? OR barcode = ?", values1)
    connection.commit()

# Summing the value of all resources.
def total_value():
    cursor.execute("SELECT SUM(value) FROM resources")
    total = cursor.fetchone()[0]
    print(f"Total Value of Center: {total}")

# Inserting a row into patron table.
def add_patron():
    patron_name = input("Name > ")
    patron_id_number = input("Unique ID Number > ")
    phone_number = input("Phone Number > ")
    email = input("Email > ")
    status = input("Status > ")
    values = (patron_name, patron_id_number, phone_number, email, status)
    cursor.execute("INSERT INTO patrons VALUES (?, ?, ?, ?, ?)", values)
    connection.commit()

# Querying the patron table for all rows.
def display_patrons():
    cursor.execute("SELECT * FROM patrons")
    print("{:>14}  {:>11}".format("Name", "ID Number"))
    for record in cursor.fetchall():
        print("{:>14}  {:>11}".format(record[0], int(record[1])))

# Querying the patron table for specific information that could be
# useful in real life.
def show_contact_info():
    patron_id_number = input("ID Number > ")
    cursor.execute("SELECT * FROM patrons WHERE patron_id_number = ?", (patron_id_number,))
    patron = cursor.fetchall()[0]
    print
    print("Contact Info for {}: {} {}".format(patron[0], patron[2], patron[3]))

# Deleting a row from patron table.
def delete_patron():
    patron_id_number = input("ID Number > ")
    cursor.execute("DELETE FROM patrons WHERE patron_id_number = ?", (patron_id_number,))
    connection.commit()

# Prompts user for built in command.
def equipment_menu():
    userInput = NULL
    while(userInput != 6):
        display_equip_menu()
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
            case 5:
                total_value()

        print()
    return None

# Prompts user for built in command.
def patron_menu():
    userInput = NULL
    while(userInput != 5):
        display_patron_menu()
        userInput = int(input("> "))
        print()
        match userInput:
            case 1:
                display_patrons()
            case 2:
                add_patron()
            case 3:
                show_contact_info()
            case 4:
                delete_patron()

        print()
    return None

# Calls other functions to get the program started and also to end 
# it.
def main():
    userInput = NULL
    while(userInput != 3):
        display_menu()
        userInput = int(input("> "))
        print()
        match userInput:
            case 1:
                equipment_menu()
            case 2:
                patron_menu()

        print()
    connection.close()


main()
