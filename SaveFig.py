# savefig('filename.extension' , dpi = value, bbox_inches = 'tighti)
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]
plt.plot(x,y,color='blue', marker='o')
plt.title('Simple Line Plot')
plt.xlabel('X Axios')
plt.ylabel('Y Axios')

plt.savefig('line_plot.png', dpi=300, bbox_inches='tight')
plt.show()