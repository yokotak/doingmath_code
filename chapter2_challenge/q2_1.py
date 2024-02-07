import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
import pandas as pd
import datetime

def list_load():
    date = []
    Himeji_t = []
    Akashi_t = []
    Kobe_t = []
    with open ('data_2.csv', 'r') as temp_f:
        reader = csv.reader(temp_f)
        # for row in reader:
        #     print(row)
        for row_i in reader:
            date.append(row_i[0])
            Himeji_t.append(float(row_i[1]))
            Akashi_t.append(float(row_i[4]))
            Kobe_t.append(float(row_i[7]))
        
        date_x = [dx.replace('/', '-') for dx in date]
        date_xx = [datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S') for s in date_x]
        date_z = [datetime.datetime.strptime(s, '%Y/%m/%d %H:%M:%S') for s in date]

    return date_z, Himeji_t, Akashi_t, Kobe_t

def str_graph():
    date, Himeji, Akashi, Kobe = list_load()
    fig, ax = plt.subplots()
    ax.plot(date, Himeji, date, Akashi, date, Kobe)
    plt.ylim(-5, 20)
    plt.xticks(rotation=20)
    ax.legend(['Himeji', 'Akashi', 'Kobe'])
    dates = mdates.HourLocator(range(0, 24, 8))
    dates_fmt = mdates.DateFormatter('%m/%d %H:%M')
    ax.xaxis.set_major_locator(dates)
    ax.xaxis.set_major_formatter(dates_fmt)

    plt.show()

if __name__ == "__main__":
    str_graph()