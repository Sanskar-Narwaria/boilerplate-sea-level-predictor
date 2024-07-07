import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')
    

    # Create scatter plot
    fig,ax=plt.subplots(figsize=(10,10))
    ax.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    res1 = stats.linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    y1=res1.intercept + res1.slope*df['Year']
    x1=np.arange(1880,2051,1)
    y1=list(res1.intercept + res1.slope*x1)
    ax.plot(x1,y1,'r',label='First Line')
    


    # Create second line of best fit
    df_filtered=df[df['Year']>=2000]
    res2=stats.linregress(df_filtered['Year'],df_filtered['CSIRO Adjusted Sea Level'])
    x2=np.arange(2000,2051,1)
    y2=list(res2.intercept + res2.slope*x2)
    ax.plot(x2,y2,'g',label='Second Line')


    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()