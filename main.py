# This is a sample Python script.

import numpy as np
import pandas as pd
from scipy.constants import pi

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(np.array([1, 2, 3, 4]))
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)
    print(pi)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('SQUAD')
    print_hi('Emma')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
