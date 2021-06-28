import wikipedia
import wptools

#Special behaviour for when a disambiguation style page comes up maybe?
# - I can confirm this via categories
def getpagename(place):
    search_results = wikipedia.search(f"Flag of {place}")
    return selectflagpage(place, search_results)

def selectflagpage(place, results):
    for result in results:
        if "flag of" in result.lower() or "flags of" in result.lower():
            return result
    for result in results:
        if "coat of arms" in result.lower():
            return result

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