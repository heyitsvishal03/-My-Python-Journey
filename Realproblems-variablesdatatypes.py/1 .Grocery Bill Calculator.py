'''🛒 1. Grocery Bill Calculator'''

r = int(input("Enter the weight of rice"))
m = int(input("Enter the volume of milk"))
b = int(input("Enter the no of packets of biscuits"))
rp = r*40
mp = m*25
bp = b*15
print("Total price of rice =", rp)
print("Total price of milk =", mp)
print("Total price of biscuit =", bp)
print("Your Total Bill Amount is :-", rp + mp + bp , "/- rupees only ")
print("THANK YOU!")