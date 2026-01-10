import matplotlib.pyplot as plt

x = ["Mon", "Tues", "Wed", "Thur", "Fri"] # x-axis
y = [10,15,7,20,12] # y-axis

plt.plot(x,y)

plt.title('Bakery Sales this Week!')

plt.xlabel('Day of the week')
plt.ylabel('Sales Per Day')

plt.show()