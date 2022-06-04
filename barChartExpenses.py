from matplotlib import pyplot as plt


def draw_expenses(category, expenses):
    



if __name__ == '__main__':
    try:
        no = int(input('How many categories: '))
        categories = []
        expenses = []
        legend = []
        for i in range(1, no+1):
            cat = input(f'Enter category {i}: ')
            exp = float(input(f'Enter expenses for category {i}: '))
            categories.append(cat)
            expenses.append(exp)
            legend.append(cat)
    except ValueError:
        print('You entered an invalid input')

    else:
        for i in range(len(categories))
        draw_expenses(categories[i], expenses[i])
    plt.show()
