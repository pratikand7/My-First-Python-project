# importing pymysql
import pymysql as mysql
# importing all the user defined modules
import show_cart
import add_cart
import upd_cart
import order
import cart_total

mydb = mysql.connect(host="localhost", user="root", passwd="1234", database="Shopping")


# defining the class
class ShoppingCart:

    def shop(self):
        list = []
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM cart")
        myresult = mycursor.fetchall()
        for rows in myresult:
            list.append(rows)

        if not list:
            add_cart.add_cart(self)

            upd_cart.upd_cart(self)

            cart_total.cart_total(self)
            
            order.order(self)

        else:

            show_cart.show_cart(self)

            cond = int(input("Do you want to review your cart(give input '1') or do you want to clear cart(give input '2'): "))
            if cond == 1:
                review = True
                while review:
                    cond1 = int(input("Do you want to add an item(give '1' as input) or \n"
                                      "Do You want to review/delete any item(give '2' as input) or\n"
                                      "Do you want place the order(give '3' as input): "))
                    if cond1 == 1:
                        add_cart.add_cart(self)
                    elif cond1 == 2:
                        upd_cart.upd_cart(self)
                    else:
                        cart_total.cart_total(self)

                        order.order(self)
                        break
            else:
                mycursor = mydb.cursor()
                mycursor.execute("SELECT Pro_Id FROM cart")
                myresult = mycursor.fetchall()
                for i in myresult:
                    val = i
                    mycursor.execute("SELECT Quantity FROM cart where Pro_ID = %s", val)
                    myresult1 = mycursor.fetchone()
                    for quant in myresult1:
                        pre = int(quant)
                    mycursor.execute("SELECT Quantity FROM products where Pro_ID = %s", val)
                    myresult2 = mycursor.fetchone()
                    for proquant in myresult2:
                        ini = int(proquant)

                    post = pre + ini
                    mycursor.execute("UPDATE products SET Quantity = %s WHERE Pro_ID = %s", (post, val))

                mycursor.execute("TRUNCATE TABLE cart")
                mydb.commit()
                print("your cart has been cleared.\nStart shopping. \n")
                add_cart.add_cart(self)

                upd_cart.upd_cart(self)

                cart_total.cart_total(self)
                
                order.order(self)


start = ShoppingCart()

start.shop()
