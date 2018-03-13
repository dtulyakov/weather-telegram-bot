#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fga():
    import urllib.request
    import json
    with urllib.request.urlopen("http://fucking-great-advice.ru/api/random") as url:
        data = json.loads(url.read().decode())
        print(data["text"])

fga()
