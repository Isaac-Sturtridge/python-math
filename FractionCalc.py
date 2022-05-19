'''
Fraction operations
'''

from fractions import Fraction

def add(a, b):
 print('Result of Addition: {0}'.format(a+b))

def subtract(a, b):
 print('Result of Subtraction: {0}'.format(a-b))

def multiply(a, b):
 print('Result of Multiplication: {0}'.format(a*b))

def divide(a, b):
 print('Result of Division: {0}'.format(a/b))
 
if __name__ == '__main__':
    while True:
        a = Fraction(input('Enter first fraction: '))
        b = Fraction(input('Enter second fraction: '))
        op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
        match op:
            case 'Add':
                add(a,b)
            case 'Subtract':
                subtract(a,b)
            case 'Multiply':
                multiply(a,b)
            case 'Divide' :
                divide(a,b)
                print(f'This is {a} divided by {b}. For the reverse, enter the second fraction first.')
     
        answer = input('Do you want to exit? Type \'y\' for yes ')
        if answer == 'y':
            break
