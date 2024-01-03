# Magic Square.

square = []

while True:
    for i in range(9):
        while True:
            try:
                num = int(input(f'Enter the number of the square in [{i}] > '))
                square.append(num)
                break
            except ValueError:
                print("Please, enter a valid number")
    if(len(square) != len(set(square))):
        print('The numbers on your square must be unique, try again')
    else:
        break

def checkMagic():
    firstDiagonal = square[0] + square[4] + square[8]
    secondDiagonal = square[2] + square[4] + square[6]
    if(firstDiagonal == secondDiagonal):
        for i in [0, 1, 2]:
            sumLine, sumColumn = 0, 0
            for x in [0, 3, 6]:
                sumLine += square[i+x]
                sumColumn += square[i-x]
            if(sumLine != firstDiagonal or sumColumn != firstDiagonal):
                return f'The square {square} is not magical'
    return f'The square {square} is magical'      


print(checkMagic())
