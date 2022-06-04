'''
Draw the trajectory of a body in projectile motion
'''

from matplotlib import pyplot as plt
import math

def frange(start, final, interval):

    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval

    return numbers

def draw_graph(x,y):
    plt.plot(x,y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')

def draw_trajectory(u, theta):

    theta = math.radians(theta)
    g = 9.8

    # Time of flight
    t_flight = 2*u*math.sin(theta)/g
    print('Time of flight: ' + str(round(t_flight, 3)) + ' seconds')
    # Find time intervals
    intervals = frange(0, t_flight, 0.001)


    # List of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)

    print('Max distance: '+ str(round(max(x), 3)) + ' metres')
    print('Max height: ' + str(round(max(y), 3)) + ' metres')
    draw_graph(x,y)

if __name__ == '__main__':
    try:
        no = int(input('How many trajectories: '))
        u_values = []
        theta_values = []
        legend = []
        for i in range(1, no + 1):
            u = float(input(f'Enter the initial velocity for trajectory {i} (m/s): '))
            theta = float(input(f'Enter the angle of projection for trajectory {i} (degrees): '))
            u_values.append(u)
            theta_values.append(theta)
            legend.append(f'trajectory {i}')
        
    except ValueError:
        print('You entered an invalid input')

    except no > 10:
        print('Too many trajectories')

    else:
        for i in range(len(u_values)):
            print(f'Stats for trajectory {i+1}: ')
            draw_trajectory(u_values[i], theta_values[i])
            plt.legend(legend)
        plt.show()    
