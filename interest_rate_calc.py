from matplotlib import pyplot as plt
import pandas as pd
initial = 1000
interest = .15
ir = pd.DataFrame ({'year': range(1, 21)})

ir['final'] = initial * ((1+interest)**ir['year'])

print (ir)

# Plot the line
# %matplotlib inline
plt.plot(ir.year, ir.final, color="green")
plt.xlabel('Year')
plt.ylabel('Final')
plt.show()
