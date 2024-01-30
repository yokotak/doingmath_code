def even_odd(num):
    if not num.is_integer():
        print('error: Please input integer.')
        return False
    
    if num % 2 == 0:
        print('num is even.')
        for i in range(1, 10):
            print(int(num + (i*2)), end=" ")
        return True
        
    print('num is odd.')
    for i in range(1, 10):
        print(int(num + (i*2)), end=" ")
    return True
    
if __name__ == '__main__':
    while(True):
        num = float(input('Please imput num:'))
        if not even_odd(num):
            continue_flag = input('Do you want to re-enter?(y/n)')
            if continue_flag == 'y':
                continue
        break