import wikipedia
import wptools
import requests
import json
import re


def getflagpage(term):
    """Returns the wikipedia page corresponding to the flag associated with the search term, along 
    with a list of alternatives. 

    :param term: A place, person, organisation, etc.
    :type term: String
    
    :return: A list containing the title of the wikipedia page corresponding to the suggested flag,
        and a list of titles for suggested alternative pages
    :rtype: [String, [String]]
    """
    result = None
    searchresults = filterresults(wikipedia.search(f"Flag of {term}"))
    if pageexists(f"Flag of {term}"):
        #TODO Bloody redirects w()
        result = getredirect(f"Flag of {term}")
        altresults = searchresults
    else:
        result = selectflagpage(term, searchresults)
        altresults = searchresults
        return [result, altresults]
    if isdisambiguation(result):
        altresults = getdisambiguationlinks(result)
        result = altresults[0]
    return [result, altresults]

def selectflagpage(place, results):
    for result in results:
        if "flag" in result.lower():
            return result
    for result in results:
        if "coat of arms" in result.lower():
            return result

def filterresults(searchresults):
    return [x for x in searchresults if re.search('flag|coat of arms', x, re.IGNORECASE)]

def getflagurl(pagename):
    page = wptools.page(pagename)
    page.get_restbase('/page/summary/')
    return page.data['image'][0]['url']

#Checks if a wikipedia page exists
#   Note: case sensitive
def pageexists(pagename):
    url = constructpageurl(pagename)
    if requests.get(url).status_code == 200:
        return True
    else: 
        return False

# Makes a url to a wikipedia page based on plaintext pagename
def constructpageurl(pagename):
    pagenamehyphen = pagename.replace(' ', '_')
    url = "https://en.wikipedia.org/wiki/" + pagenamehyphen
    return url

def getredirect(pagename):
    pagenamehyphen = pagename.replace(' ', '_')
    query = requests.get(f'https://en.wikipedia.org/w/api.php?action=query&titles={pagenamehyphen}&&redirects&format=json')
    data = json.loads(query.text)
    if 'redirects' in data['query']:
        return data['query']['redirects'][0]['to']
    else:
        return pagename

def isdisambiguation(pagename):
    pagenamehyphen = pagename.replace(' ', '_')
    query = requests.get(f'https://en.wikipedia.org/w/api.php?action=query&format=json&titles={pagenamehyphen}&prop=categories')
    data = json.loads(query.text)
    for category in data['query']['pages'][next(iter(data['query']['pages'].keys()))]['categories']:
        catname = category['title']
        if catname == "Category:All disambiguation pages":
            return True
    return False

def getdisambiguationlinks(pagename):
    links = []
    pagenamehyphen = pagename.replace(' ', '_')
    query = requests.get(f'https://en.wikipedia.org/w/api.php?action=query&format=json&titles={pagenamehyphen}&prop=links')
    data = json.loads(query.text)
    for link in data['query']['pages'][next(iter(data['query']['pages'].keys()))]['links']:
        if not link['title'] in [f'Talk:{pagename}', 'Help:Disambiguation']:
            links.append(getredirect(link['title']))
    return links
