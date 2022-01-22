'''
This script pulls the coordinates (UTME, UTMN) from the SnowEx pit forms and
writes the info with header info to a csv.

Intented for quick plotting of UTMs as a check on conversion and transcriptions.

This script works for the __2020__SnowEx__Pit__Form__

This script was modified from the pits_xls2csv_v6.py script from C. Vuyovich.

'''

__author__ = "Megan Mason, ATAAerospace Data Management Liasion"
__version__ = "01"
__maintainer__ = "Megan Mason"
__email__ = "meganmason491@boisestate.edu"
__status__ = "Dvp"
__date__ = "01.2021"

import datetime
import glob
import os
import shutil
import numpy as np
import pandas as pd
from pyproj import Proj, transform
from csv import writer
import textwrap
# from win32com import client #LOTS OF TROUBLE INSTALLING....:/
# import win32api

#----------------------------------METHODS--------------------------------------
def readSnowpit(filename):
    # fname = os.path.basename(filename)
    # pitID = fname.split('_')[0] #split and save first #EXTRA??
    # dateStr = fname.split('_')[-1] #EXTRA?? i.e. not using??

    # open excel file
    xl = pd.ExcelFile(filename)

    # date / location / stie / pit-ID / coordinates
    d = pd.read_excel(xl, sheet_name=0, usecols='S')
    Date = pd.to_datetime(d['Unnamed: 18'][4])
    # print(Date)
    # print(type(Date))
    Date_str=Date.strftime('%Y-%m-%d') #date to string
    # print(Date_str)
    # print(type(Date_str))
    d = pd.read_excel(xl, sheet_name=0, usecols='B')
    Location = d['Location:'][0]
    Site = d['Location:'][2]  # grab site name
    PitID = d['Location:'][4]  # grab pit name
    PitID = PitID.split('_')[0]
    d = pd.read_excel(xl, sheet_name=0, usecols='L')
    UTME = d['Surveyors:'][2]
    d = pd.read_excel(xl, sheet_name=0, usecols='Q')
    UTMN = d['Unnamed: 16'][2]
    d = pd.read_excel(xl, sheet_name=0, usecols='X')
    UTMzone = str(d['Unnamed: 23'][2])[:2] #save first two (eliminates letters)


    return Date_str, Location, Site, PitID, UTME, UTMN, UTMzone

#----------------------------------BODY--------------------------------------

if __name__ == "__main__": #(everything outside of this tabbing can carry over)

    # set-up
    # path_in = '../timeseries_pitbook_sheets/**/*.xlsx' #allows for different # of directories in timeseries sites
    path_in = '../timeseries_pitbook_sheets/American-River/*.xlsx'
    # path_in = '/Users/meganmason491/Documents/snowex/2020/timeseries/qaqc_pits/timeseries_pitbook_sheets/Boise-River/bogus-lower/IDBRBL_20200306.xlsx'

    # data
    data = []
    column_lst = ['Date', 'Location', 'Site', 'PitID', 'UTME', 'UTMN', 'UTMzone']

    for filename in glob.glob(path_in, recursive=True):

        # filename
        print('F:', os.path.basename(filename))


        data.append(readSnowpit(filename))

    df = pd.DataFrame(data, columns=column_lst)
    # print(df)

    print('No. of data rows:', len(df.index))

    df.to_csv('../coords.csv', sep=',', header=True)
