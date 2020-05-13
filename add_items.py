import pymysql as mysql
import show_cart

mydb = mysql.connect(host="localhost", user="root", passwd="1234", database="Shopping")


def add_item(self):
    prid = input("Enter the product id you want to add in your cart : ")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Pro_Name FROM products WHERE Pro_Id = %s", prid)
    myresult = mycursor.fetchone()
    for name in myresult:
        item = name

    mycursor.execute("SELECT Unit_Price FROM products WHERE Pro_Id = %s", prid)
    myresult = mycursor.fetchone()
    for cost in myresult:
        price = cost

    quant = int(input("Enter the number of the item you wanted to buy : "))

    up_quant = 0

    mycursor.execute("SELECT Quantity FROM products where Pro_ID = %s", prid)
    myresult = mycursor.fetchone()
    for shop_quant in myresult:
        pre = shop_quant

    if pre == 0:
        print("The product is out of stock currently")

    elif pre < quant:
        print("Sorry we have only {} items of this product left in the stock.".format(pre))
        print("You can add only {} of this product in your cart.".format(pre))

    else:
        up_quant = pre - quant
        total = price * quant

        mycursor.execute(
            "INSERT INTO cart (Pro_Id, Pro_Name, Unit_Price, Quantity, Total_Price) VALUES (%s, %s, %s, %s, %s)",
            (prid, item, price, quant, total))

        mycursor.execute("UPDATE products SET Quantity = %s WHERE Pro_ID = %s", (up_quant, prid))
        mydb.commit()
        show_cart.show_cart(self)
