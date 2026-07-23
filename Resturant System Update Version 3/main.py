import pandas as pd 
from datetime import datetime
import os
import time

df = pd.read_csv("Menu.csv")

cart=[]
def clear():
    os.system("cls")
def weather_recommendation(df):
    print("Hello before you place an order, tell me......")

    print("How's the weather treating you today?\n1-Hot🔥\n2-Cold❄️\n3-Normal🌸")
    weather = input("1/2/3: ")

    if "1" in weather:
        print("\nI advise you to order some cold drinks🥤🧊")

        print("\n        Here are our drinks😊❄️")

        drinks = df[df["Category"] == "Drink"]

        for _, row in drinks.iterrows():
            print(f"\nID:{row["ID"]} -> {row["Name"]:<10} | {row["Price"]}EGP  | Quantity:{row["Quantity"]}")

        print("\n"+"-"*15)
        print("\nWould you like to place an order🍔💯")
        order = input("(Y/N): ").strip().lower()
        if order == "y":
            order_food(df, cart)
        else:
            print("\nWelcome😊!, You light up the  Resturant\nFeel free to order anything you'd like🍔😊😋")
            time.sleep(5)
            clear()
    elif "2" in weather:
        print("\nYou're in the right place👍, \nWe have food that will warm you up🔥😊")
        print("\nHere's are our Food😋🍔🍕\n")

        food = df[df["Category"] == "Food"]

        for _, row in food.iterrows():
            print(f"ID:{row["ID"]} -> {row["Name"]:<10} | {row["Price"]}EGP | Quantity:{row["Quantity"]}")
        
        print("\n"+"-"*15)
        print("\nWould you like to place an order🍔💯")
        order = input("(Y/N): ").strip().lower()
        if order == "y":
            order_food(df, cart)
        else:
            print("Welcome😊!, You light up the  Resturant\nFeel free to order anything you'd like🍔😊😋")
            time.sleep(5)
            clear()

    else:
        print("Welcome😊!, You light up the  Resturant\nFeel free to order anything you'd like🍔😊😋")
        time.sleep(5)
        clear()
def welcome_massage(df):
    print("=" * 50)
    print("""\n\n
        ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
        ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
        ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗
        ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝
        ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
        ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝

                             ████████╗ ██████╗
                             ╚══██╔══╝██╔═══██╗
                                ██║   ██║   ██║
                                ██║   ██║   ██║
                                ██║   ╚██████╔╝
                                ╚═╝    ╚═════╝

        ██████╗ ███████╗███████╗████████╗ █████╗ ██╗   ██╗██████╗  █████╗ ███╗   ██╗████████╗
        ██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║   ██║██╔══██╗██╔══██╗████╗  ██║╚══██╔══╝
        ██████╔╝█████╗  ███████╗   ██║   ███████║██║   ██║██████╔╝███████║██╔██╗ ██║   ██║
        ██╔══██╗██╔══╝  ╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██║╚██╗██║   ██║
        ██║  ██║███████╗███████║   ██║   ██║  ██║╚██████╔z██║  ██║██║  ██║██║ ╚████║   ██║
        ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝
        """)
def show_menu(df):
    print("=" * 50)
    print("""
            🍔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🍕
                Here's The Menu For You 😋
            🍰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🍹
        """)
    for category in df["Category"].unique():

        if category == "Food":
            print("          ========== Food🍕 ==========\n")


        elif category == "Desert":
            print("\n          ========== Desert🍰 ==========\n")
        elif category == "Drink":
            print("\n          ========== Drinks🍵 ==========\n")

        else:
            print(f"\n {category}")

        category_items = df[df["Category"] == category]

        for _, row in category_items.iterrows():
            print(
                f"ID:{row['ID']} -> "
                f"{row['Name']:<20} | "
                f"{row["Price"]} EGP |"
                f"Quantity:{row["Quantity"]:<20}"
            )

    print("\n" + "=" * 50)
def show_options(df):
    print("1-order food🍔")
    print("2-Show cart🛒")
    print("3-Remove item from cart🛒❌")
    print("4-Search by ID🔍")
    print("5-Search by Name🔍")
    print("6-Exit👋")
