# importing pymysql
import pymysql as mysql
# importing tabulate
from tabulate import tabulate

# connecting to the local database server
mydb = mysql.connect(host="localhost", user="root", passwd="****", database="Shopping")


# defining the class
class ShoppingCart:
    # defining a method to display the categories
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
        
    # defining method for displaying cart value
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

    # defining method to add items into the cart
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
            a.show_cart()

    # defining method to start the shopping
    def shop(self):
        shopping = True
        while shopping:
            b.display_cat()

            c.add_item()

            cond = str(input("Want to shop more(YES OR NO) = "))
            if cond.upper() == "YES":
                shopping = True
            else:
                shopping = False

    # defining the method for updating cart values
    def upd_cart(self):
        update = True
        a.show_cart()
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
                    a.show_cart()
            else:
                break
        a.show_cart()
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
                a.show_cart()
            else:
                break
        a.show_cart()

    # defining a method to display total cart value
    def cart_total(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT SUM(Total_Price) AS Total FROM cart")
        myresult = mycursor.fetchone()

        for x in myresult:
            print("Your cart total amount is : ", x)

    # defining a method to add an address
    def add_add(self):
        address = str(input("Enter the delivery address : "))
        type = str(input("Enter the address type(Home, Office) : "))

        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO Address_Book(Type, Address) VALUES(%s, %s)", (type, address))
        mydb.commit()

    # defining method to place the order
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

            sql = "INSERT INTO order_history (Pro_Id, Pro_Name, Unit_Price, Quantity, Total_Price) "\
                  "VALUES (%s, %s, %s, %s, %s)"
            mycursor.executemany(sql, list)

            mycursor.execute("TRUNCATE TABLE cart")
            mydb.commit()
            h.add_add()
            print("All the item will be delivered within 10 working days.")
            print("Shopping complete.")

        else:
            print("Your items are saved in cart")
            mycursor = mydb.cursor()
            mycursor.execute("TRUNCATE TABLE order_history")
            mydb.commit()

    # defining a method to start the whole shopping procedure
    def start(self):
        list = []
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM cart")
        myresult = mycursor.fetchall()
        for rows in myresult:
            list.append(rows)

        if not list:
            d.shop()

            e.upd_cart()

            f.cart_total()
            
            g.order()

        else:

            a.show_cart()

            cond = int(
                input("Do you want to review your cart(give input '1') or do you want to clear cart(give input '2'): "))
            if cond == 1:
                review = True
                while review:
                    cond1 = int(input("Do you want to add an item(give '1' as input) or \n"
                                      "Do You want to review/delete any item(give '2' as input) or\n"
                                      "Do you want place the order(give '3' as input): "))
                    if cond1 == 1:
                        d.shop()
                    elif cond1 == 2:
                        e.upd_cart()
                    else:
                        f.cart_total()

                        g.order()
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
                d.shop()

                e.upd_cart()

                f.cart_total()
                
                g.order()


a = ShoppingCart()

b = ShoppingCart()

c = ShoppingCart()

d = ShoppingCart()

e = ShoppingCart()

f = ShoppingCart()

g = ShoppingCart()

h = ShoppingCart()

i = ShoppingCart()
i.start()
