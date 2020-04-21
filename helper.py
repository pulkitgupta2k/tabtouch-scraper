from htmls import getHTML
import csv
import sys

def tabulate(csvFile, array):
    with open("sheets/%s.csv" % (csvFile), 'a', newline='' ,encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(array)
        # print("Succesfully tabulated %s rows to %s.csv." % (len(array), csvFile))
    return True