#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'luxweather',
    version = '1.0',
    url = 'https://github.com/c0ding/LuxWeather',
    download_url = 'https://github.com/c0ding/LuxWeather/archive/master.zip',
    author = 'c0ding',
    author_email = 'me@martinsimon.me',
    license = 'Apache v2.0 License',
    packages = ['luxweather'],
    description = 'D\'Lëtzebuerger Wieder op Twitter. Refresh ass all Stonn. Mat vill ♥ geschriwwen vum @c0ding',
    long_description = file('README.md','r').read(),
    keywords = ['weather forecast', 'forecast', 'Yahoo Weather', 'Luxembourg'],
)
