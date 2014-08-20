# Detects Sharepoint
# @charlie.campbell @penetrat0r

import requests


def check(header, content, targetURL):	
		if "/_vti_bin/spsdisco.aspx".upper() in content or '%2FPages%2Fdefault'.upper() in content:
			return True
		else:
			if "SharePoint".upper() in header:
			   	return True

