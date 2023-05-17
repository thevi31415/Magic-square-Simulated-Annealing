import matplotlib.pyplot as plt
import numpy as np
from simulated_annealing import simulated_annealing
from magic_square import magic_square

def is_magic_square(square):
    n = len(square)
    # Tính tổng của hàng, cột và đường chéo chính đầu tiên
    magic_sum = sum(square[0])
    # Kiểm tra các hàng
    for row in square:
        if sum(row) != magic_sum:
            return 0
    # Kiểm tra các cột
    for col in range(n):
        if sum(square[row][col] for row in range(n)) != magic_sum:
            return 0
    # Kiểm tra đường chéo chính thứ 1
    if sum(square[row][row] for row in range(n)) != magic_sum:
        return 0
    # Kiểm tra đường chéo chính thứ 2
    if sum(square[row][n-row-1] for row in range(n)) != magic_sum:
        return 0
    # Nếu tất cả các điều kiện đều đúng, trả về 1
    return 1


def plot_matrix(matrix):
    fig, ax = plt.subplots()
    ax.imshow(matrix, cmap=plt.cm.Blues, interpolation='nearest')
    ax.set_xticks(np.arange(matrix.shape[1]))
    ax.set_yticks(np.arange(matrix.shape[0]))
    ax.set_xticklabels(np.arange(1, matrix.shape[1]+1))
    ax.set_yticklabels(np.arange(1, matrix.shape[0]+1))
    ax.set_xlabel('Columns')
    ax.set_ylabel('Rows')
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            text = ax.text(j, i, matrix[i, j], ha='center', va='center', color='black')
    plt.show()


if __name__ == "__main__":
    # khai báo kích thước ma trận
    n = 3
    i=1
    magic_square_problem = magic_square(n)
    schedule = [1000 / t for t in range(1, 20001)]
    solver = simulated_annealing(magic_square_problem, schedule)
    solution = solver.solve()

    # Reformat the solution state as a square matrix
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = solution.state[i*n+j]
    if is_magic_square(matrix)==0:
        print("Retry!")
    #Lặp lại cho đến khi tìm ra được magic square
    while is_magic_square(matrix)==0 and i < 5 :
        magic_square_problem = magic_square(n)
        schedule = [1000 / t for t in range(1, 20001)]
        solver = simulated_annealing(magic_square_problem, schedule)
        solution = solver.solve()

        matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = solution.state[i*n+j]
        i+=1
        if is_magic_square(matrix)==0:
            print("Retry!")

    # In ma trận

    for row in matrix:
        print(row)
    if is_magic_square(matrix):
        print("This is Magic Square")
        new_matrix = np.array(matrix)
        plot_matrix(new_matrix)
    else:
        print("This isn't Magic Square")
        new_matrix = np.array(matrix)
        plot_matrix(new_matrix)