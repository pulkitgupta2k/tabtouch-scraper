from bs4 import BeautifulSoup
from htmls import getHTML
import re
from pprint import pprint
from helper import tabulate


if __name__ == "__main__":
    date = input("Enter the date: (YYYY-MM-DD) ")
    # date = "2020-04-18"
    html = getHTML("https://www.tabtouch.com.au:443/racing/hub?date={}".format(date))
    
    if html is None:
        print("Failed for date :"+ date)
    
    soup = BeautifulSoup(html,'html.parser')

    links = []
    temp_link = ""
    meetings = soup.findAll('a' , {'class' : 'meeting tooltip'})
    for meeting in meetings:
        try:
            short_link = meeting['href']
            if temp_link != short_link:
                link = "https://www.tabtouch.com.au" + short_link
                links.append(link)
                temp_link = short_link
            # print(meeting['href'])
        except:
            print("Error")
    # pprint(links)
    final_array = []
    for link in links:
        html1 = getHTML(link)
        soup1 = BeautifulSoup(html1, 'html.parser')
        body = soup1.find('tbody')
        rows = body.findAll('tr', {'id': re.compile(r"race-number-[0-9]")})
        details = {}
        for index,row in enumerate(rows):    
            if index%2 == 0:
                details['sno'] = str(int(index/2))
                row_det = row.findAll('td')
                details['start'] = row_det[0].text
                details['dist'] = row_det[2].text.strip()
                details['race_name'] = row_det[4].text.strip()
            else:
                two_thirds = row.find('div', {'class' : 'two-thirds'})
                tab = two_thirds.find('table')
                tab_res = tab.find('tbody')
                part_dets = tab_res.findAll('tr')
                for index, part_det in enumerate(part_dets):
                    row_det1 = part_det.findAll('td')
                    details['rank_'+ str(index+1) + '_num'] = row_det1[1].text.strip()
                    details['rank_'+ str(index+1) + '_name'] = row_det1[3].contents[0].strip()
                    details['rank_'+ str(index+1) + '_rider'] = row_det1[3].find("small").text
                    tote = row_det1[4].findAll('strong')
                    if(len(tote)==2):
                        details['rank_'+ str(index+1) + '_W'] = tote[0].text
                        details['rank_'+ str(index+1) + '_P'] = tote[1].text
                    elif (len(tote)==1):
                        details['rank_'+ str(index+1) + '_W'] = '-'
                        details['rank_'+ str(index+1) + '_P'] = tote[0].text
                    else:
                        details['rank_'+ str(index+1) + '_W'] = '-'
                        details['rank_'+ str(index+1) + '_P'] = '-'
                result_pool = two_thirds.find('ul')
                result_pool_tabs = result_pool.findAll('li')
                details['win'] = result_pool_tabs[0].find('span', {'class' : 'win'}).find('strong',{'class': 'pool-amount'}).text
                details['place'] = result_pool_tabs[0].find('span', {'class' : 'place'}).find('strong',{'class': 'pool-amount'}).text
                details['qulnella'] = result_pool_tabs[1].find('strong',{'class': 'pool-amount'}).text
                details['exacta'] = result_pool_tabs[2].find('strong',{'class': 'pool-amount'}).text
                details['trifecta'] = result_pool_tabs[3].find('strong',{'class': 'pool-amount'}).text
                try:
                    details['first_4'] = result_pool_tabs[4].find('strong',{'class': 'pool-amount'}).text
                except:
                    details['first_4'] = '-'
                try:
                    details['double'] = result_pool_tabs[5].find('strong',{'class': 'pool-amount'}).text
                except:
                    details['double'] = '-'
                try:
                    details['quaddle'] = result_pool_tabs[6].find('strong',{'class': 'pool-amount'}).text
                except:
                    details['quaddle'] = '-'
                third = row.find('div',{'class' : 'third'})
                third_body = third.find('tbody')
                third_body_res = third_body.findAll('tr')
                details['qulnella_results'] = third_body_res[0].findAll('td')[1].text.strip()
                details['qulnella_dividends'] = third_body_res[0].findAll('td')[2].text.strip()
                details['exacta_results'] = third_body_res[1].findAll('td')[1].text.strip()
                details['exacta_dividends'] = third_body_res[1].findAll('td')[2].text.strip()
                details['trifecta_results'] = third_body_res[2].findAll('td')[1].text.strip()
                details['trifecta_dividends'] = third_body_res[2].findAll('td')[2].text.strip()
                details['first_4_results'] = third_body_res[3].findAll('td')[1].text.strip()
                details['first_4_dividends'] = third_body_res[3].findAll('td')[2].text.strip()
                # details['double_results'] = third_body_res[4].findAll('td')[1].text.strip()
                # details['double_dividends'] = third_body_res[4].findAll('td')[2].text.strip()
                # try:
                #     details['quaddle_results'] = third_body_res[5].findAll('td')[1].text.strip()
                #     details['quaddle_dividends'] = third_body_res[5].findAll('td')[2].text.strip()
                # except:
                #     details['quaddle_results'] = '-'
                #     details['quaddle_dividends'] = '-'
                
                final_array.append(details)
                pprint(details)
                details = {}

    for array in final_array:
        arr = []
        arr.append(array['sno'])
        arr.append(array['start'])
        arr.append(array['dist'])
        arr.append(array['race_name'])

        arr.append(array['rank_1_num'])
        arr.append(array['rank_1_name'])
        arr.append(array['rank_1_rider'])
        arr.append(array['rank_1_W'])
        arr.append(array['rank_1_P'])

        try:
            arr.append(array['rank_2_num'])
            arr.append(array['rank_2_name'])
            arr.append(array['rank_2_rider'])
            arr.append(array['rank_2_W'])
            arr.append(array['rank_2_P'])
        except:
            arr.append(" ")
            arr.append(" ")
            arr.append(" ")
            arr.append(" ")
            arr.append(" ")
        
        try:
            arr.append(array['rank_3_num'])
            arr.append(array['rank_3_name'])
            arr.append(array['rank_3_rider'])
            arr.append(array['rank_3_W'])
            arr.append(array['rank_3_P'])
        except:
            arr.append(" ")
            arr.append(" ")
            arr.append(" ")
            arr.append(" ")
            arr.append(" ")

        try:
            arr.append(array['rank_4_num'])
            arr.append(array['rank_4_name'])
            arr.append(array['rank_4_rider'])
            arr.append(array['rank_4_W'])
            arr.append(array['rank_4_P'])
        except:
            arr.append(" ")
            arr.append(" ")
            arr.append(" ")
            arr.append(" ")
            arr.append(" ")

        arr.append(array['win'])
        arr.append(array['place'])
        arr.append(array['qulnella'])
        arr.append(array['exacta'])
        arr.append(array['trifecta'])
        arr.append(array['first_4'])
        arr.append(array['double'])
        arr.append(array['quaddle'])

        arr.append(array['qulnella_results'])
        arr.append(array['qulnella_dividends'])
        arr.append(array['exacta_results'])
        arr.append(array['exacta_dividends'])
        arr.append(array['trifecta_results'])
        arr.append(array['trifecta_dividends'])
        arr.append(array['first_4_results'])
        arr.append(array['first_4_dividends'])

        tabulate(date,arr)
            # print('Alt')
            # print(row.findAll('td')[4].text)

    # print(meetings)
    # print(html)