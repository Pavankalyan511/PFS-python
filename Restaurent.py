enter = input("Enter status: ")
tables = 3
orders = 4
bill=0
if enter == "entered":
    print("Welcome sir")
    a = input("Enter user's Dialogue: ")
    if tables != 0:
        print("Yes Sir the tables are available")
    x = "Starters-Veg & Non-Veg, Veg Biryani, Non Veg Biryani, Butter Naan, All veg and nonveg fries, etc.. All these are good sir, and our restarent is famous for mutton biryani,chicken 65 and Soft Drinks sir"
    Menu = [
        "Ghobi Manchuria",
        "Paneer",
        "Butter Naan",
        "Prawn 65",
        "Chicken 65",
        "Mutton 65",
        "veg Biryani",
        "Chicken Biryani",
        "Mutton Biryani",
        "Soft Drinks",
        "ice creams",
    ]
    y = input("Enter user's Dialogue: ")
    print("Sure Sir, This is the Menu card:", Menu)
    print(x)
    while orders > 0:
        b = input("Enter users Dialogue: ").lower()
        if any(b in item.lower() for item in Menu):
            print("ok sir")
            Total_bill=bill
            orders -= 1
        else:
            print("Sorry sir the item is not available, please order from the menu provided!")
    c = input("Enter User's Dialogues: ")
    if Menu=="Ghobi Manchuria":
        bill+=150
    elif Menu=='Panner':
        bill+=100
    elif Menu=='Butter Naan':
        bill+=100
    elif Menu=='Prawn 65':
        bill+=150
    elif Menu=='Chicken 65':
        bill+=200
    elif Menu=='Mutton 65':
        bill+=250
    elif Menu=='veg Biryani':
        bill+=120
    elif Menu=='Chicken Biryani':
        bill+=170
    elif Menu=='Mutton Biryani':
        bill+=250
    elif Menu=='Soft Drinks':
        bill+=100
    elif Menu=='ice creams':
        bill+=100
    print(f"Here's the Bill sir: Rs. {Total_bill}")
    d = input("Enter User's Dialogues: ")
    print("Thank you Sir, if you felt satisfied by our service please give the rating sir, and please visit us again")
