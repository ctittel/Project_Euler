class Sudoku:
    def __init__(self,lines):
        self.numbers = 

sudokus = []

with open("p096_sudoku.txt") as file:
    counter = 0
    lines = []
    for line in file:
        if counter:
            lines.append(str.replace(line,"\n",""))
        counter += 1
        if counter == 10:
            sudokus.append(Sudoku(lines))
            print(lines)
            lines = []
            counter = 0
