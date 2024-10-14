import numpy as np
from tabulate import tabulate


def setAccuracy(eps : float):
    acc = eps
    i = 0

    while acc < 1:
        acc *= 10
        i += 1
    
    return i


def matrixConversion(A : np.ndarray, B : np.ndarray):
    for i in range(len(A)):
        B[i] /= A[i][i]

        for j in range(len(A)):
            A[i][j] /= A[i][i] * -1 if i != j else 1

        A[i][i] = 0
    
    return A, B


def relaxationMethod(A : np.ndarray, B : np.ndarray, eps : float, acc : int):
    x = np.zeros(len(A))
    xx = np.zeros(len(A))
    R = np.copy(B)

    iterations = 0
    
    for i in range(len(A)):
        R[i] = R[i] - x[i] + sum([A[i][j] * x[j] for j in range(len(A)) if i != j])
    
    table = [['k', 'x1', 'x2', 'x3', 'x4', 'R1', 'R2', 'R3', 'R4'], 
            [iterations, 
            round(x[0], acc + 1), 
            round(x[1], acc + 1), 
            round(x[2], acc + 1), 
            round(x[3], acc + 1), 
            round(R[0], acc + 1), 
            round(R[1], acc + 1), 
            round(R[2], acc + 1),
            round(R[3], acc + 1)]]
    
    x = list([R[i] if R[i] == max(R, key=abs) else 0 for i in range(len(R))])
    xx[x.index(max(x, key=abs))] += max(R, key=abs)
    
    while any([abs(i) > eps for i in R]):
        for i in range(len(A)):
            R[i] = R[i] - x[i] + sum([A[i][j] * x[j] for j in range(len(A)) if i != j])
        
        iterations += 1
        table.append([iterations,
                    round(xx[0], acc + 1), 
                    round(xx[1], acc + 1), 
                    round(xx[2], acc + 1),
                    round(xx[3], acc + 1),
                    round(R[0], acc + 1),
                    round(R[1], acc + 1), 
                    round(R[2], acc + 1), 
                    round(R[3], acc + 1)])
                    
        x = list([R[i] if R[i] == max(R, key=abs) else 0 for i in range(len(R))])
        xx[x.index(max(x, key=abs))] += max(R, key=abs)
    
    x = list([R[i] if R[i] == max(R, key=abs) else 0 for i in range(len(R))])
    xx[x.index(max(x, key=abs))] += max(R, key=abs)

    iterations += 1
    table.append([iterations,
                round(xx[0], acc + 1), 
                round(xx[1], acc + 1), 
                round(xx[2], acc + 1),
                round(xx[3], acc + 1)])

    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    return xx


def main():
    A = np.array(
    [
        [2.958, 0.147, 0.354, 0.238],
        [0.127,	2.395, 0.256, 0.237],
        [0.403, 0.184, 3.815, 0.416],
        [0.259, 0.361, 0.281, 3.736],
    ]
)

    B = np.array([0.651, 0.898, 0.595, 0.389])

    eps = pow(10, -3)

    A, B = matrixConversion(A, B)
    acc = setAccuracy(eps)

    xx = relaxationMethod(A, B, eps, acc)

    print(f'x = ({str([round(x, acc) for x in xx])[1:-1]})')


main()