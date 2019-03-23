# Problem 96
f = open('p096_sudoku.txt','r')
sudoku_file = f.read()

lines = sudoku_file.split('\n')
sudoku = []

li = [x for i,x in enumerate(lines) if i % 10] # kein "Grid" mehr
ziffs = [str(x) for x in range(1,10)]
sudoku = [li[i:i+9] for i in range(0,len(li),9)]
sudoku = [[list(line) for line in sud] for sud in sudoku]

# sudoku[nummer des sudokus][Zeile][Stelle]

for sud in sudoku:
    def nachbarn_zeile(zeile):
        return [elem for elem in sud[zeile] if elem is not '0']

    def nachbarn_spalte(spalte):
        return [satz[spalte] for satz in sud if satz[spalte] is not '0']

    def nachbarn_quadrat(zeile,spalte):
        zeile = zeile // 3
        spalte = spalte // 3
        return [elem for elem in [satz[spalte:spalte+3] for satz in sud[zeile:zeile+3]] if elem is not '0']

    def finde_moeg(zeile,spalte):
        zeil = nachbarn_zeile(zeile)
        spal = nachbarn_spalte(spalte)
        quad = nachbarn_quadrat(zeile,spalte)
        return [ziff for ziff in ziffs if ziff not in zeil and ziff not in spal and ziff not in quad]


    ungeloeste = [(zeile,spalte,finde_moeg(zeile,spalte)) for zeile,satz in enumerate(sud) for spalte,stelle in enumerate(satz) if stelle == '0']
    while len(ungeloeste):
        for i,ungeloest in enumerate(ungeloeste):
