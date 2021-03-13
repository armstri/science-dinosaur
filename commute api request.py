import time
from datetime import datetime
import requests
from apscheduler.schedulers.background import BackgroundScheduler


def commute_request():

    api_key = 'AIzaSyDB0GfR1ulHzjtD8NHQngYMtR1zeaE-K4Q'
    base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial'
    origin = 'ChIJ-X3lsxBF5IkRszqn6uIPZoo'       
    destination = 'ChIJ79Y9PXYK5okRD9fF_h3xQGs'

    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')

    request_url = base_url + '&origins=place_id:' + origin + '&destinations=place_id:' + destination +'&departure_time=now&traffic_model=best_guess' + '&key=' + api_key

    #print(request_url)
    
    commute_data = requests.get(request_url)
    commute_data = commute_data.json()['rows'][0]['elements'][0]
    commute_time = round(commute_data['duration_in_traffic']['value']/60)

    print('***************************')
    print('The commute time to Mystic Aquarium is approximately ' + str(commute_time) + ' minutes.')
    print('Current Time:', current_time)
    print('***************************')
    
    #return commute_time

#def amtrak_scrape():
    


#sched = BackgroundScheduler (daemon=True)
#sched.add_job(commute_request, 'interval', minutes=1)
#sched.start()
commute_request()
    
