# Detects LifeRay CMS
# @penetrat0r

import requests

def check(header, content, targetURL):
    if 'liferay.aui'.upper() in content:
        return True

