import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
from math import log10


def f(x):
    return 0.5 * np.exp((np.sqrt(x)) * -1) - 0.2 * np.sqrt(x ** 3) + 2


def plot_func():
    x = np.linspace(3, 6, 100)
    f = 0.5 * np.exp((np.sqrt(x)) * -1) - 0.2 * np.sqrt(x ** 3) + 2

    plt.figure()
    plt.plot(x, f)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title("Localization of the root of a nonlinear equation")
    plt.grid(True)

    plt.show()


def set_initial_approximation():
    while True:
        try:
            x0 = float(eval(input("\nEnter initial approximation x0: ")))
            x1 = float(eval(input("Enter initial approximation x1: ")))

            if f(x0) * f(x1) < 0:
                break
            else:
                print("The condition of the Bolzano-Cauchy theorem are not satisfied. Try again.")
            
        except Exception:
            print("Wrong input. Try again.")
    
    return x0, x1


def set_accuracy():
    while True:
        try:
            accuracy = float(eval(input("Enter the accuracy: ")))
            if 1 > accuracy and 0 < accuracy:
                break
            else:
                print("Incorrect accuracy.")
        except Exception:
            print("Incorrect accuracy.")
    
    return int(abs(log10(float(accuracy)))) + 1, accuracy


def chord_method(accuracy, x0, x1, num_of_decimal_places):
    iterations = 0

    f0 = f(x0)
    f1 = f(x1)

    dx = abs(x1 - x0)
    iterations += 1

    format_str = f"{{:.{num_of_decimal_places + 1}f}}"
    table = [
        ['k', 'x', 'f(x)', '|xk - xk-1|'],
        [iterations - 1, format_str.format(x0), format_str.format(f0), '-'],
        [iterations, format_str.format(x1), format_str.format(f1), format_str.format(dx)]
    ]

    while abs(dx) > accuracy:
        iterations += 1

        new_x = x0 - (f0 / (f1 - f0)) * (x1 - x0)
        dx = abs(new_x - x1)

        x0, x1 = x1, new_x
        f0, f1 = f(x0), f(x1)

        table.append([iterations, format_str.format(x1), format_str.format(f1), format_str.format(dx)])
    
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid', numalign='right'))
    return x1

        
def main():
    num_of_decimal_places, accuracy = set_accuracy()

    plot_func()

    x0, x1 = set_initial_approximation()

    root_of_equation = chord_method(accuracy, x0, x1, num_of_decimal_places)
    print(f"x = {round(root_of_equation, num_of_decimal_places)}")


main()