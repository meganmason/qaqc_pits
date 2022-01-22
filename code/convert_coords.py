import datetime
import glob
import os
import shutil
import numpy as np
import pandas as pd
import utm
# from pyproj import Proj, transform
from csv import writer
import textwrap

# bring in data
fname = '../coords.csv'
df = pd.read_csv(fname)

#
lat_list = []
lon_list = []

for i, row in df.iterrows():
    lat, lon = utm.to_latlon(row.UTME, row.UTMN, row.UTMzone, "Northern")
    lat_list.append(lat)
    lon_list.append(lon)

df['Latitude']  = lat_list
df['Longitude'] = lon_list

df = df[['Unnamed: 0', 'Date', 'Location', 'Site', 'PitID', 'Latitude', 'Longitude', 'UTME', 'UTMN',
       'UTMzone']]

df.to_csv('../coords_latlon.csv', sep=',', header=True)

print('done!')
