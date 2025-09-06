print("Welcome to our Restaurant.Here is the menu")
menu={
        'Pizza':250,
        'Burger':100,
        'Pasta':120,
        'Coffee':80
    }
print("1.Pizza:Rs 250\n","2.Burger:Rs 100\n","3.Pasta:Rs 120\n","4.Coffee:Rs 80\n")
Total_Order=0

Ordered_Items=input("Enter the name of the item you want to order : ")
if Ordered_Items in menu:
        Total_Order+=menu[Ordered_Items]
        print(f"Your item {Ordered_Items} has been added to your order")
else:
        print("Your orderes item is not in the menu ")
while True:
    another_order=input("Do you want to order anything else(Yes/No):")
    if another_order=="No":
        break
    else:
        if  another_order == "Yes":
            item2=input("Enter the name of the item you want to order now:")
            if item2 in menu:
                Total_Order+=menu[item2]
                print(f"Your item{item2} is added on your order cart")
            else:
                print("Item is not available in the menu")
   

print(f"Your Total Bill is:Rs{Total_Order}")


