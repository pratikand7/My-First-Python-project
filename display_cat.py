import pymysql as mysql
from tabulate import tabulate

mydb = mysql.connect(host="localhost", user="root", passwd="1234", database="Shopping")


def display_cat(self):
    # define an empty list where all the data from database will be stored
    cat = []
    mycursor = mydb.cursor()
    # sql query for selecting the columns to display
    mycursor.execute("SELECT Pro_Id, Pro_Name, Unit_Price FROM products")
    myresult = mycursor.fetchall()
    for rows in myresult:
        cat.append(rows)
    header = ["id", "Name", "Price(in dollars)"]
    # tabulating the category display
    print(tabulate(cat, headers=header))
