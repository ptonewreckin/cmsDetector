# Detects Allinta CMS
# @charlie.campbell @penetrat0r

import requests


def check(header, content, targetURL):	
    if "powered_allinta.gi".upper() in content or 'contenteditable="inherit" start="fileopen"'.upper() in content or "Allinta CMS".upper() in content or "allinta.com".upper() in content:
        return True

