# plt.plot(x, y, color='color name', linestyle='Line_Style', linewidth=value, marker='marker symbol', label='label name')

import matplotlib.pyplot as plt

months = [1,2,3,4]
sales = [1000, 1500, 1200, 1800]

plt.plot(months, sales, color='blue', linestyle='--', linewidth = 2, marker = 'o', label='2025 sales data')
plt.show()