import datetime
import glob
import os
import shutil
import numpy as np
import pandas as pd
from pathlib import Path

# d_path = Path('/Users/meganmason491/Google Drive/SnowEx-2020-timeseries-pits/timeseries_protocol_photos/') #protocol photos
d_path = Path('/Users/meganmason491/Google Drive/SnowEx-2020-timeseries-pits/timeseries_pitbook_photos/') #book photos
f_paths = d_path.rglob('*.jpg')
version = 'v01'

for path in f_paths:
    if path.is_file():
        if path.name[0:28] != 'SnowEx20_SnowPits_TimeSeries': #if the image does NOT start with '', then do the code.

            #print(path.name)
            directory = path.parent #dir
            ext = path.suffix #ext
            name = path.stem #stem
            pitID, dateString, desc = name.split('_')[2:] #save 2nd to end
            newname = 'SnowEx20_SnowPits_TimeSeries' + '_' +  dateString + '_' + pitID + '_' + desc +'_' + version + ext
            print("%s --> %s" %(name, newname))
            path.rename(Path(directory, newname))


#troubleshooting when single file didn't work.
                        # try:
                        #     pitID, dateString, desc = name.split('_')[2:] #save 2nd to end
                        # except ValueError as e:
                        #     print(name)

# print('script done!')
