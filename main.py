years = None
investment_amount = None
profit_percent = None
total_profit = None


# Get name of company you want to invest with
company_name = input("Enter the name of the company that you want to invest with: ")

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

if investment_amount is not None and profit_percent is not None and years is not None and company_name is not None:
    total_profit = investment_amount * (1+ profit_percent) ** years
    print(f"The total profit for a {int(years)} year investment of {int(investment_amount)} at {int(profit_percent * 100)}% is: {total_profit:.2f}")
    with open('investments.txt', 'a') as file:
        file.write(f'{company_name.title()} | {investment_amount:.2f} | {int(profit_percent * 100)}% | {years} | {total_profit:.2f}\n')
        print('Data has been saved to investments.txt')
