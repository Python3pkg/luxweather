#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'luxweather',
    version = '1.1',
    url = 'https://github.com/mrsmn/LuxWeather',
    download_url = 'https://github.com/mrsmn/LuxWeather/archive/master.zip',
    author = 'mrsmn',
    author_email = 'me@martinsimon.me',
    license = 'Apache v2.0 License',
    packages = ['luxweather'],
    description = 'luxweather is an APACHE licensed Twitter weather bot written in Python',
    long_description = file('README.md','r').read(),
    keywords = ['weather forecast', 'forecast', 'Luxembourg', 'twitter'],
)
