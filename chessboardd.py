
def print_chessboard(size):
    for row in range(size):
        line = ""
        for col in range(size):
            if (row + col) % 2 == 0:
                line += "X "
            else:
                line += "O "
        print(line.strip())

print(print_chessboard(8))