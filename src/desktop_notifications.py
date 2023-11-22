from plyer import notification

def notify(
    five_minute_average_raw_json:dict, 
    threshold:int
)-> None:
    """
    Gives a notification to user's device when called. The message will tell you what average price is below 
    the threshold. It is implied that average high prices being below the threshold means that average low prices
    will also be below the threshold. 

    Parameters:
    five_minute_average_raw_json (dict): a raw json file containing data on the past 5 minutes of bond sales 
    threshold (int): a user defined bond price threshold to trigger notifications 
    """
    average_high_price = five_minute_average_raw_json['avgHighPrice']
    average_low_price = five_minute_average_raw_json['avgLowPrice']

    if average_high_price < threshold:
        message = f'Average high prices for bonds are at {average_high_price}. Below defined threshold of {threshold}!'
    else:
        message = f'Average low prices for bonds are at {average_low_price}. Below defined threshold of {threshold}!'

    notification.notify(
        title='Hurry to the Grand Exchange!',
        message= message,
        app_icon=None,  
        timeout=10  # In seconds
    )
    

