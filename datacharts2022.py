import pandas as pd
import matplotlib.pyplot as plt

def createVisual(x_Cord, y_Cord, x_Label, y_Label, title):
    plt.bar(x_Cord, y_Cord)
    plt.gcf().set_size_inches(8, 4)
    plt.xlabel(x_Label)
    plt.ylabel(y_Label)
    plt.title(title)
    plt.show()
  

df_old = pd.read_csv('New_United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv')

df_new = pd.DataFrame()

df_new['maxCase'] = df_old.groupby(['state'])['conf_cases'].max()
df_new['maxDeath'] = df_old.groupby(['state'])['conf_death'].max()

df_new.to_csv('Final_United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv')

states = []
states = df_new.index

createVisual(states, df_new['maxCase'], 'States', 'Confirmed Reported Cases(millions)', 
             'COVID-19 Cases per State (that chose to report)')
createVisual(states, df_new['maxDeath'], 'States', 'Confirmed Reported Deaths', 
             'COVID-19 Deaths per State (that chose to report)')
