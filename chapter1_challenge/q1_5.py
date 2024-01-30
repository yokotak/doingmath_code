from fractions import Fraction
import re

def add(a, b):
    print('Result of Addition: {0}'.format(a+b))

def sub(a, b):
    print('Result of Subtract: {0}'.format(a-b))
    
def div(a, b):
    print('Result of Subtract: {0}'.format(a*b))
    
def multi(a, b):
    print('Result of Subtract: {0}'.format(a/b))

if __name__ == '__main__':
    while True:
            
        try:
            a = Fraction(input('Enter first fraction:'))
            b = Fraction(input('Enter second fraction:'))
            while True:
                op = input('Operation to perform -Add, Subtract, Divide, Multiply:')
                if re.match('add', op, re.IGNORECASE) != None:
                    add(a, b)
                if re.match('sub', op, re.IGNORECASE) != None:
                    sub(a, b)
                if re.match('div', op, re.IGNORECASE) != None:
                    div(a, b)
                if re.match('multi', op, re.IGNORECASE) != None:
                    multi(a, b)
                op = input('continue operation to perform?(y/n defaut n)')
                if op == 'y' or op == 'yes':
                    continue
                break
            op = input('re-enter fraction to perform?(y/n defaut n)')
            if op == 'y' or op == 'yes':
                continue
            break
        except ValueError:
            print('Invalid fraction entered')