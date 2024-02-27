import math

def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))
        numbers.sort()
        print(numbers[13])
    return numbers

def calc_quantile(numbers, quantile_num):
    i = (len(numbers)*quantile_num)/100 + 0.5
    print(i)
    if i.is_integer():
        quantile = numbers[int(i)]
    else:
        k, f = math.modf(i)
        quantile = (1-f)*numbers[k] + f*numbers[k+1]

    return quantile

if __name__ == "__main__":
    data = read_data("marks.txt")
    quantile_num = float(input("please input quantile num:"))
    quantile = calc_quantile(data, quantile_num)
    print("quantile ({0}) = {1}".format(quantile_num, quantile))