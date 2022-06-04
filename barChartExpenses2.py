
from matplotlib import pyplot as plt
import math


def draw_bar_chart(expenditure, category):
    # number of categories
    num_bars = len(category)
    #
    positions = range(1, num_bars+1)
    plt.barh(positions, expenditure, align="center")
    #labels
    plt.yticks(positions, category)
    plt.xlabel('Expenditure')
    plt.ylabel('category')
    plt.title('expenditure for different categories')
    plt.grid()
    plt.show()
    

if __name__ == '__main__':
    try:
        no = int(input('How many categories: '))
        categories = []
        expenditures = []
        for i in range(1, no + 1):
            cat = str(input('Enter category: '))
            exp = int(input('Expenditure: '))
            categories.append(cat)
            expenditures.append(exp)

    except ValueError:
        print('Invalid entry')

    else:
        draw_bar_chart(expenditures,categories)
