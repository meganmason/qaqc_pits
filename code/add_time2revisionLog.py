import datetime
import time
import glob
import os
import shutil
import pandas as pd
import csv
from csv import writer
from pathlib import Path
from openpyxl import load_workbook

xls_path = Path('/Users/meganmason491/Google Drive/SnowEx-2020/SnowEx-2020-timeseries-pits/timeseries_pitbook_sheets_EDIT/FOR_EDIT/')
revisions_path = Path('/Users/meganmason491/Downloads/snowex2020-timeseries-pits-revisions.xlsx') #downloads file to test...

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def fillTime(filename):

    timeStr = filename.name.split('_')[2]
    timeStrColon = timeStr[:2] + ':' + timeStr[2:] # insert colon
    # t = datetime.datetime.strptime(timeStrColon, "%H:%M")

    return timeStrColon


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":


    for f in xls_path.rglob('*COSB*'):

        # print(f.name)
        time = fillTime(f)
        print(time)
