import wikipedia
import wptools

#Special behaviour for when a disambiguation style page comes up maybe?
# - I can confirm this via categories
def getpagename(place):
    search_results = wikipedia.search(f"Flag of {place}")
    return selectflagpage(place, search_results)

def selectflagpage(place, results):
    for result in results:
        if "flag of" in result.lower():
            return result
    for result in results:
        if "coat of arms" in result.lower():
            return result

def getflagurl(pagename):
    page = wptools.page(pagename)
    page.get_restbase('/page/summary/')
    return page.data['image'][0]['url']
