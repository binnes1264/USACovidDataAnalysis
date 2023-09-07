import pandas as pd
import matplotlib.pyplot as plt

#create graph instance with characteristics
def createVisual(x_Cord, y_Cord, x_Label, y_Label, title):
    plt.bar(x_Cord, y_Cord)
    plt.gcf().set_size_inches(8, 4)
    plt.xlabel(x_Label)
    plt.ylabel(y_Label)
    plt.title(title)
    plt.show()
  
#open cleaned file
df_old = pd.read_csv('New_United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv')

#create file for final data
df_new = pd.DataFrame()

#create new columns with the max confirmed cases and deaths by state
df_new['maxCase'] = df_old.groupby(['state'])['conf_cases'].max()
df_new['maxDeath'] = df_old.groupby(['state'])['conf_death'].max()

#add calulated max values to final file
df_new.to_csv('Final_United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv')

#add state names to final file
states = []
states = df_new.index

#create graphs
createVisual(states, df_new['maxCase'], 'States', 'Confirmed Reported Cases(millions)', 
             'COVID-19 Cases per State (that chose to report)')
createVisual(states, df_new['maxDeath'], 'States', 'Confirmed Reported Deaths', 
             'COVID-19 Deaths per State (that chose to report)')
