import matplotlib.pyplot as plt
# from pylab import plot, savefig

def create_graph():
    x_numbers=[1, 2, 3]
    y_numbers=[2, 4, 6]
    plt.plot(x_numbers, y_numbers)
    plt.savefig('mygraph.png')
    plt.show()

if __name__ == "__main__":
    create_graph()