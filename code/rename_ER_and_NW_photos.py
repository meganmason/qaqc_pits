import datetime
import glob
import os
import shutil
import numpy as np
import pandas as pd
from pathlib import Path
from openpyxl import load_workbook

# discluded are: Irwin Barn, Gothic, and Trench
# er_dict = {
# "20200201_COERAP_1": "1524",
# "20200201_COERAP_2": "1550",
# "20200201_COERAP_3": "1610",
# "20200226_COERAP_1": "1550",
# "20200226_COERAP_2": "1600",
# "20200427_COERAP_1": "0845",
# "20200427_COERAP_2": "0930",
# "20200427_COERAP_3": "1015",
# "20200512_COERAP_1": "1430",
# "20200201_COER12_1": "1154",
# "20200201_COER12_2": "1232",
# "20200201_COER12_3": "1305",
# "20200226_COER12_1": "1226",
# "20200226_COER12_2": "1241",
# "20200226_COER12_3": "1242",
# "20200428_COER12_1": "1400",
# "20200428_COER12_2": "1415",
# "20200428_COER12_3": "1445",
# "20200512_COER12_1": "1030",
# "20200512_COER12_2": "1045",
# "20200512_COER12_3": "1100",
# "20200226_COER13_1": "1115",
# "20200226_COER13_2": "1130",
# "20200226_COER13_3": "1155",
# "20200428_COER13_1": "1230",
# "20200428_COER13_2": "1245",
# "20200428_COER13_3": "1300",
# "20200512_COER13_1": "1115",
# "20200512_COER13_2": "1130",
# "20200512_COER13_3": "1200",
# "20200201_COER14_2": "1040",
# "20200201_COER14_1": "1300",
# "20200201_COER14_3": "1350",
# "20200226_COER14_2": "1007",
# "20200226_COER14_1": "1024",
# "20200226_COER14_3": "1040",
# "20200428_COER14_1": "1015",
# "20200428_COER14_2": "1045",
# "20200428_COER14_3": "1115",
# "20200512_COER14_1": "1230",
# "20200512_COER14_2": "1300",
# "20200512_COER14_3": "1330",
# "20200201_COERO2_2": "0950",
# "20200201_COERO2_1": "1120",
# "20200201_COERO2_3": "1220",
# "20200226_COERO2_2": "1000",
# "20200226_COERO2_1": "1018",
# "20200226_COERO2_3": "1120",
# "20200427_COERO2_1": "1145",
# "20200427_COERO2_2": "1215",
# "20200427_COERO2_3": "1245",
# "20200201_COERO4_1": "1000",
# "20200201_COERO4_2": "1115",
# "20200201_COERO4_3": "1215",
# "20200226_COERO4_1": "1230",
# "20200226_COERO4_2": "1330",
# "20200226_COERO4_3": "1425",
# "20200428_COERO4_1": "0830",
# "20200428_COERO4_2": "0900",
# "20200428_COERO4_3": "0915",
# "20200513_COERO4_1": "0845",
# "20200513_COERO4_2": "0900",
# "20200513_COERO4_3": "0915",
# "20200201_COERO6_1": "1400",
# "20200201_COERO6_2": "1430",
# "20200201_COERO6_3": "1500",
# "20200226_COERO6_1": "1428",
# "20200226_COERO6_2": "1458",
# "20200226_COERO6_3": "1459",
# "20200427_COERO6_1": "1345",
# "20200427_COERO6_2": "1430",
# "20200427_COERO6_3": "1445",
# "20200202_COERUP_1": "1030",
# "20200202_COERUP_2": "1120",
# "20200202_COERUP_3": "1215",
# "20200226_COERUP_1": "1310",
# "20200226_COERUP_2": "1330",
# "20200226_COERUP_3": "1400",
# "20200429_COERUP_1": "1030",
# "20200429_COERUP_2": "1115",
# "20200429_COERUP_3": "1130",
# "20200512_COERUP_1": "0900",
# "20200512_COERUP_2": "0930",
# "20200512_COERUP_3": "0945"
# }


