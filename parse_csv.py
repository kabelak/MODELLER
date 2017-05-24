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


def main(argv):
    url = "http://datagov.ic.nhs.uk/presentation/2017_01_January/T201701ADDR+BNFT.CSV"

    with urllib.request.urlopen(url) as response, open("201701.csv", 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
        print("download complete")

    df = pd.read_csv(argv)

    mydf = df[df["PRACTICE"].isin(["N81649", "N85638"])]

    # print(mydf)

    # writer = pd.ExcelWriter('output.xlsx')
    mydf.to_csv('output.csv', sep=',')
    # mydf.to_excel(writer, 'Sheet1')


#    i = 0
#    while ( i < 2 ):
#        print(i)
#        j = 0
#        while ( j < 10 ):
#           print(j)
#           print(df.iloc[i,j])
#            j += 1
#        i += 1









if __name__ == "__main__":
    main(sys.argv[1])

__author__ = 'Kavin'
__usage__ = ''
