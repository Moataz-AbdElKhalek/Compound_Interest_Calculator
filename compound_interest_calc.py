import pandas as pd

initial_investment = float(input("Enter your initial investment value: "))
interest_rate = float(input("Enter the estimated annual interest rate (%): "))/100
number_of_years = int(input("Enter the number of years that you plan to invest: "))

# To make a table of investment years
investment_values = pd.DataFrame({'year': range(1, number_of_years+1)})

# Compound Interest Rate = Initial_Investment_Value x (1+Interest_Rate)^(Number_of_Years) >> Simple math!
investment_values['compound_value'] = initial_investment * ((1+interest_rate)**investment_values['year'])

print(investment_values)

print(f'\nTotal money at {interest_rate}% in {number_of_years} years is:  ', round(investment_values.at[number_of_years-1,'compound_value'] , 2) )

# Plot the line

graph = input("Do you want to graph output? (Y,N): ")
if graph == 'Y' or graph == 'y' or graph == 'Yes' or graph == 'yes':

    from matplotlib import pyplot as plt
    plt.plot(investment_values.year, investment_values.compound_value, color="green")
    plt.xlabel('Year')
    plt.ylabel('Compound Value')
    plt.show()

print('\nThanks for using the Compound Interest Rate Calculator!\n')
