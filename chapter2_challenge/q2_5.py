import matplotlib.pyplot as plt

def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    # n > 2
    a = 1
    b = 1
    #first two members of the series 
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b 
        b = c

    return series

def plot_moment(n):
    series = fibo(n)
    conse_series = []
    for si in range(len(series)-1):
        conse = series[si+1]/series[si]
        conse_series.append(conse)
    plt.plot(conse_series)
    plt.xlim([0, n])
    plt.ylim([1, 2.2])
    plt.grid()
    plt.show()

if __name__ == '__main__':
    num_for_fib = int(input('Please enter fibonacci num:'))
    plot_moment(num_for_fib)