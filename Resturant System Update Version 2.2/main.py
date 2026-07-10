import pandas as pd 
from datetime import datetime

df = pd.read_csv("Menu.csv")

cart=[]

print("Hello before you place an order, tell me......")

weather = input("How's the weather treating you today?\n(1-Hot🔥\n2-Cold❄️\n3-Normal🌸)\n(write a number🙂)\n")

if "1" in weather:
    print("\nI advise you to order some cold drinks🥤🧊")

    print("\nHere are our drinks😊❄️")

    drinks = df[df["Category"] == "Drink"]

    for _, row in drinks.iterrows():
        print(f"\nID:{row["ID"]} -> {row["Name"]:<10} | {row["Price"]}EGP  | Quantity:{row["Quantity"]}")

elif "2" in weather:
    print("You're in the right place👍, \nWe have food that will warm you up🔥😊")
    print("\nHere's are our Food😋🍔🍕\n")

    food = df[df["Category"] == "Food"]

    for _, row in food.iterrows():
        print(f"ID:{row["ID"]} -> {row["Name"]:<10} | {row["Price"]}EGP | Quantity:{row["Quantity"]}")

else:
    print("Welcome😊!, You light up the  Resturant\nFeel free to order anything you'd like🍔😊😋")
    
while True:

    print("\n" + "=" * 50)
    print("           🍔 Welcome to Resturant 🍔")
    print("=" * 50)
    print("\n" + "="*10+" Here's the Mneu for you 😊 "+"="*10)

    for category in df["Category"].unique():

        if category == "Food":
            print("\n          ========== Food🍕 ==========\n")

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

    print("1-order food🍔")
    print("2-Show cart🛒")
    print("3-Remove item from cart🛒❌")
    print("4-Exit👋")

    user_choise = input("Choise Option:")

    if user_choise == "1":
        food_id = int(input("Enter Food id:"))
        food = df[df["ID"] == food_id]
        if food.empty:
            print("Invalid food id ❌")
            continue

        Quantity = int(input("How much do you want(enter a number):"))
        avalid_quantity = food.iloc[0]["Quantity"]

        if Quantity > avalid_quantity:
            print("Not enough quantity ❌🫤")
            continue
        
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


        df.loc[df["ID"] == food_id, "Quantity"] = avalid_quantity - Quantity

        print("Added to cart ✅🛒")

    elif user_choise == "2":

        if not cart:
            print("Cart is empty 🛒❌")
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
            print(f"Subtotal = {total: .2f}EGP")
            print(f"\nVAT = {vat:.2f}EGP")
            print(f"\nTotal = {grand_total:.2f}EGP")
            print("\nDate :" , datetime.now().strftime("%d/%m/%Y"))
            print("Time :",datetime.now().strftime("%H:%M:%S"))



    elif user_choise == "3":
        if not cart:
            print("Cart is empty🛒❌")
            continue
        
        print("\n===== YOUR CART =====\n")

        for item in cart:
            print(f"ID:{item["ID"]} -> {item["Name"]} x{item["Qty"]}")

        remove_item = int(input("\nEnter item id to remove❌: "))
        found = False

        for item in cart:
            if item["ID"] == remove_item:
                df.loc[df["ID"] == remove_item,
                "Quantity"] += item["Qty"]
                cart.remove(item)
                print("Item removed Successfully✅")
                found = True
                break
            
        if not found:
            print("Item not found in your Cart❌")

    elif user_choise == "4":
        print("OK, Have a nice day 👋")
        break
    else:
        print("Invalid option ❌")


    df.to_csv("Menu.csv" , index=False)
