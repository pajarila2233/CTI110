# This program calculates and displays travel expenses
# 19 February 2023
# CTI-110 PH1W2 - Travel Expenses
# Alberto Pajarilla

budget = float(input('Enter your budget: '))
destination = input('Enter your travel destination: ')
gas_cost = float(input('Enter the amount you will spend on gas: '))
accomodation_cost = float(input('Enter the amount you will spend on accomodation: '))
food_cost = float(input('Enter the amount you will spend on food: '))

total_expenses = gas_cost + accomodation_cost + food_cost
remaining_budget = budget - total_expenses

print('Your travel destination is:', destination)
print('Your total expenses are:', total_expenses)
print('Your remaining budget is:', remaining_budget)

                          
                          
