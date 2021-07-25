# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Name     : inline-tube-mate [ Telegram ]
# Repo     : https://github.com/vijayanvishnu641/inine-tube-mate
# Author   : Modrepos [ https://t.me/modrepos ]

from youtubesearchpython import *

async def youtube_search(query):
    search = VideosSearch(query)
    result = search.result()['result']
    return result

async def yt_link_search(url):
    videoInfo = Video.getInfo(url, mode=ResultMode.dict)
    return videoInfo