def order_food(df, cart):
        food_id = input("Enter Item id:")
        if food_id == "":
            print("You didn't write an Item ID❌,Try again🔁")
            time.sleep(3)
            clear()
            return
        food_id = int(food_id)
        food = df[df["ID"] == food_id]
        if food.empty:
            print("Invalid Item id ❌")
            time.sleep(2)
            clear()
            return
        
        name = food.iloc[0]['Name']
        price = food.iloc[0]['Price']
        available_quantity = food.iloc[0]["Quantity"]

        print("\n============ Item Details ============\n")
        print(
            f"Name    : {name}  \n"
            f"Price    : {price}EGP  \n"
            f"Qunatity    : {available_quantity}"
        )
        print("=" * 30)

        Quantity = input("How much do you want?:")
        if Quantity == "":
            print("You didn't write Qunatity❌,Try again🔁")
            time.sleep(3)
            clear()
            return
        if not Quantity.isdigit():
            print("Quantity must be a number, Try again🔁")
            time.sleep(3)
            clear()
            return
        Quantity = int(Quantity)
        available_quantity = food.iloc[0]["Quantity"]
        if Quantity <= 0:
            print("Quantity must be grater than 0.")
            print("Try again🔄️")
            time.sleep(3)
            clear()
            return

        if Quantity > available_quantity:
            print(f"Sorry, only {available_quantity} item(s) are available🤏")
            print("Try again🔄️")
            time.sleep(5)
            clear()
            return
        
        name = food.iloc[0]["Name"]
        price = food.iloc[0]["Price"]

        found = False

        for item in cart:
            if item["ID"] == food_id:
                item["Qty"] += Quantity
                item["Total"] = item["Qty"] * item["Price"]

                found = True
                break
        if not found:
            cart.append({
                "ID": food_id,
                "Name": name,
                "Price": price,
                "Qty": Quantity,
                "Total": price * Quantity
            })                


        df.loc[df["ID"] == food_id, "Quantity"] = available_quantity - Quantity

        print("Added to cart ✅🛒")
        time.sleep(3)
        clear()
def show_cart(df, cart):
        if not cart:
            print("\nCart is empty 🛒❌")
            print("\n"+"-"*15)
            print("\nWould you like to place an order🍔💯") 
            order = input("(Y/N): ").strip().lower()
            if order == "y":
                order_food(df, cart)

            else:
                print("\nno problem😊")
                print("\nOur Resturant is Always at your Service!!😊❤️")
                time.sleep(5)
                clear()

        else:
            print("\n===== YOUR CART =====\n")
            total = 0
            for item in cart:
                print(
                    f"{item['Name']:<20}"
                    f"x{item['Qty']:<7}"
                    f"{item['Price']}EGP"
                )

            print("\n" + "=" *10+" Receipt " + "=" *10 + "\n")

            print( 
                f"{'Name':<15}"
                f"{'Qty':<10}"
                f"{'Price':<10}"
                f"{'Total':<10}"
                )
            print("-"*50+"\n")
            for item in cart:
                print(
                    f"{item['Name']:<15} "
                    f"{item['Qty']:<10} "
                    f"{item['Price']:<10}"
                    f"{item['Total']:<10}"
                )
                total += item["Total"]
            if total >= 500:
                total *=0.9
                print("\n        10% Discount Aplplied🎉")    
            vat = total * 0.10
            grand_total = total + vat
            
            print("\n")
            print(f"Subtotal : {total: .2f}EGP")
            print(f"\nVAT : {vat:.2f}EGP")
            print(f"\nTotal : {grand_total:.2f}EGP")
            print("\nDate : " , datetime.now().strftime("%d/%m/%Y"))
            print("Time : ",datetime.now().strftime("%H:%M:%S"))   

            checkout(cart, vat, total, grand_total)                 
def remove_item(df, cart):
        if not cart:
            print("Cart is empty🛒❌")
            time.sleep(2)
            clear()
            return
        
        print("\n===== YOUR CART =====\n")

        for item in cart:
            print(f"ID:{item["ID"]} -> {item["Name"]} x{item["Qty"]}")

        remove_item = int(input("\nEnter item id to remove❌: "))
        found = False

        for item in cart:
            if item["ID"] == remove_item:
                removed_Qty = int(input("How many do you want to remove? "))

                if removed_Qty <= 0:
                    print("Invaild Qunatity!❌")
                    print("Try again🔄️")
                    found = True
                    time.sleep(3)
                    clear()
                    break
                
                if removed_Qty > item["Qty"]:
                    print("The quantity of item is more than what's in your cart🛒❌")
                    print("Try again🔄️")
                    found = True
                    time.sleep(5)
                    clear()
                    break

                df.loc[df["ID"] == remove_item,
                "Quantity"] += removed_Qty
                
                item["Qty"] -= removed_Qty

                item["Total"] = item["Qty"] * item["Price"]

                if item["Qty"] == 0:
                    cart.remove(item)
                print("Item updeted Successfuly✅🛒")
                found = True
                time.sleep(2)
                clear()
                break
        if not found:
            print("Item not found in your Cart❌")
            print("Try again🔄️")
            time.sleep(2)
            clear()
