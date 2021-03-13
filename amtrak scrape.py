import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from pprint import pprint
import sys

train_num = input('Enter your train number: ')

url = ('https://asm.transitdocs.com/api/trainDetail.php?year=2021&month=2&day=21&train='+ str(train_num))

#url = 'https://asm.transitdocs.com/api/trainDetail.php?year=2021&month=2&day=16&train=66'
r = requests.get(url)

try:
    traindata = r.json()
    stationdata = traindata['stations']
except:
    print ('Train number '+str(train_num) + ' is not in service at this time')
    sys.exit()

# Using next() + dictionary comprehension 
# Find dictionary matching value in list 
pvd_data = next((sub for sub in stationdata if sub['code'] == 'PVD'), None) 
  
try:    
    pvd_est_dep = pvd_data['est_dep']
except:
    print('Train number ' + str(train_num) + ' departed PVD at ' + str(pvd_data['act_dep']))
    sys.exit()
if pvd_est_dep[1] == '/':
    pvd_est_dep = '0'+ pvd_est_dep


pvd_sch_dep = pvd_data['sch_dep']

if pvd_sch_dep[1] == '/':
    pvd_sch_dep = '0'+ pvd_sch_dep

pvd_est_time=datetime.strptime(pvd_est_dep, '%m/%d/%Y %I:%M%p')
pvd_sch_time= datetime.strptime(pvd_sch_dep, '%m/%d/%Y %I:%M%p') 

minute_delta = (pvd_est_time - pvd_sch_time).total_seconds() / 60.0


if pvd_est_time == pvd_sch_time:
    print('Train '+ str(train_num)+ ' is currently on schedule')
elif pvd_est_time > pvd_sch_time:
    print('Train '+ str(train_num)+ ' is currently ' +str(minute_delta) + ' minutes behind schedule')
elif pvd_est_time < pvd_sch_time:
    print('Train '+ str(train_num)+ ' is currently ' +str(minute_delta) + ' minutes ahead of schedule')

print('************')
         
print('Train '+ str(train_num)+ ' is scheduled to depart PVD for BBY at ' + str(pvd_sch_time))
print('Train '+ str(train_num)+ ' is estimated to depart PVD for BBY at ' + str(pvd_est_time))

  



