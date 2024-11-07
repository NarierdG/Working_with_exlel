import pandas as pd
import plotly.graph_objects as go

df = pd.read_excel('output.xlsx')

temperature = df.iloc[:, 1:16]
humidity = df.iloc[:, 16:]

fig_temp = go.Figure()
for i in range(15):
    if i >= 10:
        fig_temp.add_trace(go.Scatter(
            x=temperature.index,
            y=temperature.iloc[:, i],
            mode='lines',
            name=f'Датчик {i+1}',
            line=dict(color='gray')
        ))
    else:
        fig_temp.add_trace(go.Scatter(
            x=temperature.index,
            y=temperature.iloc[:, i],
            mode='lines',
            name=f'Датчик {i+1}'
        ))

fig_temp.update_layout(title='Температура датчиков',
                       xaxis_title='Номер показания',
                       yaxis_title='Температура (°C)',
                       template='plotly_white')

fig_temp.show()

fig_humidity = go.Figure()
for i in range(15):
    if i >= 10:
        fig_humidity.add_trace(go.Scatter(
            x=humidity.index,
            y=humidity.iloc[:, i],
            mode='lines',
            name=f'Датчик {i+1}',
            line=dict(color='gray')
        ))
    else:
        fig_humidity.add_trace(go.Scatter(
            x=humidity.index,
            y=humidity.iloc[:, i],
            mode='lines',
            name=f'Датчик {i+1}'
        ))

fig_humidity.update_layout(title='Влажность датчиков',
                           xaxis_title='Номер показания',
                           yaxis_title='Влажность (%)',
                           template='plotly_white')

fig_humidity.show()

# Old version, open grafics in window

# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_excel('output.xlsx')
#
# temperature = df.iloc[:, 1:16]
# humidity = df.iloc[:, 16:]
#
#
# plt.figure(figsize=(12, 6))
# plt.title('Температура датчиков')
# plt.xlabel('Номер показания')
# plt.ylabel('Температура (°C)')
#
# for i in range(15):
#   plt.plot(temperature.iloc[:, i], label=f'Датчик {i+1}')
#
# plt.legend()
# plt.grid(True)
#
# plt.figure(figsize=(12, 6))
# plt.title('Влажность датчиков')
# plt.xlabel('Номер показания')
# plt.ylabel('Влажность (%)')
#
# for i in range(15):
#   plt.plot(humidity.iloc[:, i], label=f'Датчик {i+1}')
#
# plt.legend()
# plt.grid(True)
#
# plt.show()