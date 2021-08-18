# -*- coding: utf-8 -*-
import sys
sys.path.append('/Users/mac/.local/share/virtualenvs/mac-hhPdHwQA/lib/python3.6/site-packages')
import requests
import datetime
from pykakasi import kakasi
import csv
import re

url = []
r = []
R = []

for i in reversed(range(1,8)):
    url.append('https://www.data.jma.go.jp/obd/stats/data/mdrr/pre_rct/alltable/predaily0'+str(i)+'.csv')
url.append('https://www.data.jma.go.jp/obd/stats/data/mdrr/pre_rct/alltable/predaily00_rct.csv')
#print(url)
#url = 'https://www.data.jma.go.jp/obd/stats/data/mdrr/pre_rct/alltable/predaily00_rct.csv'

datetime_now = datetime.datetime.now()
#date = datetime_now.strftime('%m_%d')
kakasi = kakasi()

kakasi.setMode('H', 'a')
kakasi.setMode('K', 'a')
kakasi.setMode('J', 'a')

conv = kakasi.getConverter()

trans_table = str.maketrans({"（":"(", "）":")"})



try:
    for i in range(8):
        r.append(requests.get(url[i]))
        r[i].encoding = "Shift_JIS"
        R.append(conv.do(r[i].text))
        with open('data/data_after'+str(i)+'_'+str(datetime_now.month)+'_'+str(datetime_now.day)+'.csv',mode='w') as file:
            file.write(R[i])
    for i in range(8):
        with open('data/data_after'+str(i)+'_'+str(datetime_now.month)+'_'+str(datetime_now.day)+'.csv', mode="r", encoding="utf-8") as rf:
            reader = csv.reader(rf)
            next(reader)
            with open('data/new_data_after'+str(i)+'_'+str(datetime_now.month)+'_'+str(datetime_now.day)+'.csv', mode="w", encoding="utf-8") as wf:
                writer = csv.writer(wf)
                #writer.writerow(["id", "menu", "price(+tax)"])
                for line in reader:
                    try:
                        precipitation = round(float(line[9]))
                    except:
                        pass
                    point = line[2].translate(trans_table)
                    point = re.findall("(?<=\().+?(?=\))", point)
                    writer.writerow([line[1],point,precipitation])

    
    
    #r.encoding = "Shift_JIS"
    #R = conv.do(r.text)
    #print(r.text)
    #file = open('data_2020_'+date+'.csv',mode='w')
    #with open('data_2020_'+str(datetime_now.month)+'_'+str(datetime_now.day)+'.csv',mode='w') as file:
        #file.write(r.text.encode('Shift_JIS'))
        #file.write(R)
    #file.close()
    #print(date)
    
except requests.exceptions.RequestException as err:
    print(err)

"""

with open('data_before_'+i+'_'+str(datetime_now.month)+'_'+str(datetime_now.day)+'.csv', mode="r", encoding="utf-8") as rf:
    reader = csv.reader(rf)
    next(reader)
    with open('new_data_before_'+i+'_'+str(datetime_now.month)+'_'+str(datetime_now.day)+'.csv', mode="w", encoding="utf-8") as wf:
        writer = csv.writer(wf)
        #writer.writerow(["id", "menu", "price(+tax)"])
        for line in reader
            precipitation = round(float(line[9]))
            writer.writerow([line[1],line[2],precipitation])
"""
