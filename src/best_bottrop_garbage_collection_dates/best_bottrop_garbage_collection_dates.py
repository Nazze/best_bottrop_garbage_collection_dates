import enum
import requests
import datetime

trash_types_json = ""

def get_name_for_id(x):
    for i in trash_types_json:
        if i.get("id") == x:
            return i.get("name")
    return x

def today_or_later(x):
    xday, xmonth, xyear = x.get("formattedDate").split(".")
    xdate = datetime.date(int(xyear), int(xmonth), int(xday))

    if xdate >= datetime.datetime.today().date():
        return x;
    else: return False;

def get_dates_as_json(street_code, number):
    trash_types = requests.get('https://www.best-bottrop.de/api/trashtype')
    trash_types_json = trash_types.json()

    dates = requests.get('https://www.best-bottrop.de/api/street/{0}/house/{1}/collection'.format(street_code, number))
    dates_json = dates.json()
    dates_json = list(filter(today_or_later, dates_json))

    for date_item in dates_json:
        date_item.update({"trashType": get_name_for_id(date_item.get("trashType"))})

    return dates_json