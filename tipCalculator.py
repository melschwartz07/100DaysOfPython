#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number.

print("Welcome to the tip calculator!")

total = float(input("What is the total of the bill? $"))
tip = int(input("What percentage would you like to tip? 10, 12, or 15."))
people = int(input("How many people are splitting the bill?"))

tip_as_percent = tip / 100
total_tip_amount = total * tip_as_percent
total_bill = total + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person shoud pay ${final_amount}")