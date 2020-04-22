from htmls import getHTML
import csv
import sys
import os

def tabulate(csvFile, array):
    with open("%s.csv" % (csvFile), 'a', newline='' ,encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(array)
        print("Tabbed")
        # print("Succesfully tabulated %s rows to %s.csv." % (len(array), csvFile))
    return True

def delete_file(csvFile):
    try:
        os.remove("{}.csv".format(csvFile))
    except:
        pass

def tabulate_n(csvFile, array):
    with open("%s.csv" % (csvFile), 'w', newline='' ,encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(array)
        print("Tabbed")
        # print("Succesfully tabulated %s rows to %s.csv." % (len(array), csvFile))
    return True


def get_last_line(csvFile):
    with open("%s.csv" % (csvFile), 'r', newline='' ,encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        rows = list(reader)
        return rows[-1]

def filePresent(csvFile):
    try:
        f = open("{}.csv".format(csvFile))
        return True
    except:
        return False

def ins_arr(csvFile):
    with open("%s.csv" % (csvFile), 'r', newline='' ,encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        rows = list(reader)
        ret_arr = []
        for row in rows:
            dic = {}
            dic['sno'] = row[0]
            dic['location_code'] = row[1]
            dic['location'] = row[2]
            dic['start'] = row[3]
            dic['dist'] = row[4]
            dic['race_name'] = row[5]
            dic['rank_1_num'] = row[6]
            dic['rank_1_name'] = row[7]
            dic['rank_1_rider'] = row[8]
            dic['rank_1_W'] = row[9]
            dic['rank_1_P'] = row[10]
            dic['rank_2_num'] = row[11]
            dic['rank_2_name'] = row[12]
            dic['rank_2_rider'] = row[13]
            dic['rank_2_W'] = row[14]
            dic['rank_2_P'] = row[15]
            dic['rank_3_num'] = row[16]
            dic['rank_3_name'] = row[17]
            dic['rank_3_rider'] = row[18]
            dic['rank_3_W'] = row[19]
            dic['rank_3_P'] = row[20]
            dic['rank_4_num'] = row[21]
            dic['rank_4_name'] = row[22]
            dic['rank_4_rider'] = row[23]
            dic['rank_4_W'] = row[24]
            dic['rank_4_P'] = row[25]
            dic['win'] = row[26]
            dic['place'] = row[27]
            dic['qulnella'] = row[28]
            dic['exacta'] = row[29]
            dic['trifecta'] = row[30]
            dic['first_4'] = row[31]
            dic['double'] = row[32]
            dic['quaddle'] = row[33]
            dic['qulnella_results'] = row[34]
            dic['qulnella_dividends'] = row[35]
            dic['exacta_results'] = row[36]
            dic['exacta_dividends'] = row[37]
            dic['trifecta_results'] = row[38]
            dic['trifecta_dividends'] = row[39]
            dic['first_4_results'] = row[40]
            dic['first_4_dividends'] = row[41]
            ret_arr.append(dic)
        return ret_arr
        
