#rent calculator
###inputs we neded from the user
#total rent
#total food ordered  
#electricity unnits spend
#charge per units

rent = int(input("Enter your flat rent = "))
food = int(input("enter the amount of food ordered"))
electricity_spend = int(input("Enter the total of electricity spend"))
charge_per_unit = int(input("Enter the charger per unit="))
persons = int(input("Enter the no. of person living="))

total_bill = electricity_spend * charge_per_unit
output = (food + rent + total_bill) //persons

print("each person will pay = ", output)