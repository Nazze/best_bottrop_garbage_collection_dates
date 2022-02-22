"""Basic tests for the BEST Bottrop API"""
import asyncio
import aiohttp
import pytest
import requests
from asyncio.proactor_events import _ProactorBasePipeTransport
from functools import wraps


import best_bottrop_garbage_collection_dates

@pytest.mark.asyncio
async def test_load_trash_types():
    print ("test_load_trash_types")
    test_class = best_bottrop_garbage_collection_dates.BESTBottropGarbageCollectionDates()
    print (test_class)
    await test_class.load_trash_types()
    assert test_class.trash_types_json != ""

@pytest.mark.asyncio
async def test_load_trash_types_and_check_content():
    print ("test_load_trash_types")
    test_class = best_bottrop_garbage_collection_dates.BESTBottropGarbageCollectionDates()
    print (test_class)
    await test_class.load_trash_types()
    test_class.trash_types_json[0].get("DFF3C375")
    for i in test_class.trash_types_json: 
        if i.get("id") == "DFF3C375":
            garbage_type_str = i.get("name")
    assert garbage_type_str == "Papiertonne"

@pytest.mark.asyncio
async def test_load_dates_pass():
    print ("test_load_dates")
    try:
        test_class = best_bottrop_garbage_collection_dates.BESTBottropGarbageCollectionDates()
        l = await test_class.get_dates_as_json("Steinmetzstraße", 4)
    except aiohttp.ClientError as e:
        print ("Could not load dates!")
    #assert (l != None and type(l) is list)
    assert l != None

@pytest.mark.asyncio
async def test_load_dates_fail():
    print ("test_load_dates")
    test_class = best_bottrop_garbage_collection_dates.BESTBottropGarbageCollectionDates()
    l = await test_class.get_dates_as_json("bla",200)
   # l = await test_class.get_dates_as_json("Steinmetzstraße", 4)
    #assert l != None
    assert "" == l

def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise
    return wrapper

# Silence the exception here.
_ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)