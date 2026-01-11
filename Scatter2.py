#plt.scatter(x,y, color='color_name' marker='marker style', label = 'label name')
import matplotlib.pyplot as plt

plt.scatter([1,2,3], [50,55,60], color='blue', label='Class A') #g1
plt.scatter([1,2,3], [45,50,52], color='orange', label='Class B') #g2

plt.xlabel('Hours studied')
plt.ylabel('Exam Score')
plt.title('Comparison of Two Classes')
plt.legend()
plt.grid(True)
plt.show()