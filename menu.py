#Menu
menu={
    "pizza": {
        "small": 250,
        "medium": 350,
        "large": 500
    },
    "momos": {
        "half": 40,
        "full": 70
    },
    "burger": {
        "regular": 40,
        "double-cheese":60
    },
    "springroll": {
        "regular": 50
    },
    "milkshake": {
        "half": 40,
        "large": 80
    }
}


print("Welcome to the restaurant")

name = input("Enter customer name: ")


#menu items print
print("pizza🍕:\nsmall:250\nmedium:350\nlarge:500")
print("\nmomos:\nhalf:40\nfull:70")
print("\nburger🍔:\nregular:40")
print("\nspringroll:\nregular:50")
print("\nmilkshake🧋:\nhalf:40\nlarge:80\n")
print("Special discount for today if you order for more than 1000 you will get 15% discount\n and if more than 500 you will get 10% dicount")
totalbill=0
orders=[]
item_one=input("enter the first item name  =  ")
size=input("enter the size of the item ")
qty = int(input("enter quantity "))
if item_one in menu:  
    totalbill=totalbill+(menu[item_one][size]*qty)
    orders.append(f"{item_one} ({size}) x {qty}")
    print(f"first order added {item_one} and the bill is{totalbill}")
else:
    print("sorry! item out of stock")


#another order
while True:
    print("Do you want another item from the menu")
    permission=input("yes/No ")
    if permission=="yes":
        another_item=input("enter the item ")
        size=input("enter the size of the item ")
        qty = int(input("enter quantity "))
        if another_item in menu:
            totalbill = totalbill + (menu[another_item][size] * qty)
            orders.append(f"{another_item} ({size}) x {qty}")
            print(f"{another_item} added and the bill is {totalbill}")
        else:
            print("sorry! item out of stock")
    else:
        break



#discount
discount=0
if totalbill>1000:
    discount=totalbill*0.15
elif totalbill>500:
    discount=totalbill*0.10
final_bill=totalbill-discount


#delivery
delivery = input("Home delivery? (yes/no): ")
if delivery == "yes":
    final_bill=final_bill+ 40
    print("Delivery charge added: ₹40")
print(f"Customer: {name}\n")
print("\nItems Ordered:")
for i, item in enumerate(orders, start=1):
    print(f"{i}. {item}")
print(f"the total amount is {totalbill}")
print(f"special discount{discount}")
print(f"total bill is {final_bill} ")