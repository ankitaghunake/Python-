import matplotlib .pyplot as plt
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x, y)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Simple Line Plot')
plt.xlim(0, 6)
plt.ylim(0,12)
plt.show()
plt.grid()
plt.legend()
plt.savefig('simple_line_plot.png')
