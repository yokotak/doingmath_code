'''
The relationship between  gravitational force and distance between two bodies
'''
import matplotlib.pyplot as plt
# draw the graph
def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitational force in newtons')
    plt.title('Gravitational force and distance')
    plt.show()

def generate_F_r():
    # generate values for r
    r = range(100, 1001, 10)
    # empty list to store the calculated values of F
    F = []
    # constant, G
    G = 6.674*(10**-11)
    # two masses
    m1 = 0.5
    m2 = 1.5
    # calculate Force and add it to the list, F
    for dist in r:
        force = G*(m1*m2)/(dist**2)
        F.append(force)
    # call the draw_graph function
    draw_graph(r, F)

if __name__ == "__main__":
    generate_F_r()

