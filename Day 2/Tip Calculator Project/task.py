print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

bill_total = bill * (1 + tip / 100)
bill_per_person = bill_total / people

print(f"Each person should pay: ${round(bill_per_person, 2)}")