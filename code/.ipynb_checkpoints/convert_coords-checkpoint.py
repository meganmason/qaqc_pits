import datetime
import glob
import os
import shutil
import numpy as np
import pandas as pd
from pyproj import Proj, transform
from csv import writer
import textwrap

fname = '../coords.csv'
d = pd.read_csv(fname)

print(d)
