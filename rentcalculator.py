##Input from the user
#no.of users in room/hostel
#Room rent
#total food orderd price
#electricity bill
#charge per 1 unit
#toutput:otal amount should be paid 
person=int(input("Enter no.of persons living in the room/hostel:"))
rent=int(input("Enter your hostel/room rent:"))
food=int(input("Enter the amount of food ordered:"))
electricity=int(input("Enter the amount of electricity spend:"))
charge_per_unit=int(input("Enter the amount of charge per unit :"))
Total_amount_paid_per_person=(rent+food+electricity*charge_per_unit)//3
print(f"Total amount should pay by  each  person is {Total_amount_paid_per_person}")

