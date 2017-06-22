__author__ = 'Kavin'
__usage__ = ''

import sys

monthDict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
             9: "September", 10: "October", 11: "November", 12: "December"}

month = 1
while (month < 13):
    year = 2017

    _baseurl = "http://datagov.ic.nhs.uk/presentation/"
    _folder = str(year) + "_" + str("{0:0=2d}".format(month)) + "_" + str(monthDict[month]) + "/"
    _file = "T" + str(year) + str("{0:0=2d}".format(month)) + "ADDR+BNFT.CSV"

    url = _baseurl + _folder + _file

    print(url)

    month += 1
