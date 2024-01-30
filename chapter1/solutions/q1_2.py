def multi_table(a, b):
    for i in range(1, b):
        print('{0} x {1} = {2}'.format(a, i, a*i))

if __name__ == '__main__':
    a = float(input('enter use num:'))
    b = int(input('enter range:'))
    multi_table(a, b)