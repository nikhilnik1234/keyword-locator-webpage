import urllib.request as urllib
import re
urls = ["https://stackoverflow.com/questions/31019854/typeerror-cant-use-a-string-pattern-on-a-bytes-like-object-in-re-findall",
        "https://www.continuum.net/resources/mspedia/managed-it-services-overview",
        "https://ubtpro.com"]

keywords = ["mAnaged it",
            "courier"]

for url in urls:
    page = urllib.urlopen(url).read().decode('utf-8')
    page = page.lower()
    print("Searching keywords in url - ", url)
    for keyword in keywords:
        i= page.find(keyword.lower())
        if i>=0 :
            print("FOUND - ",keyword)

        else:
            print("NOT FOUND - ",keyword)
    print()
    

