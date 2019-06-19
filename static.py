def create_false_boolmatrix(h, w):
    boolmatrix = list()
    for i in range(h):
        row = list()
        for j in range(w):
            row.append(False)
        boolmatrix.append(row)
    return boolmatrix


def iteration_true_in_boolmatrix(boolmatrix):
    count = 0
    for i in range(len(boolmatrix)):
        for j in range(len(boolmatrix[i])):
            if boolmatrix[i][j] == True:
                count += 1
    return count


def try_search_neighbor(matrix, boolmatrix, i, j):
    if boolmatrix[i][j] == True:
        return boolmatrix
    else:
        boolmatrix[i][j] = True
        neighbor = list()
        if j < len(matrix[i]) - 1:
            if matrix[i][j] == matrix[i][j+1] and j+1 < len(matrix[i]):#справа
                if boolmatrix[i][j+1] == False:
                    neighbor.append((i, j+1))
        if matrix[i][j] == matrix[i][j-1] and j-1 >= 0:#слева
            if boolmatrix[i][j-1] == False:
                neighbor.append((i, j-1))
        if i < len(matrix) - 1:
            if matrix[i][j] == matrix[i+1][j] and i+1 < len(matrix):#снизу
                if boolmatrix[i+1][j] == False:
                    neighbor.append((i+1, j))
        if matrix[i][j] == matrix[i-1][j] and i-1 >= 0:#сверху
            if boolmatrix[i-1][j] == False:
                neighbor.append((i-1, j))
        if len(neighbor) > 0:
            for a in neighbor:
                boolmatrix = try_search_neighbor(matrix, boolmatrix, a[0], a[1])
        return boolmatrix


def matrix_neigbor(matrix):
    result = list()
    for i in range(len(matrix)):
        row = list()
        for j in range(len(matrix[i])):
            boolmatrix = create_false_boolmatrix(len(matrix), len(matrix[i]))
            boolmatrix = try_search_neighbor(matrix, boolmatrix, i, j)
            count = iteration_true_in_boolmatrix(boolmatrix)
            row.append(count)
        result.append(row)
    return result
