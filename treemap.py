import pandas as pd
import plotly.express as px

df = pd.read_csv("Results_21Mar2022_Edited.csv")

fig = px.treemap(df, 
                 path=['diet_group', 'sex', 'age_group'],  
                 values='n_participants',
                 color='total_gwp', 
                 color_continuous_scale='RdYlGn_r',
                 title="Environmental Impact by Diet Group",
                 labels={'diet_group': 'Diet Type', 
                         'sex': 'Gender', 
                         'age_group': 'Age Category', 
                         'n_participants': 'Number of People',
                         'total_gwp': 'Total GWP (kg CO₂e)'})

fig.show()
