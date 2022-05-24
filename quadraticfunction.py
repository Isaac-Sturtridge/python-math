'''
Quadratic function calculator
'''
import matplotlib.pyplot as plt

# Assume values of x
x_values = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values = []
for x in x_values:
    # calculate value
    y = x**2 + 2*x + 1
    print('x={0} y={1}'.format(x, y))
    y_values.append(y)

plt.plot(x_values,y_values, marker='o')
plt.title('Quadratic Function')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
