import plotly.express as px
import pandas as pd
from flask import Flask

spotify = pd.read_csv('spotify.csv')

data = {
    'X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Y': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    'Category': ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E'],
    'Size': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}
df = pd.DataFrame(data)

fig = px.scatter(df, x='X', y='Y', color='Category', size='Size', symbol='Category',
                 title='Gráfico de Dispersão Personalizado',
                 labels={'X': 'Eixo X', 'Y': 'Eixo Y'})
fig.show()
