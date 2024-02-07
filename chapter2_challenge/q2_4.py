'''
水平棒グラフ
'''

import matplotlib.pyplot as plt
def create_bar_chart(data, labels):
    #number of bars
    num_bars =len(data)
    #　次のリストで各棒がy軸の中央に位置する[1, 2, 3...]となる
    positions = range(1, num_bars+1)
    plt.barh(positions, data, align='center')
    #棒ラベルの設定
    plt.yticks(positions, labels)
    plt.xlabel('Amount')
    plt.ylabel('Categories')
    plt.title('Weekly expenditures')
    #格子線の表示
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # #先週の歩数
    # steps = [6534, 7000, 8900, 10786, 3467, 11045, 5095]
    # #Correspinding days
    # labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

    # カテゴリー数の入力
    categories_num = int(input('Enter the num of categories: '))
    categories = []
    expenditures = []
    for ci in range(categories_num):
        category = input('Enter category: ')
        expenditure = int(input('Expenditure: '))
        categories.append(category)
        expenditures.append(expenditure)

    create_bar_chart(expenditures, categories)
