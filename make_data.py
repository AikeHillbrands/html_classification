import requests
from bs4 import BeautifulSoup as Soup


def set_label(soups,label):
    for soup in soups:
        soup.label = label




test_urls = [
    "https://www.theguardian.com/media/newspapers",
    "https://www.spiegel.de/",
    "https://www.handelsblatt.com/?navi=HOME_21148818",
    "https://www.faz.net/aktuell/"
]


labled = []


def find_and_label(url,query_labels):
    soup = Soup(requests.get(url).content,"lxml").find("body")
    
    for (label,selector) in query_labels:
        soups = soup.select(selector)
        set_label(soups,label)
    return soup

labels = [
    ("https://www.rhein-zeitung.de/sport/fussball-regional/fussballverband-rheinland/fussball-rheinlandliga.html",[
        ["article","article"],
        ["title","h2[class='teaser__headline']"]
        ]),
    ("https://www.theguardian.com/media/newspapers",[
        ["article","div[class='fc-item__content']"],
        ["title","div[class='fc-item__content']"]
        ]),
    ("https://www.spiegel.de/",[
        ["article","article"],
        ["title","header"]
        ]),
    ("https://www.handelsblatt.com/?navi=HOME_21148818",[
        ["article","div[class='o-teasers__item']"],
        ["title",'div[class="c-teaser__title"] > h3']
        ]),
    ("https://www.faz.net/aktuell/",[
        ["article","article"],
        ["title","span[class='tsr-Base_HeadlineText']"]
        ]),
    ("https://11er-online.de/",[
        ["article","div[class='rs_teaser_container']"],
        ["title","div[class='rs_headline']"]
        ]),
    ("https://www.blick-aktuell.de/Bad-Neuenahr/Sport",[
        ["article","article"],
        ["title","h2 > a"]
        ]),
    ("https://www.ak-kurier.de/akkurier/www/67-sport.html",[
        ["article","article > div[class='uk-clearfix'] > div"],
        ["title","div > p[class='rubric-headline-secondary']"]
        ]),
    ("https://www.nr-kurier.de/67-sport.html",[
        ["article","article > div[class='uk-clearfix'] > div"],
        ["title","div > p[class='rubric-headline-secondary']"]
        ]),
    ("https://www.siegener-zeitung.de/tag/fu%C3%9Fball-rheinlandliga",[
        ["article","article"],
        ["title","div > h3[class='article-card-headline']"]
        ]),
    ("https://www.kicker.de/",[
        ["article","div[class='kick__modul__item']"],
        ["title","a > h3"]
        ]),
]

soups = []

for l in labels:

    soups+= (find_and_label(*l)).find_all()

pass