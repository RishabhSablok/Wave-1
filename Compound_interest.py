# Taking input before doing calculations
interest__rate = 4/100
principle = int(input("Input the principle amount: "))
# Doing all the calculations
amount_one_year = principle * (1 + interest__rate) ** 1
amount_two_year = principle * (1 + interest__rate) ** 2
amount_three_year = principle * (1 + interest__rate) ** 3
# Printing the answer
print("Your invesmeent will become", round(amount_one_year, 2), "in one year.")
print("Your invesmeent will become", round(amount_two_year, 2), "in two year.")
print("Your invesmeent will become", round(amount_three_year, 2), "in three year.")