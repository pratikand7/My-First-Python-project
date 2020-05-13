import pymysql as mysql
from tabulate import tabulate

mydb = mysql.connect(host="localhost", user="root", passwd="1234", database="Shopping")


def show_cart(self):
    # defining an empty list
    list = []
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM cart")
    myresult = mycursor.fetchall()
    for rows in myresult:
        list.append(rows)
    header = ["Pro_Id", "Pro_Name", "Unit_Price(in dollars)", "Quantity", "Total_Price(in dollars)"]
    print(tabulate(list, headers=header))
    print("*****************************************************************")
