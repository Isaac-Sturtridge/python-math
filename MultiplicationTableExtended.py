# multiplication table


# enter as floats to allow float and integer input without error
table = float(input('Enter a number: '))
index = float(input('Enter the number of multiplications to display: '))

def multi_table(table):
    for i in range(1, int(index) + 1):
         print('{0} x {1} = {2}'.format(table, i, table*i))

if index.is_integer() == False:
    print("Please enter an integer when choosing how many to display")

else:
    # converts table to integer if applicable to make it look nicer
    if table.is_integer() == True:
        table = int(table)
    index = int(index)
    multi_table(table) 

