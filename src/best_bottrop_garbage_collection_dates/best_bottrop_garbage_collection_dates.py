from __future__ import annotations

from dataclasses import dataclass
from .const import STREET_ID_DICT, BASE_URL, DEFAULT_TIMEOUT, CHECK_COOKIE_NAME, CHECK_COOKIE_VALUE
import aiohttp
import datetime
import logging
from yarl import URL

_LOGGER = logging.getLogger(__name__)

@dataclass
class BESTBottropGarbageCollectionDates:
    """ Class for managing connection and data to the BEST Bottrop garbage collection dates"""

    trash_types_json : list[dict] = ""
    session_timeout = aiohttp.ClientTimeout (total=None,sock_connect=DEFAULT_TIMEOUT,sock_read=DEFAULT_TIMEOUT)
    base_url = BASE_URL
    base_url_port = None

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

    def get_street_id_dict (self):
        return STREET_ID_DICT

    def get_id_for_name(self, x):
        return STREET_ID_DICT.get(x)

    def _get_base_url(self) -> str:
        # check if port was overwritten
        if self.base_url_port != None:
            return self.base_url+":"+str(self.base_url_port)
        return self.base_url

    def _create_session(self, base_url: str) -> aiohttp.ClientSession:
        # The website expects the cookie that its browser check sets via JavaScript
        cookie_jar = aiohttp.CookieJar(unsafe=True)
        cookie_jar.update_cookies({CHECK_COOKIE_NAME: CHECK_COOKIE_VALUE}, response_url=URL(base_url))
        return aiohttp.ClientSession(timeout = self.session_timeout, cookie_jar = cookie_jar)

    async def _get_json(self, url: str):
        async with self._create_session(self._get_base_url()) as session:
            async with session.get(url) as response:
                response.raise_for_status()
                # raises ContentTypeError (a ClientError) if the server returned e.g. an HTML page
                return await response.json()

    async def get_trash_types (self):
        # Load the trashtypes
        try:
            self.trash_types_json = await self._get_json(self._get_base_url()+'/api/trashtype')
        except (aiohttp.ClientError, aiohttp.ClientConnectionError, TimeoutError) as e:
            _LOGGER.debug ("Could not load dates due to exception: %s", type(e).__name__)
            raise e

    async def get_dates_as_json(self, street_code, number) -> list[dict]:
        dates_json = ""

        if (street_code != None and self.trash_types_json != None):
            try:
                url = self._get_base_url()+'/api/street/{0}/house/{1}/collection'.format(street_code, number)
                dates_json = await self._get_json(url)
                dates_json = list(filter(self._today_or_later, dates_json))
            except aiohttp.ClientResponseError as e:
                if e.status == 404:
                    # unknown street or house number: there are no dates
                    return []
                _LOGGER.debug ("Could not load dates due to exception: %s", type(e).__name__)
                raise e
            except (aiohttp.ClientError, aiohttp.ClientConnectionError, TimeoutError) as e:
                _LOGGER.debug ("Could not load dates due to exception: %s", type(e).__name__)
                raise e

            for date_item in dates_json:
                date_item.update({"trashType": self._get_name_for_id(date_item.get("trashType"), self.trash_types_json)})

        return dates_json
