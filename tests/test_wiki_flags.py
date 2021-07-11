from flaggart.wiki_flags import *
import pytest

########################################################################################################################################################################
# Unit Tests
########################################################################################################################################################################

# getflagpage

def test_getflagpage_basic():
    assert getflagpage("Scotland")[0] == "Flag of Scotland"

#VERY IMPORTANT
def test_getflagpage_basic2():
    assert getflagpage("Provo")[0] == "Flag of Provo, Utah"

def test_getflagpage_altname():
    assert getflagpage("Britain")[0] == "Union Jack"

def test_getflagpage_flagsof():
    assert getflagpage("Mughal Empire")[0] == "Flags of the Mughal Empire"

def test_getflagpage_disambig_nypure():
    result = getflagpage("New York")
    assert result[0] == "Coat of arms of New York"
    for page in  ["Coat of arms of New York", "Flags of New York City"]:
        assert page in result[1]

def test_getflagpage_disambig_nycity():
    assert getflagpage("New York City")[0] == "Flags of New York City"
 
def test_getflagpage_disambig_nystate():
    assert getflagpage("New York State")[0] == "Coat of arms of New York"

    # For some reason running this with pytest ocassionally gives a result where the rainbow flag and 
    #   bi flag pages are swapped. Don't worry about it.
def test_getflagpage_search_lgbt():
    result = getflagpage('gay')[0]
    assert result[0] == 'Rainbow flag (LGBT)' 
    for page in ['Rainbow flag (LGBT)', 'Bear flag (gay culture)', 'Gay pride flag of South Africa', 'Bisexual pride flag', 'Rainbow flag', 'Pansexual pride flag', 'Pride flag', 'Lesbian flag']:
        assert page in result[1]

def test_getflagpage_ispage_includesearch():
    result = getflagpage('Britain')[1]
    for page in ['Flag of the United Kingdom', 'Flag of Great Britain', 'List of United Kingdom flags', 'Historical flags of the British Empire and the overseas territories', 
    'Flag of British Columbia', 'Star of India (flag)', 'Flag of Sri Lanka', 'Flag of Malaysia', 'Flag of the United States']:
        assert page in result

def test_getflagpage_ispage_coatofarms():
    result = getflagpage('British coat of arms')
    assert result[0] == "Royal coat of arms of the United Kingdom"
    for page in ['Royal coat of arms of the United Kingdom', 'Arms of Canada', 'National coat of arms', 'Flag and coat of arms of Corsica', 
    'Coat of arms', 'Coat of arms of Malaysia', 'Coat of arms of Zimbabwe', 'Coat of arms of British Columbia', 'Royal arms of England', 'Coat of arms of Australia']:
        assert page in result[1]

# selectflagpage

def test_selectflagpage_basic():
    assert selectflagpage("Scotland", ['Flag of Scotland']) == 'Flag of Scotland'

def test_selectflagpage_altname():
    assert selectflagpage("Britain", ["Union Jack", "Flag of Britain"]) == "Flag of Britain"

def test_selectflagpage_coatarms():
    assert selectflagpage("Portugal", ["Coat of Arms of Portugal"]) == "Coat of Arms of Portugal"

def test_selectflagpage_royalcoat():
    assert selectflagpage("United Kingdom", ["Royal coat of arms of the United Kingdom"]) == "Royal coat of arms of the United Kingdom"

# getflagurl

def test_getflagurl_basicscotland():
    assert getflagurl('Flag of Scotland') == "https://upload.wikimedia.org/wikipedia/commons/1/10/Flag_of_Scotland.svg"

def test_getflagurl_provo():
    assert getflagurl("Flag of Provo, Utah") == 'https://upload.wikimedia.org/wikipedia/en/2/23/Flag_of_Provo%2C_Utah_%282015%29.png'

# constructpageurl

def test_constructurl_oneword():
    assert constructpageurl("test") == "https://en.wikipedia.org/wiki/test"

def test_constructurl_morewords():
    assert constructpageurl("test and again") == "https://en.wikipedia.org/wiki/test_and_again"

# pageexists

def test_pageexists_exists():
    assert pageexists("Wikipedia") == True

def test_pageexists_altname():
    assert pageexists("Flag of United Kingdom")

def test_pageexists_notexists():
    assert pageexists("not a real wikipedia page") == False

# getrerdirect

def test_getredirect_ny():
    assert getredirect("Flag of New York State") == "Coat of arms of New York"

def test_getredirect_realname():
    assert getredirect("Coat of arms of New York") == "Coat of arms of New York"

#isdisambiguation

def test_isdisambiguation_true():
    assert isdisambiguation("Flag of New York") == True

def test_isdisambiguation_false():
    assert isdisambiguation("Union Jack") == False

#getdisambiguationlinks

def test_getdisambiguationlinks_newyork():
    assert getdisambiguationlinks('Flag of New York') == ['Coat of arms of New York', "Flags of New York City"]

def test_getdisambiguationlinks_train():
    links = getdisambiguationlinks('4 Train')
    for page in ['4 (New York City Subway service)', 'Line 4 Yellow (Montreal Metro)', 'Paris Métro Line 4', 'Line 4, Beijing Subway', 'Line 4, Shanghai Metro']:
        assert getredirect(page) in links

#filterresults

def test_filterresults_simple():
    assert filterresults(["flag of belgium"]) == ['flag of belgium']

def test_filterresults_none():
    assert filterresults(["notrelevant"]) == []

def test_filterresults_diffcase():
    assert filterresults(["Flag of Scotland"]) == ['Flag of Scotland']

def test_filterresults_flags():
    assert filterresults(["Flags of New York"]) == ['Flags of New York']

def test_filterresults_arms():
    assert filterresults(["Coat of arms of New York"]) == ['Coat of arms of New York'] 

def test_filterresults_flagatend():
    assert filterresults(["Rainbow Flag (LGBT)"]) == ["Rainbow Flag (LGBT)"]