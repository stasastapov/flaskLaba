import numpy as np


def matrixToString(M):
    s = '\n'.join([''.join([str(u) for u in row]) for row in M])
    return (s.replace('[', '')).replace(']', '').replace('\n', ';')


def matrixReverse(data):  # обратная матрицу
    try:
        return matrixToString((np.linalg.inv(np.matrix(data).T)))
    except:
        return 'Fail'


def arraySum(data):  # сумма элементов массива
    M = data.split(' ')
    return np.sum(M, dtype=float)


def matrixTransponse(M):  # транспонированная матрица
    return matrixToString(np.matrix(M).T)


def convert_to_quaternery(num: str):
    num_for_convert = int(num)
    if num_for_convert == 0:
        return 0
    quaternery_number = ''
    while num_for_convert > 0:
        remainer = num_for_convert % 4
        quaternery_number = str(remainer) + quaternery_number
        num_for_convert //= 4
    return quaternery_number

def removing_vowels(data: str):
    vowels = "aeiouyAEIOUYаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    for vowel in vowels:
        data = data.replace(vowel, "")
    return data

def sort_data(data: list):
    sorted_data = sorted(data)
    return sorted_data


def MatrixToList(matrix):
    ListMatrix = []

    matrix = matrix.split('; ', 2)

    for i in range(0, 2):
        matrix[i] = matrix[i].split(' ')

    ListMatrix += matrix

    for i in range(0, 2):
        for j in range(0, 2):
            ListMatrix[i][j] = int(ListMatrix[i][j])  # Elm's Mat From Str To Int

    return ListMatrix

def matrix_multiplication(matrix1, matrix2):
    matrix1 = MatrixToList(matrix1)
    matrix2 = MatrixToList(matrix2)

    result = []
    if len(matrix1[0]) != len(matrix2):
        return "Невозможно умножить матрицы: неправильные размеры"
    for i in range(len(matrix1)):
        row_result = []
        for j in range(len(matrix2[0])):
            element_sum = 0
            for k in range(len(matrix2)):
                element_sum += matrix1[i][k] * matrix2[k][j]
            row_result.append(element_sum)
        result.append(row_result)
    return result