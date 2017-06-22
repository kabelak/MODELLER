__author__ = 'Kavin'
__usage__ = ''

import sys
import re
import argparse
import os
import pandas as pd
import urllib.request
import shutil

monthDict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
             9: "September", 10: "October", 11: "November", 12: "December"}


def main():
    for year in range(2017, 2017, 1):
        for month in range(1, 1, 1):
            _baseurl = "http://datagov.ic.nhs.uk/presentation/"
            _folder = str(year) + "_" + str("{0:0=2d}".format(month)) + "_" + str(monthDict[month]) + "/"
            _file = "T" + str(year) + str("{0:0=2d}".format(month)) + "PDPI+BNFT.CSV"
            url = _baseurl + _folder + _file

            if os.path.exists(_file):
                if (os.path.getsize(_file) > 10):
                    pass
                else:
                    print("File Corrupt, redownloading")
                    with urllib.request.urlopen(url) as response, open(_file, 'wb') as out_file:
                        shutil.copyfileobj(response, out_file)
                        print("download of " + _file + " complete")
            else:
                with urllib.request.urlopen(url) as response, open(_file, 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)
                    print("download of " + _file + " complete")

            df = pd.read_csv(_file)

            mydf = df[df["PRACTICE"].isin(["P82016", "P84023", "P83017", "P85014", "P86012", "P87627", "P84004",
                                           "P84672", "P88617", "P89025", "P91007", "P92038"])]

            if os.path.exists('output.csv'):
                mydf.to_csv('output.csv', mode='a', index=False, header=False)
            else:
                mydf.to_csv('output.csv', sep=',', index=False)



#    i = 0
#    while ( i < 2 ):
#        print(i)
#        j = 0
#        while ( j < 10 ):
#           print(j)
#           print(df.iloc[i,j])
#            j += 1
#        i += 1









if (__name__ == "__main__"):
    main()