def search_food_id(df):
        food_id = input("Enter item ID: ")
        if food_id == "":
            print("You didn't write an ID❌,Try again🔁")
            time.sleep(3)
            clear()
            return
        
        if not food_id.isdigit():
            print("ID must be a number❌,Try again🔁")
            time.sleep(3)
            clear()
            return
        food_id = int(food_id)
        food = df[df["ID"] == food_id]

        if food.empty:
            print("Item ID didn't found❌")
            time.sleep(3)
            clear()
            return
        
        else:
            row = food.iloc[0]
            print("\n========== Food Found ==========\n")
            print(
            f"ID : {row['ID']}\n"
            f"Name : {row['Name']}\n"
            f"Category : {row["Category"]}\n"
            f"Price : {row['Price']}EGP\n"
            f"Quantity : {row['Quantity']}"
            )

            print("\nWould you like to place an order🍔💯") 
            order = input("(Y/N): ").strip().lower()
            if order == "y":
                order_food(df, cart)

            else:
                print("\nno problem😊")
                print("\nOur Resturant is Always at your Service!!😊❤️")
                time.sleep(5)
                clear()
def search_food_name(df):
        search = input("Enter Item Name: ").strip()

        if search == "":
            print("You didn't Enter an Item Name❗")
            print("Try again🔄️")
            time.sleep(3)
            clear()
            return
        result = df[df["Name"].str.contains(search,case=False)]
        if result.empty:
            print("Item not Found, Try again🔄️")
            time.sleep(3)
            clear()
            return
        else:
            print("\n============ Search Results ============\n")
            for _, row in result.iterrows():
                print(
                    f"ID:{row['ID']} -> "
                    f"{row['Name']:<20} | "
                    f"{row['Price']}EGP | "
                    f"Qunatity:{row['Quantity']}" 
                )
            print("\nWould you like to place an order🍔💯") 
            order = input("(Y/N): ").strip().lower()
            if order == "y":
                order_food(df, cart)

            else:
                print("\nno problem😊")
                print("\nOur Resturant is Always at your Service!!😊❤️")
                time.sleep(5)
                clear()
def exit_program(df):
    print("Thanks for visiting us ❤️")
    print("OK, Have a nice day 👋")
    return
def checkout(cart, vat, total, grand_total):
    print("\nWould you like To Checkout🛒💯✅")
    checkout = input("(Y/N): ").strip().lower()
    if checkout == "y":
        print("\n"+"="*15 +" PAYMENT RECEIPT "+"="*15)
        print( 
            f"{'Name':<15}"
            f"{'Qty':<10}"
            f"{'Price':<10}"
            f"{'Total':<10}"
            )
        print("-"*50+"\n")
        for item in cart:
            print(
                f"{item['Name']:<15} "
                f"{item['Qty']:<10} "
                f"{item['Price']:<10}"
                f"{item['Total']:<10}"
            )
        print(f"\n\nSubtotal : {total:.2f}EGP")
        print(f"\nVAT : {vat:.2f}EGP")
        print(f"\nTotal : {grand_total:.2f}EGP")
        print("-"*35)
        print("\nPayment Successfull!;✅")
        print("\nThanks for choosing our Resturant😇🍔")
        print("\nWe Hope to see you again soon!!😇❤️")
        cart.clear()
        print("Would you like place anothe Order or Exit!!")
        order = input("1/2: ")
        if order == "1":
            order_food(df, cart)
        elif order == "2":
            exit_program(df)
            exit()
    elif checkout == "n":
        print("\nno problem😊")
        print("\nOur Resturant is Always at your Service!!😊❤️")
        time.sleep(5)
        clear()
    else:
        print("Invaid choise❌")
        print("Try again🔄️")
        time.sleep(5)
        clear()



weather_recommendation(df)
while True:
    welcome_massage(df)
    show_menu(df)
    show_options(df)
    user_choise = input("Choise Option:")
    if user_choise == "1":
        order_food(df, cart)
    elif user_choise == "2":
        show_cart(df, cart)

    elif user_choise == "3":
        remove_item(df, cart)
    
    elif user_choise == "4":
        search_food_id(df)

    elif user_choise == "5":
        search_food_name(df)

    elif user_choise == "6":
        exit(df)
        break
    else:
        print("Invalid option ❌")
        print("Try again🔄️")
        time.sleep(3)
        clear()

    df.to_csv("Menu.csv" , index=False)
