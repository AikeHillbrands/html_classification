

from bs4 import BeautifulSoup as Soup
import requests
from make_data import get_all_data
import pandas as pd

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

def unpack_nested_dict(d):
    res = {}
    for key,value in d.items():
        if isinstance(value,dict):
            for k,v in value.items():
                res[key+"_"+k] = v
        else:
            res[key] = value

    return res

def propergate_embeddings(soup,depth = 0,parents = {},y_pos = 0):
    all_children_counts = {}
    direct_children_counts = {}

    embeddings = {}
    embeddings["y_pos"] = y_pos

    if soup.children:
        for child in soup.children:
            if child.name:
                add_to_dict(direct_children_counts,child.name)
                add_to_dict(all_children_counts,child.name)
                all_children_counts = add_dicts(all_children_counts,propergate_embeddings(child,depth+1,parents = add_dicts(parents,{soup.name:1}),y_pos=y_pos))
                y_pos += 1
                pass

    embeddings["direct_word_count"] = len((soup.find(text=True,recursive = False) or "").split())
    embeddings["all_word_count"] = len(soup.text.split())
    
    embeddings["child_counts"] = all_children_counts
    embeddings["direct_child_counts"] = direct_children_counts
    embeddings["class"] = {soup.name:1}
    embeddings["depth"] = depth
    embeddings["parents"] = parents
    
    soup.embeddings = unpack_nested_dict(embeddings)


    return all_children_counts

def set_label(soups,label):
    for soup in soups:
        soup.label = label





soups = get_all_data()

labeled_and_classified  =[]

for soup in soups:
    propergate_embeddings(soup)

    labeled_and_classified += soup.find_all()

df = pd.DataFrame([s.embedding for s in soups])

df["label"] = [s.label for s in soups]

pass