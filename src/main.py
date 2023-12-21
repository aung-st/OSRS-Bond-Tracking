from get_data import get_data_five_minute_average
from dump_json import create_filename,dump_json
from process_json import bulk_process_five_minute_average_json
from desktop_notifications import notify
import time



if __name__ == "__main__":

    # how long the program runs for in seconds
    time_end = time.time() + 3600 # run for an hour
    
    while time.time() < time_end:
        
        # call five minute average data on old school bond (item id: 13190)
        five_minute_average_raw_json = get_data_five_minute_average()['data']['13190']

        # json path
        five_minute_average_json_path = "data/json_dump/five_minute_averages/"

        # hash id length
        id_length = 4

        # create filename and fetch id
        five_minute_averages_filename,five_minute_averages_id = create_filename(five_minute_average_json_path,id_length)

        # dump five minute average json file
        dump_json(five_minute_average_raw_json,five_minute_averages_filename)
        
        # user defined threshold
        threshold = 9500000

        # add data to database
        bulk_process_five_minute_average_json('osrs_db',five_minute_average_raw_json,five_minute_averages_id)
        
        # give notification if price is under threshold 
        # volume is in the condition as 0 volume means NULL price as there were no sales 
       
        if  five_minute_average_raw_json['highPriceVolume'] != 0 and five_minute_average_raw_json['avgHighPrice'] < threshold: 
            notify(five_minute_average_raw_json,threshold)
        elif  five_minute_average_raw_json['lowPriceVolume'] != 0 and five_minute_average_raw_json['avgLowPrice'] < threshold: 
            notify(five_minute_average_raw_json,threshold)


        
        # pause execution to avoid spamming API calls
        time.sleep(300)



    

