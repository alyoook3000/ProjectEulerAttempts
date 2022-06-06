def BigGridP(filename):
    with open(filename, 'r') as f:
        rows = [[int(num) for num in line.split()] for line in f]

    greatest = 0
    diagonal_up = 0
    product = []
    for i in range(20):
        for j in range(20):
            if j + 3 < 20:
                across = rows[i][j] * rows[i][j + 1] * \
                        rows[i][j + 2] * rows[i][j + 3]
            if i + 3 < 20:
                down = rows[i][j] * rows[i + 1][j] * \
                       rows[i + 2][j] * rows[i + 3][j]
            if i + 3 < 20 and j + 3 < 20:
                diagonal_down = rows[i][j] * rows[i + 1][j + 1] * \
                            rows[i + 2][j + 2] * rows[i + 3][j + 3]
            if i - 3 >= 0 and j + 3 < 20:
                diagonal_up = rows[i][j] * rows[i - 1][j + 1] * \
                          rows[i - 2][j + 2] * rows[i - 3][j + 3]

            greatest = max(greatest, across, down, diagonal_down, diagonal_up)
    return(greatest)


print(BigGridP('gridchallengedata.txt'))