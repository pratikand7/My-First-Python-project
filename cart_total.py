import pymysql as mysql


mydb = mysql.connect(host="localhost", user="root", passwd="1234", database="Shopping")


def cart_total(self):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT SUM(Total_Price) AS Total FROM cart")
    myresult = mycursor.fetchone()

    for x in myresult:
        print("Your cart total amount is : ", x)
