from flaggart.wiki_flags import *
import pytest

def test_getpagename_basic():
    assert getpagename("Scotland") == "Flag of Scotland"

def test_selectpage_basic():
    assert selectflagpage("Scotland", ['Flag of Scotland']) == 'Flag of Scotland'

def test_selectpage_altname():
    assert selectflagpage("Britain", ["Union Jack", "Flag of Britain"]) == "Flag of Britain"