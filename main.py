years = None
investment_amount = None
profit_percent = None

# Get years and make sure the input only contains numbers
years_set = False
while not years_set:
    try:
        years = float(input("Enter amount of years you're investing for: "))
        years_set = True
    except ValueError:
        print("Please enter years in numbers only")

# Get investment_amount and make sure the input only contains numbers
investment_set = False
while not investment_set:
    try:
        investment_amount = float(input("Enter investment amount: "))
        investment_set = True
    except ValueError:
        print("Please enter investment amount in numbers only")


# Get profit_percent and make sure the input only contains numbers
persent_set = False
while not persent_set:
    try:
        profit_percent = float(input("Enter annual increase percent: ")) / 100
        persent_set = True
    except ValueError:
        print("Please enter annual increase percent in numbers only")




# Calculate the total profit after X amount of years

if investment_amount and profit_percent and years:
    total_profit = investment_amount * (1+ profit_percent) ** years
    print(f"The total profit for a {int(years)} year investment of {int(investment_amount)} at {int(profit_percent * 100)}% is: {total_profit:.2f}")