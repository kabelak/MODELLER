__author__ = 'Kavin'
__usage__ = ''

import sys

monthDict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
             9: "September", 10: "October", 11: "November", 12: "December"}

i = 1
while (i < 13):
    print(monthDict[i])
    i += 1
    # "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9,  "Oct":10,  "Nov":11,  "Dec":12}
