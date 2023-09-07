import pandas as pd 
import numpy as np


df_new = pd.read_csv('United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv')
print(df_new)

#drop columns that are guessed and not confirmed cases
df_new = df_new.drop(columns = ['tot_cases', 'prob_cases', 'pnew_case', 
    'tot_death', 'prob_death', 'pnew_death', 'consent_cases', 'consent_deaths', 'created_at'])
 
#sort data by submission date
df_new['submission_date'] = pd.to_datetime(df_new['submission_date'])
df_new = df_new.sort_values("submission_date")

#drop rows with zero values
columns = ['conf_cases', 'new_case', 'conf_death', 'new_death']
df_new = df_new.replace(0, np.nan).dropna(axis=0, how='any', subset=columns).fillna(0)

#add to new file
df_new.to_csv('New_United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv')