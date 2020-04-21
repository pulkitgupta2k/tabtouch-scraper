from htmls import getHTML
import csv
import sys
import numpy

def tabulate(csvFile, array):
    with open("sheets/%s.csv" % (csvFile), 'a', newline='' ,encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        for i in range(0, len(array)):
            if len(array[i]) > 0:
                writer.writerow(array[i])
        print("Succesfully tabulated %s rows to %s.csv." % (len(array), csvFile))
    return True