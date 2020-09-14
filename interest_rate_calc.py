import pandas as pd

initial = float(input("Enter your initial saving value >> "))
interest = float(input("Enter the current interest rate >> "))
years = int(input("Enter the number of years >> "))
ir = pd.DataFrame ({'year': range(1, years+1)})

ir['final'] = initial * ((1+interest)**ir['year'])

print (ir)

print ('\nTotal Money Gained at the End of Period >> ', round(ir.at[years-1,'final']-initial , 2) )

# Plot the line

graph = input("Do you want to graph output? (Y,N) >> ")
if graph == 'Y' or graph == 'y' or graph == 'Yes' or graph == 'yes':

    from matplotlib import pyplot as plt
    plt.plot(ir.year, ir.final, color="green")
    plt.xlabel('Year')
    plt.ylabel('Final')
    plt.show()

print('\nThanks for using the Interest Rate Calculator!\n')
