#even-odd vending machine

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
    print("Here are the next ten even numbers: ", end="")
    for num in range(9):
        if num == 8:
            print(str(number) + ".")
        else:
            print(str(number) + ",", end=" ")
        number += 2

else:
    print(f"{number} is odd.")
    print("Here are the next ten odd numbers: ", end="")
    for num in range(9):
        if num == 8:
            print(str(number) + ".")
        else:
            print(str(number) +  ",", end=" ")
        number += 2
