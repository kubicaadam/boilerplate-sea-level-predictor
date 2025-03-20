import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot

    plt.subplots(1, 1, figsize=(10, 5))
    
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    plt.scatter(x, y)

    # Create first line of best fit

    slope1, yintercept1, r1, p1, se1 = linregress(x, y)

    x1 = [x.min(), 2050]
    y1 = [x1[0] * slope1 + yintercept1, x1[1] * slope1 + yintercept1]

    plt.plot(x1, y1)

    # Create second line of best fit

    df2000 = df.loc[df["Year"] >= 2000]
    x2000 = df2000["Year"]
    y2000 = df2000["CSIRO Adjusted Sea Level"]

    slope2, yintercept2, r2, p2, se2 = linregress(x2000, y2000)

    x2 = [x2000.min(), 2050]
    y2 = [x2[0] * slope2 + yintercept2, x2[1] * slope2 + yintercept2]

    plt.plot(x2, y2)

    # Add labels and title

    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()