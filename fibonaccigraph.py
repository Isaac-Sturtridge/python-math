from matplotlib import pyplot as plt
import math

def draw_graph(x,y):
    plt.plot(x,y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Fibonacci ratio')

def fibo(n):
    if n == 1:
        return[1]
    if n == 2:
        return [1,1]
    # n > 2
    a = 1
    b = 1
    series = [a,b]
    for i in range(n):
        c = a+b
        series.append(c)
        a = b
        b = c

    return series


if __name__ == '__main__':
    try:
        n = int(input('How many numbers: '))
        fib_n = fibo(n)
        ratios = [1]
        for i in range(1, len(fib_n)):
            if fib_n[i] != fib_n[-1]:
                ratio = fib_n[i+1]/fib_n[i]
                ratios.append(ratio)
            else:
                ratio = (fib_n[i] + fib_n[i-1])/fib_n[i]
                ratios.append(ratio)

    except ValueError:
        print('Value Error')

    else:
        draw_graph(fib_n, ratios)
        plt.show()
