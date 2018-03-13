#!/usr/bin/env python3
# -*- coding: utf-8 -*-


try:
    # For Python 3.0 and later
    import urllib.request
    import json
    with urllib.request.urlopen("http://fucking-great-advice.ru/api/random") as url:
        data = json.loads(url.read().decode())
        #print(data["text"])

except ImportError:
    # Fall back to Python 2's urllib2
    import urllib2
    import json
    response = urllib2.urlopen("http://fucking-great-advice.ru/api/random")
    data = json.load(response)
    #print(data["text"])


#response = urllib.request.urlopen("http://fucking-great-advice.ru/api/random")
#data = json.loads(response.read().decode())
print(data["text"])

