'''
Generate equally spaced floating point numbers between two given values
'''
def frage(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment

    return numbers

'''
Draw the trajectory of a body in projectile motion
'''
from matplotlib import pyplot as plt
import math

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')

def frange(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval
    return numbers

def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8
    # Time of flight
    t_flight = 2*u*math.sin(theta)/g
    # find time intervals
    intervals = frange(0, t_flight, 0.001)
    # list of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
        draw_graph(x, y)

if __name__ == "__main__":
    # try:
    #     u = float(input('Enter the initial velocity (m/s):'))
    #     theta = float(input('Enter the angle of projection (degree):'))
    # except ValueError:
    #     print('You enterd an invalid input')
    # else:
    #     draw_trajectory(u, theta)
    #     plt.show()

    # list of three different initial velocity
    # u_list = [20, 40, 60]
    # theta = 45
    # for u in u_list:
    #     draw_trajectory(u, theta)

    num_trajectories = int(input('How many trajectories?: '))
    # degree_list = [0]*num_trajectories
    # velocity_list = [0]*num_trajectories
    legend_list = []

    for ti in range(num_trajectories):
        # degree_list[ti] = int(input('Enter the initial velocity for trajectory 1 (m/s): ', ti+1))
        # velocity_list[ti] = int(input('Enter the angle of projection for trajectory $d (degree): ', ti+1))
        u = int(input('Enter the initial velocity for trajectory {0} (m/s): '.format(ti+1)))
        theta = int(input('Enter the angle of projection for trajectory %d (degree): '.format(ti+1)))
        legend_list.append(str(u))
        draw_trajectory(u, theta)

    # Add a legend and show the graph
    plt.legend(legend_list)
    plt.show()