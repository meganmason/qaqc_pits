import datetime
import glob
import os
import shutil
import numpy as np
import pandas as pd
from csv import writer
import textwrap
from pathlib import Path
import utm

#----------------------------------METHODS--------------------------------------
def readSnowpit(filename):

    # open excel file
    xl = pd.ExcelFile(filename)

    #unique ID
    Identifier = '_'.join(filename.stem.split('_')[0:3])

    # location / pit name
    d = pd.read_excel(xl, sheet_name=0, usecols='B')
    Location = d['Location:'][0]
    Site = d['Location:'][2]
    PitID = d['Location:'][4][:6]


    # spatial info
    d = pd.read_excel(xl, sheet_name=0, usecols='L')
    UTME = int(d['Observers:'][2]) # force int, some cases of string
    d = pd.read_excel(xl, sheet_name=0, usecols='Q')
    UTMN = int(d['Unnamed: 16'][2])
    d = pd.read_excel(xl, sheet_name=0, usecols='X')
    UTMzone = int(d['Unnamed: 23'][2]) # for northern hemisphere
    # convert to Lat/Lon
    LAT = round(utm.to_latlon(UTME, UTMN, UTMzone, "Northern")[0], 5) #tuple output, save first
    LON = round(utm.to_latlon(UTME, UTMN, UTMzone, "Northern")[1], 5) #tuple output, save second

    # temporal info
    d = pd.read_excel(xl, sheet_name=0, usecols='X')
    pit_time = d['Unnamed: 23'][4]
    d = pd.read_excel(xl, sheet_name=0, usecols='S')
    pit_date = d['Unnamed: 18'][4].date()

    return Identifier, PitID, Location, Site, UTME, UTMN, UTMzone, LAT, LON, pit_date, pit_time

#----------------------------------BODY--------------------------------------
if __name__ == "__main__":

    # set-up
    path_in = Path('/Users/mamason6/Google Drive/My Drive/SnowEx-2020/SnowEx-2020-timeseries-pits/timeseries_pitbook_sheets_EDIT/COMPLETE')

    # data
    data = []
    column_lst = ['Identifier', 'PitID', 'Location', 'Site', 'Easting', 'Northing', 'Zone', 'Latitude', 'Longitude', 'Date', 'Local/Standard Time']

    for filename in sorted(path_in.rglob('*.xlsx')):
        # filename
        print(f"...reading {filename.name}")

        d = readSnowpit(filename)

        # append data list with each pit
        data.append(readSnowpit(filename))

    # convert data list to dataframe
    df = pd.DataFrame(data, columns=column_lst)
    print('No. of data rows:', len(df.index))

    # create csv - all sites
    df.to_csv('/Users/mamason6/Documents/snowex/core-datasets/ground/snow-pits/qaqc_pits/sites_dictionary.csv', sep=',', header=True)


    '''
    create: df_avg
    modify dataframe to count unique # of pits compute average coordinates
    '''

    # count unique # of pits
    df['Pit Count'] = df['PitID'].map(df['PitID'].value_counts())

    # mean lcoation of snow pit study plot for Time Series
    df_avg = df.groupby(['PitID', 'Site', 'Location', 'Pit Count']).mean().reset_index()
    # df_avg = df.groupby(['PitID']).mean()

    # add State column
    df_avg['State'] = df_avg['PitID'].str[:2]

    # Sig figs by column
    df_avg['Latitude']  = df_avg['Latitude'].round(decimals=5)
    df_avg['Longitude'] = df_avg['Longitude'].round(decimals=5)
    df_avg['Easting']   = df_avg['Easting'].round(decimals=0)
    df_avg['Northing']  = df_avg['Northing'].round(decimals=0)

    # reorder
    df_avg = df_avg[['State', 'Location', 'Site', 'PitID', 'Latitude', 'Longitude', 'Easting', 'Northing', 'Zone', 'Pit Count']]

    # create csv - average of sites
    df_avg.to_csv('/Users/mamason6/Documents/snowex/core-datasets/ground/snow-pits/qaqc_pits/avg_coords.csv', sep=',', header=True)
