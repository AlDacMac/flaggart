from flaggart.wiki_flags import selectflagpage
from flaggart.wiki_flags import getpage
import pytest
import wikipedia

scotpage = wikipedia.page("flag of scotland")

#Tests for getpage

def test_getpage_basic():
    assert getpage("Scotland") == scotpage

#Tests for selectpage

def test_selectpage_basic():
    assert selectflagpage("Scotland", ['Flag of Scotland']) == 'Flag of Scotland'

def test_selectpage_altname():
    assert selectflagpage("Britain", ["Union Jack", "Flag of Britain"]) == "Flag of Britain"