# location = "East-River"
# path = Path('/Users/mamason6/Google Drive/My Drive/SnowEx-2020/SnowEx-2020-timeseries-pits/timeseries_pitbook_photos/{}'.format(location))
#
# for filename in path.rglob('*.jpg'):
#
#     if "COERIB" in filename.name:
#         # print('skipping because it is: ', filename.name)
#         pass
#     elif "COERGT" in filename.name:
#         # print('skipping because it is: ', filename.name)
#         pass
#     elif "COERTR" in filename.name:
#         # print('skipping because it is: ', filename.name)
#         pass
#
#     else:
#         directory = filename.parent #dir
#         fname_parse = filename.stem.split('_') # parse the parts of the filename
#         # dict_key = fname_parse[3] + '_' + fname_parse[4] + '_' + fname_parse[5] # create dict key to match fname_dict key (pitID_yyymmdd), give you the time!
#         # time_str = er_dict.get(dict_key)
#         # fname_parse[5] = time_str # replace number 1,2,3 sequence with time
#         list_order = [0, 1, 2, 3, 5, 4, 6, 7]
#         fname_parse = [fname_parse[i] for i in list_order]
#         newname = '_'.join(fname_parse) + filename.suffix
#         print(Path(directory, newname))
#         filename.rename(Path(directory, newname))


# NIWOT
nw_dict = {
"20200122_CONWFF_1": "1020",
"20200122_CONWFF_2": "1010",
"20200122_CONWFF_3": "1025",
"20200212_CONWFF_1": "1110",
"20200212_CONWFF_2": "1145",
"20200311_CONWFF_1": "0900",
"20200311_CONWFF_2": "0920",
"20200311_CONWFF_3": "0945",
"20200422_CONWFF_1": "1310",
"20200513_CONWFF_1": "0955",
"20200513_CONWFF_2": "1030",
"20200513_CONWFF_3": "0930",
"20200122_CONWFN_1": "1245",
"20200122_CONWFN_2": "1230",
"20200122_CONWFN_3": "1231",
"20200212_CONWFN_1": "1335",
"20200311_CONWFN_1": "1100",
"20200311_CONWFN_2": "1130",
"20200311_CONWFN_3": "1101",
"20200513_CONWFN_1": "1000",
"20200513_CONWFN_2": "0944",
"20200513_CONWFN_3": "1024",
"20200513_CONWFN_4": "1048",
"20200122_CONWFS_1": "1405",
"20200122_CONWFS_2": "1406",
"20200122_CONWFS_3": "1400",
"20200212_CONWFS_1": "1040",
"20200212_CONWFS_2": "1108",
"20200212_CONWFS_3": "1100",
"20200311_CONWFS_1": "0930",
"20200311_CONWFS_2": "0931",
"20200311_CONWFS_3": "1010",
"20200513_CONWFS_1": "1000",
"20200513_CONWFS_2": "0930",
"20200513_CONWFS_3": "0915",
"20200513_CONWFS_4": "0945",
"20200122_CONWOF_1": "1140",
"20200122_CONWOF_2": "1115",
"20200122_CONWOF_3": "1100",
"20200212_CONWOF_1": "1300",
"20200212_CONWOF_2": "1310",
"20200212_CONWOF_3": "1254",
"20200311_CONWOF_1": "1100",
"20200311_CONWOF_2": "1118",
"20200311_CONWOF_3": "1145",
"20200422_CONWOF_1": "1054",
"20200422_CONWOF_2": "1155",
"20200513_CONWOF_1": "1050",
"20200513_CONWOF_2": "1105",
"20200513_CONWOF_3": "1130",
"20200513_CONWOF_4": "1115",
}

location = "Niwot-Ridge"
path = Path('/Users/mamason6/Google Drive/My Drive/SnowEx-2020/SnowEx-2020-timeseries-pits/timeseries_pitbook_photos/{}'.format(location))

for filename in path.rglob('*.jpg'):

    if "CONWSA" in filename.name:
        # print('skipping because it is: ', filename.name)
        pass
    elif "CONWC1" in filename.name:
        # print('skipping because it is: ', filename.name)
        pass

    else:
        directory = filename.parent #dir
        fname_parse = filename.stem.split('_') # parse the parts of the filename
        dict_key = fname_parse[3] + '_' + fname_parse[4] + '_' + fname_parse[5] # create dict key to match fname_dict key (pitID_yyymmdd), give you the time!
        time_str = nw_dict.get(dict_key)
        fname_parse[5] = time_str # replace number 1,2,3 sequence with time
        list_order = [0, 1, 2, 3, 5, 4, 6, 7]
        fname_parse = [fname_parse[i] for i in list_order]
        newname = '_'.join(fname_parse) + filename.suffix
        print(Path(directory, newname))
        filename.rename(Path(directory, newname))
