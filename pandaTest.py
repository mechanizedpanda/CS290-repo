import pandas as pd

df = pd.read_csv('survey_results_public.csv')
print(df.tail(11))

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)



schema_df = pd.read_csv('survey_results_schema.csv')

