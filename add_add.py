# import mysql module to use mysql functions
import pymysql as mysql
# connecting to mysql server
mydb = mysql.connect(host="localhost", user="root", passwd="1234", database="Shopping")


# defining the method for adding address
def add_add(self):

    address = str(input("Enter the delivery address : "))
    type = str(input("Enter the address type(Home, Office) : "))

    mycursor = mydb.cursor()
    # inserting the data into the address_book table
    mycursor.execute("INSERT INTO Address_Book(Type, Address) VALUES(%s, %s)", (type, address))
    mydb.commit()
