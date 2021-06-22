import wikipedia
import wptools

#Special behaviour for when a disambiguation style page comes up maybe?
# - I can confirm this via categories
def getpagename(place):
    search_results = wikipedia.search(f"Flag of {place}")
    return selectflagpage(place, search_results)

def selectflagpage(place, results):
    for result in results:
        if result[0:7] == "Flag of":
            return result
        elif result[-4:] == "Flag":
            return result
        elif result[0:7] == "Flags of":
            return result
    for result in results:
        if result[0:12] == "Coat of Arms":
            return result

def getflagurl(pagename):
    page = wptools.page(pagename)
    page.get_restbase('/page/summary/')
    return page.data['image'][0]['url']
