from __future__ import annotations


from dataclasses import dataclass
from const import STREET_ID_DICT
import enum
import requests
import datetime
import aiohttp

@dataclass
class BESTBottropGarbageCollectionDates:
    """ Class for managing connection and data to the BEST Bottrop garbage collection dates"""

    trash_types_json : list[dict] = ""
    HTTPSession : aiohttp.ClientSession() = None

    def _get_name_for_id(self, x, json):
        for i in json:
            if i.get("id") == x:
                return i.get("name")
        return x

    def _today_or_later(self, x):
        # Check and return only if the date in the JSON is today or later
        xday, xmonth, xyear = x.get("formattedDate").split(".")
        xdate = datetime.date(int(xyear), int(xmonth), int(xday))

        if xdate >= datetime.datetime.today().date():
            return x;
        else: return "";

    def load_trash_types (self):
        # Load the trashtypes
        try:
            trash_types = requests.get('https://www.best-bottrop.de/api/trashtype')
        except requests.exceptions.RequestException:
            print ("Could not load trashtypes!")
            return ""
        self.trash_types_json = trash_types.json()

    def get_dates_as_json(self, street, number) -> list[dict]:
        # Get the BEST street id code for a given street
        street_code = STREET_ID_DICT.get(street)

        dates_json = ""

        if (street_code != None and self.trash_types_json != None):
            try:
                dates = requests.get('https://www.best-bottrop.de/api/street/{0}/house/{1}/collection'.format(street_code, number))
            except requests.exceptions.RequestException:
                print ("Could not load dates!")
                return ""
            dates_json = dates.json()
            dates_json = list(filter(self._today_or_later, dates_json))

            # now replace the BEST trashType codes with real names, e.g. 3F14EDC7 for Gelbe Tonne

            for date_item in dates_json:
                date_item.update({"trashType": self._get_name_for_id(date_item.get("trashType"), self.trash_types_json)})

        return dates_json
        