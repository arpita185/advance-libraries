import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [22, 24, 19, 23, 25, 27, 21]

plt.figure(figsize=(10, 5))
plt.plot(days, temperatures, marker='o', linestyle='-', color='royalblue', label='Temperature (°C)')

plt.title('Weekly Temperature Overview')
plt.xlabel('Day of the Week')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.legend()

max_temp = max(temperatures)
max_day = days[temperatures.index(max_temp)]
plt.annotate(f'Max: {max_temp}°C', 
             xy=(max_day, max_temp), 
             xytext=(max_day, max_temp + 2),
             arrowprops=dict(facecolor='red', shrink=0.05),
             ha='center')


plt.tight_layout()
plt.show()

