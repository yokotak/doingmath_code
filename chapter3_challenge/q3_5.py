
# ファイルを読み込み昇順に並び替える関数
def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))
        numbers.sort()
        print(numbers[13])
    return numbers

def create_classes(numbers, n):
    low = min(numbers)
    high = max(numbers)

    # width of each class
    width = (high - low)/n
    classes = []
    a = low
    b = low + width
    classes = []
    while a < (high-width):
        classes.append((a, b))
        a = b
        b = a + width
    # The last class may be of size
    # less than width
    classes.append((a, high+1))
    return classes

if __name__ == "__main__":
    data = read_data("marks.txt")
7