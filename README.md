# Overview

This is a simple SQL based database that would be used for an equipment lending company. The program open up a menu in the terminal that will allow 
the user to navigate to the table they wish to work with. Once they do the program will then prompt the user to indicate a command that they wish to preform with the tables. The databases are built in SQLite3 which is a sort of local SQL database.

I wrote this program to get practice using SQL Relational Databases. I chose to specifically make a "Equipment Lender" database because I use a 
database like this everyday at my work with the BYUI Production Office, but recently we have run into a few problems with this database and software
so thought it would be interesting to "mock up" a replacement software and database. 

[Software Demo Video](https://youtu.be/cvBuPgGyoDw)

# Relational Database

Like I wrote a bit earlier, I created this program using SQLite3. I would say the biggest reason I did this was so that I could practice SQL syntax, 

My program currently is divided into the maintenece of two tables. One for equipment the other for patrons. They both include Names and unique ID's, 
the unique ID's are based off the use of barcodes and card scans that we use currently at my office. This allows for there to be two patrons or pieces of equipment that have the same name, but are different and are treated differently.

# Development Environment

I used VS Code to edit my code. I like it because it has a lot of Python functionality built in, which makes it much easier and faster to develop Python programs.

I used Python to access SQLite through the sqlite3 library. I also used the connection library from multiprocessing to actually connect to my database.

# Useful Websites

* [SQLiteTutorial](https://www.sqlitetutorial.net/)
* [Python](https://docs.python.org/3.8/library/sqlite3.html)
* [Educba](https://www.educba.com/sqlite-sum/)

# Future Work

* Item 1 - I want to make a third table that is named reservations. This table will be able to access both other databases to make reservations for patrons of equipment. This table would check to make sure the status and condition of patrons and resources were viable before allowing for reservations to be made. It would also hold date and time information about the length of the reservation and due dates. Finally it would keep the total value of all the equipment that the reservation holds.
* Item 2 - I want to add more checks to make sure that the user is inputting valid data that will not cause the program to crash.
* Item 3 - I want to eventually make the menu in an app, or some sort of User Interface that will make the program more user friendly and appealing to use.1