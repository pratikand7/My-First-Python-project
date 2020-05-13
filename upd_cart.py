import pymysql as mysql
import show_cart

mydb = mysql.connect(host="localhost", user="root", passwd="1234", database="Shopping")


def upd_cart(self):
    update = True
    show_cart.show_cart(self)
    mycursor = mydb.cursor()
    while update:
        check2 = str(input("Do you want to change any item's quantity(YES or NO) : "))
        if check2.upper() == "YES":
            id = input("Enter the product id for which item you want to change the quantity : ")
            num = int(input("By which number you want to change it : "))

            mycursor.execute("SELECT Quantity FROM cart where Pro_ID = %s", id)
            cartresult = mycursor.fetchone()

            mycursor.execute("SELECT Quantity FROM products where Pro_Id = %s", id)
            proresult = mycursor.fetchone()

            for q in cartresult:
                cartpre = q

            for r in proresult:
                propre = r

            total = propre + cartpre

            if total == 0:
                print("The product is out of stock")

            elif num > total:
                print("Sorry we have only {} items of this product left in the stock.".format(total))
                print("You can add only {} of this product in your cart.".format(total))

            else:
                post = total - num
                mycursor.execute("SELECT Unit_Price FROM products WHERE Pro_Id = %s", id)
                myresult = mycursor.fetchone()
                for cost in myresult:
                    price = cost
                total = price * num

                mycursor.execute("UPDATE cart SET Quantity = %s WHERE Pro_Id = %s", (num, id))
                mycursor.execute("UPDATE cart SET Total_Price = %s WHERE Pro_Id = %s", (total, id))
                mycursor.execute("UPDATE products SET Quantity = %s WHERE Pro_ID = %s", (post, id))
                mydb.commit()
                show_cart.show_cart(self)
        else:
            break
    show_cart.show_cart(self)
    while update:
        check3 = str(input("Do you want to remove any item(YES or NO) : "))
        if check3.upper() == "YES":
            val = int(input("Enter the product id you want to remove : "))

            mycursor = mydb.cursor()
            mycursor.execute("SELECT Quantity FROM cart where Pro_ID = %s", val)
            myresult = mycursor.fetchone()
            for quant in myresult:
                pre = quant

            mycursor.execute("SELECT Quantity FROM products where Pro_ID = %s", val)
            myresult = mycursor.fetchone()
            for proquant in myresult:
                ini = proquant

            post = pre + ini

            mycursor.execute("DELETE FROM cart WHERE Pro_Id = %s", val)
            mycursor.execute("UPDATE products SET Quantity = %s WHERE Pro_ID = %s", (post, val))

            mydb.commit()
            show_cart.show_cart(self)
        else:
            break
    show_cart.show_cart(self)
