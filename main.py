from bs4 import BeautifulSoup as Soup
import requests

def add_dicts(dict1,dict2):
    res = {}
    res.update(dict2)
    for key,value in dict1.items():
        if key in res: res[key] += value
        else: res[key] = value
    
    return res

def add_to_dict(dict,key,value = 1):
    if key in dict: dict[key] +=value
    else: dict[key] = value

def children_counts(soup,depth = 0,parents = []):
    res = {}
    if soup.children:
        for child in soup.children:
            if child.name:
                add_to_dict(res,child.name)
                res = add_dicts(res,children_counts(child,depth+1,parents = parents + [soup.name]))
                pass

    soup.embeddings = {}
    soup.embeddings["child_counts"] = res
    soup.embeddings["class"] = {soup.name:1}
    soup.embeddings["depth"] = depth
    soup.embeddings["parents"] = parents


    return res



url = "https://www.rhein-zeitung.de/sport/fussball-regional/fussballverband-rheinland/fussball-rheinlandliga.html"

soup = Soup(requests.get(url).content,"lxml")

children_counts(soup)
pass

