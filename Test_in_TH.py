import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('output.xlsx')

temperature = df.iloc[:, 1:16]
humidity = df.iloc[:, 16:]


plt.figure(figsize=(12, 6))
plt.title('Температура датчиков')
plt.xlabel('Номер показания')
plt.ylabel('Температура (°C)')

for i in range(15):
  plt.plot(temperature.iloc[:, i], label=f'Датчик {i+1}')

plt.legend()
plt.grid(True)

plt.figure(figsize=(12, 6))
plt.title('Влажность датчиков')
plt.xlabel('Номер показания')
plt.ylabel('Влажность (%)')

for i in range(15):
  plt.plot(humidity.iloc[:, i], label=f'Датчик {i+1}')

plt.legend()
plt.grid(True)