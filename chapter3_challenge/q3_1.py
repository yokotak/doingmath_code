import csv
import matplotlib.pyplot as plt

def read_csv(filename):

    with open(filename, encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        next(reader)
        next(reader)

        lol = []
        tier = []
        # x = []

        for row in reader:
            # x.append(row)
            lol.append(float(row[1]))
            tier.append(float(row[2]))
    # print(x)
    return lol, tier

def find_corr_x_y(x, y):
    nx = len(x)
    ny = len(y)

    if nx != ny:
        print("Error list length isn't equal")
        return False, 0
    #積の和を求める
    prod = []
    for xi, yi in zip(x, y):
        prod.append(xi*yi)
        sum_prod_x_y = sum(prod)
        sum_x = sum(x)
        sum_y = sum(y)
        squred_sum_x = sum_x**2
        squred_sum_y = sum_y**2
        x_squre = []
        for xi in x:
            x_squre.append(xi**2)

        # find the sum
        x_squre_sum =sum(x_squre)

        y_squre = []
        for yi in y:
            y_squre.append(yi**2)

        # find the sum
        y_squre_sum =sum(y_squre)

        #use formla to calculate correlation
        numerator = nx * sum_prod_x_y - sum_x * sum_y
        denominator_term1 = nx * x_squre_sum - squred_sum_x
        denominator_term2 = nx * y_squre_sum - squred_sum_y
        denominator = (denominator_term1 * denominator_term2) ** 0.5
        correlation = numerator / denominator

        return True, correlation
    
def scatter_plot(x, y):
    plt.scatter(x, y)
    plt.xlabel('Number')
    plt.ylabel('Square')
    plt.show()

if __name__ == '__main__':
    lol, tier = read_csv('lol_tier_relation.csv')
    x = [1]
    corr_flag, corr = find_corr_x_y(lol, x)
    if corr_flag:
        print('Highest correlation: {0}'.format(corr))
        scatter_plot(lol, tier)