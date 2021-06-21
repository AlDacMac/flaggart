from flaggart.wiki_flags import *
import pytest

def test_getpagename_basic():
    assert getpagename("Scotland") == "Flag of Scotland"

def test_selectpage_basic():
    assert selectflagpage("Scotland", ['Flag of Scotland']) == 'Flag of Scotland'

def test_selectpage_altname():
    assert selectflagpage("Britain", ["Union Jack", "Flag of Britain"]) == "Flag of Britain"

def test_getflagurl_basicscotland():
    assert getflagurl('Flag of Scotland') == "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Flag_of_Scotland.svg/1000px-Flag_of_Scotland.svg.png"

def test_getflagurl_provo():
    assert getflagurl("Flag of Provo, Utah") == 'https://upload.wikimedia.org/wikipedia/en/2/23/Flag_of_Provo%2C_Utah_%282015%29.png'