import pymysql as mysql
import display_cat
import add_item

mydb = mysql.connect(host="localhost", user="root", passwd="1234", database="Shopping")


def add_cart(self):
    shopping = True
    while shopping:
        display_cat.display_cat(self)

        add_item.add_item(self)

        cond = str(input("Want to shop more(YES OR NO) = "))
        if cond.upper() == "YES":
            shopping = True
        else:
            shopping = False
