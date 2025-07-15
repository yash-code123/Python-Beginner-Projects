print("Welcome to the tip calculator!")
bill = input("What was the total bill? ₹")
tip = input("How much tip would you like to give? ")
people = input("How many people to split the bill?")
total_bill = bill + tip
div = total_bill / people
final_pay = round(div, 2)
print(f"Each person should pay: ₹{final_pay}")
