def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("Matrix is empty")
        return

    rows = len(matrix)
    cols = len(matrix[0])

   
    column_widths = [max(len(str(matrix[i][j])) for i in range(rows)) for j in range(cols)]

    for i in range(rows):
        for j in range(cols):
           
            print("{:>{width}}".format(matrix[i][j], width=column_widths[j]), end=" ")
        print()

matrix = [
    [1, 22, 333],
    [4444, 55555, 666666],
    [7777777, 88888888, 999999999]
]

print_matrix_integer(matrix)
