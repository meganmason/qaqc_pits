import datetime
import glob
import os
import shutil
import numpy as np
import pandas as pd
from pyproj import Proj, transform
from csv import writer
import textwrap


def some_function():
    a = str(2)
    b = 2*5
    c = 2 * np.random.randint(0,10)
    return a,b,c

# bar = [some_function() for i in range(5)]

data = []

for i in range(5):
    data.append(some_function())

df = pd.DataFrame(data, columns=['A', 'B', 'C'])

print(df)
