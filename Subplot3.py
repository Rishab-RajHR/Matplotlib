#plt.subplot(nrows, ncols, index)

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]

# fig, ax = plt.subplots(nrows, ncols, figsize=(width, height))
fig, ax = plt.subplots(1, 2, figsize = (10, 5))

x = [1,2,3,4]
y = [10,20,15,25]

ax[0].plot(x,y,color='blue')
ax[0].set_title('Line Plot')

ax[1].bar(x,y,color='green')
ax[1].set_title('Bar Chart')

fig.suptitle('Comparison of Line and Bar Charts')

plt.tight_layout() # Automatic adjustment
plt.show()

