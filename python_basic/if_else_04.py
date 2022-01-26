# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.


quantity = int(input('Enter the quantity\n'))
total =  quantity * 100
Discount =  total - total *0.10
txt = 'Discount for  you is {} '

if total>1000:
 print (total)
 print(txt.format(Discount),"\nThanks for shopping")
else:
 print(total)   
 print("No discount")
 
