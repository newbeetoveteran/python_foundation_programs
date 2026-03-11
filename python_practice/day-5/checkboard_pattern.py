# printing a checkboard using "#" and "*"

check_board = 4
whites = "#"
blacks = "*"

for i in range(check_board):
    row = " "
    for j in range(check_board):
        if (i + j) % 2 == 0:
            row += whites
        else:
            row += blacks
    print(row)