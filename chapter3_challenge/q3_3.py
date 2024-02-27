import matplotlib.pyplot as plt
from stats import mean, median, mode, variance_sd
import csv


# csvファイルを読み込み
# データを日付と人口のリストに入れていく
def read_csv(filename):

    with open(filename, encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        date = []
        population = []
        # x = []

        for row in reader:
            # x.append(row)
            year = str(row[0][0:4])
            date.append(year)
            population.append(float(row[1]))
    # print(x)
    return date, population

# 数値データの差異の計算したリスト
def difference_calc(data):
    differences = []
    for id in range(len(data)- 2):
         difference = data[len(data) -2 -id]-data[len(data) -1 -id]
         differences.append(difference)
    print(differences)
    return differences

# 文字データを差異に合わせた合成リスト
def diffenrence_str(data):
    differences = []
    for id in range(len(data) - 2):
        difference = data[len(data) -1 -id] + "-" + data[len(data) -2 -id]
        differences.append(difference)
    print(differences)
    return differences

def create_char(data1, data2):
    plt.plot(data1, data2)
    plt.xticks(rotation=45)
    plt.show()

if __name__=='__main__':
    date, population = read_csv('USA_SP_POP_TOTL.csv')
    difference_y = diffenrence_str(date)
    difference_p = difference_calc(population)
    m = mean(difference_p)
    median = median(difference_p)
    mode = mode(difference_p)
    variance, sd = variance_sd(difference_p)
    print('Mean: {0:.5f}'.format(m))
    print('Median: {0:.5f}'.format(median))
    print('Mode: {0:.5f}'.format(mode))
    print('Variance: {0:.5f}'.format(variance))
    print('Standard deviation: {0:.5f}'.format(sd))
    create_char(difference_y, difference_p)