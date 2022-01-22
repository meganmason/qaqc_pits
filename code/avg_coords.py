import datetime
import glob
import os
import shutil
import numpy as np
import pandas as pd

# ~~~~~~~~~ ideal steps
# 1 - bring in data
# 2 - list of outliers to remove
# 3 - mean location of snow pit study plot for time series
# 4 -  write to csv file
#~~~~~~~~~ end outline

# ~~~~~~ megan's way....clunky
# bring in data
fname = '../coords_latlon.csv'
df = pd.read_csv(fname)
df = df.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'])
df['Site'] = df['Site'].str.lower()
# df.to_csv('../test.csv', sep=',', header=True)

# list of outliers to remove
    # idx, site, date (IF NEW PITS GET ADDED IDXS NEED TO BE UPDATED)

        # 13, banner-snotel, 2020-02-19
        # 18, banner-open, 2020-01-09
        # 32, bogus-upper, 2020-02-07
        # 43, LDP-open, 2020-03-04
        # 44, LDP-open, 2020-03-11
        # 48, LDP-tree, 2020-02-20
        # 61, joe-wright, 2020-03-11
        # 67, michigan-river, 2020-02-26
        # 70, fraser-jpl1, 2019-10-24
        # 90, fraser-jpl1, 2020-03-18
        # 96, fraser-jpl2, 2019-12-16
        # 121, countyline-open, 2019-12-19
        # 130, countyline-open, 2020-03-18
        # 132, countyline-tree, 2019-12-19
        # 140, countyline-tree, 2020-03-18
        # 141, countyline-tree, 2020-03-25
        # 150, skyway-open, 2020-03-21
        # 158, skyway-tree, 2020-03-21
        # 159, skyway-tree, 2020-03-28
        # 221, sagehen-forest, 2019-12-20

rmv_idx = [13, 18, 32, 43, 44, 48, 61, 67, 70, 90, 96, 121, 130, 132, 140, 141, 150, 158, 159, 221]

# sites to remove due to bad coordinates
# print(df.loc[rmv_idx])


df.drop(rmv_idx, inplace=True) #drop all rows idenified above

# mean location of snow pit study plot for time series
grp = df.groupby("PitID").mean()

# sig figs by column
grp['Latitude'] = grp['Latitude'].round(decimals=5)
grp['Longitude'] = grp['Longitude'].round(decimals=5)
grp['UTME'] = grp['UTME'].round(decimals=0)
grp['UTMN'] = grp['UTMN'].round(decimals=0)

# create csv
grp.to_csv('../avg_coords.csv', sep=',', header=True)

print('script is complete!')

# # UTMs
# mean_utme = grp['UTME'].mean()
# mean_utmn = grp['UTMN'].mean()
# mean_zone = grp['UTMzone'].mean()
# #lat/lon
# mean_lat = grp['Latitude'].mean()
# mean_lon = grp['Longitude'].mean()
