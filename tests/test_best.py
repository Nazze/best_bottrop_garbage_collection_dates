"""Basic tests for the BEST Bottrop APi."""
import asyncio
import aiohttp
import pytest

import best_bottrop_garbage_collection_dates

def test_load_trash_types():
    print ("test_load_trash_types")
    test_class = best_bottrop_garbage_collection_dates.BESTBottropGarbageCollectionDates()
    print (test_class)
    test_class.load_trash_types()
    assert test_class.trash_types_json != ""

def test_load_trash_types_and_check_content():
    print ("test_load_trash_types")
    test_class = best_bottrop_garbage_collection_dates.BESTBottropGarbageCollectionDates()
    print (test_class)
    test_class.load_trash_types()
    test_class.trash_types_json[0].get("DFF3C375")
    for i in test_class.trash_types_json: 
        if i.get("id") == "DFF3C375":
            garbage_type_str = i.get("name")
    assert garbage_type_str == "Papiertonne"

def test_load_dates_pass():
    print ("test_load_dates")
    test_class = best_bottrop_garbage_collection_dates.BESTBottropGarbageCollectionDates()
    print (test_class)
    l=test_class.get_dates_as_json("Steinmetzstraße",4)
    assert type(l) is list


def test_load_dates_fail():
    print ("test_load_dates")
    test_class = best_bottrop_garbage_collection_dates.BESTBottropGarbageCollectionDates()
    print (test_class)
    l=test_class.get_dates_as_json("bla",200)
    assert "" == l