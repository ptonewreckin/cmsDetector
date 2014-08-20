# Detects Hippo CMS
# @penetrat0r
# Hippo doesn't appear to have any special attributes on it's login form.  

import requests

def check(header, content, targetURL):
	if "Hippo &copy".upper() in content or 'content="Hippo,'.upper() in content:
		return True

