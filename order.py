import pymysql as mysql
import add_add

mydb = mysql.connect(host="localhost", user="root", passwd="1234", database="Shopping")


def order(self):
    check = str(input("Do you want to place the order(Yes or No): "))
    if check.upper() == "YES":
        print("Your order has been placed.")
        mycursor = mydb.cursor()
        list = []
        mycursor.execute("SELECT * FROM cart")
        myresult = mycursor.fetchall()
        for rows in myresult:
            list.append(rows)

        sql = "INSERT INTO order_history (Pro_Id, Pro_Name, Unit_Price, Quantity, Total_Price) " \
              "VALUES (%s, %s, %s, %s, %s)"
        mycursor.executemany(sql, list)

        mycursor.execute("TRUNCATE TABLE cart")
        mydb.commit()

        add_add.add_add(self)

        print("All the item will be delivered within 10 working days.")
        print("Shopping complete.")

    else:
        print("Your items are saved in cart")
        mycursor = mydb.cursor()
        mycursor.execute("TRUNCATE TABLE order_history")
        mydb.commit()
