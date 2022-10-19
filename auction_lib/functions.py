import locale
locale.setlocale(locale.LC_NUMERIC,"de")

import time
from datetime import datetime
import re

def get_auction_id(text):
    # get the auction end timestamp
    found_parts = re.search('\((.+?)\)', text)
    if found_parts: found = found_parts.group(1) # take the middle part

    auction_end_timestamp = found

    # get the auction title
    found_parts = re.search('\n(.+?)\n', text)
    if found_parts: found = found_parts.group(1) # take the middle part

    auction_title = found

    auction_id = auction_end_timestamp + " - " + auction_title
    return auction_id

def get_auction_detail_id(driver):
    auction_title = driver.find_element_by_css_selector(".auktionstitel").text

    # get end time from auction offer site
    end_time = get_auction_detail_end_time(driver)

    auction_id = end_time[:-3] + " Uhr - " + auction_title
    return auction_id

def get_current_price(text):
    # get the current auction price
    found_parts = re.search('€\\n(.+?) €', text)
    if found_parts: found = found_parts.group(1)

    # convert string to float
    curr_price = locale.atof(found)

    return curr_price
    
def save_data_into_dict(curr_data_dict, curr_id, extraction_time, curr_price):
    # save data with the auction end timestamp and title as a ID
    if curr_id not in curr_data_dict:
        curr_data_dict[curr_id] = {}
    if extraction_time not in curr_data_dict[curr_id]:
        curr_data_dict[curr_id][extraction_time] = {}
    curr_data_dict[curr_id][extraction_time]["price"] = curr_price
    return curr_data_dict

def get_time_series(data_dict, curr_id, subkey="price"):
    # create time series for given id
    x, y = [], []
    for key, data in data_dict[curr_id].items():
        x.append(key)
        if subkey is not None:
            y.append(data[subkey])
        else:
            y.append(data)

    return x, y

def get_offer_metrics(text):
    # get detailed information overview from auction offer
    found_parts = re.search('Höchstbietender\n(.+?)\n', text)
    if found_parts: highest_bidder = found_parts.group(1) # take the middle part

    found_parts = re.search('Anzahl Gebote\n(.+?)\n', text)
    if found_parts: found = found_parts.group(1) # take the middle part
    n_o_bids = int(found)

    found_parts = re.search('Anzahl Klicks\n(.+?)\n', text)
    if found_parts: found = found_parts.group(1) # take the middle part
    n_o_clicks = int(found)

    regexp = re.compile("Anzahl Beobachter\n(.*)$")
    found = regexp.search(text).group(1)
    n_o_watchers = int(found)

    return highest_bidder, n_o_bids, n_o_clicks, n_o_watchers