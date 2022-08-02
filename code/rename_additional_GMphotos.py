from datetime import datetime, timedelta
import glob
import os
import shutil
import numpy as np
import pandas as pd
from pathlib import Path

path = Path('/Users/mamason6/Google Drive/My Drive/SnowEx-2020/SnowEx-2020-timeseries-pits/gm_snowex_jsl/pics-renamed')

# # Part 1 - reorder filename so that pitID comes after date/time portion
# for i, filename in enumerate(sorted(path.rglob('*.jpg'))):
#     # print(i, filename.stem)
#
#     directory = filename.parent # dir
#     fname_parse = filename.stem.split('_') # parse the parts of the filename
#     order_list = [0, 1, 2, 4, 5, 3, 6, 7] # new order to match (i.e yyyymmdd_hhmm_xxxxxx)
#     fname_reorder = [fname_parse[i] for i in order_list] # reorder list
#     newname = '_'.join(fname_reorder) + filename.suffix # join list and add suffix
#     print(Path(directory, newname))
#     filename.rename(Path(directory, newname)) # save file
#
# print('script donzo!')


# Part II -
    # a). date format, mmddyy --> yyyymmdd.
    # b). fix time to standard time (all pits post 3/8/2020 were in Daylight time). Need -1hr.

daylight_savings = datetime(2020, 3, 8) # March 8th, 2020

for i, filename in enumerate(sorted(path.rglob('*.jpg'))):
    # print(i, filename.stem)

    timestamp_str = filename.stem.split('_')[3] + '_' + filename.stem.split('_')[4]
    timestamp = datetime.strptime(timestamp_str, '%m%d%y_%H%M') # time
    # print(timestamp)

    if timestamp > daylight_savings:
        # convert to Local Standard Time
        newTime = timestamp - timedelta(hours=1) # this has to be a datetime combo, not just time
    else:
        newTime = timestamp

    # file management
    directory = filename.parent # dir
    newTimestamp_str = newTime.strftime("%Y%m%d_%H%M") # new timestamp as string from line above
    newFilename = Path(str(filename.name).replace(timestamp_str, newTimestamp_str)) # update filename
    print(Path(directory, newFilename))
    filename.rename(Path(directory, newFilename)) # save file
