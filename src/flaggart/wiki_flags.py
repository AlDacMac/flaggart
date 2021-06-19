import wikipedia

#Special behaviour for when a disambiguation style page comes up maybe?
def getpage(place):
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
        if result[0:] == "Coat of arms":
            return result