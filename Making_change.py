cents = int(input("Input the amount of cents: "))
toonies = 0
loonies = 0
pennies = 0
nickels = 0
dimes = 0
quarters = 0
while cents != 0:
    if cents >= 200:
        cents -= 200
        toonies += 1
    if 200 >= cents >= 100:
        cents -= 100
        loonies += 1
    if 100 >= cents >= 25:
        cents -= 25
        quarters += 1
    if 25 >= cents >= 10:
        cents -= 10
        dimes += 1
    if 10 >= cents >= 5:
        cents -= 5
        nickels += 1
    if 5 >= cents >= 1:
        cents -= 1
        pennies += 1

print("Toonies: ", toonies)
print("Loonies: ", loonies)
print("Quarters: ", quarters)
print("Dimes: ", dimes)
print("Nickels: ", nickels)
print("Pennies: ", pennies)