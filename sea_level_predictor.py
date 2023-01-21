import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
  fig , ax = plt.subplots(1, figsize = (12,6))
  ax.scatter(data = df, x = 'Year', y = 'CSIRO Adjusted Sea Level')

    # Create first line of best fit
  s = linregress(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
  ax.set_xlim(1850,2075)
  a = np.arange(1850,2050)
  ax.plot(a, s.slope*a+s.intercept, color='red', linestyle='--', linewidth=2)
    # Create second line of best fit
  new_df = df.loc[df['Year'] >=2000]
  s1 = linregress(x = new_df['Year'], y = new_df['CSIRO Adjusted Sea Level'])
  ax.plot(a, s1.slope*a+s1.intercept, color='steelblue', linestyle='--', linewidth=2)
    # Add labels and title
  ax.set_title('Rise in Sea Level')
  ax.set_xlabel('Year')
  ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()