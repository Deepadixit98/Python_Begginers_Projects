price = int(input('Enter price Rs. :'))
qty = int(input('Enter quantity no. :'))
amt = price * qty

if amt > 10000:
    print("yayy..........a discout of 10% is applicable !")
    discount = amt * 0.1
    amt = amt - discount
elif amt > 5000:
    print("yayy..........A discout of 5% is applicable !")
    discount = amt * 0.05
    amt = amt - discount
elif amt > 2000 :
     print("yayy..........A discout of 2% is applicable !")
     discount = amt * 0.02
     amt = amt - discount
elif amt > 1000:
     print("A discout of 1% is applicable !")
     discount = amt * 0.01
     amt = amt - discount
else : print("No discount !")

print('Your total amount is Rs. :', amt)

""" In this project, if-elif conditionalstatements 
and while (infinite) loop of python and COMMON SENSE. """