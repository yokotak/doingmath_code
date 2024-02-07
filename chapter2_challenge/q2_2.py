import matplotlib.pyplot as plt
'''
2次関数電卓
'''
def quadratic_function():
    # xの値
    x_value = []
    for xi in range(-300, 301):
        x_value.append(xi)
    
    y_value = []
    for x in x_value:
        #2次関数の値を計算
        #function
        y = x**2 + 2*x + 1
        # print('x = {0} y = {1}'.format(x, y))
        y_value.append(y)
    return x_value, y_value

def str_graph():
    x, y = quadratic_function()
    plt.plot(x, y)
    plt.ylim(0, 100000)
    plt.show()

if __name__ == "__main__":
    str_graph()