# Detects GetSimple CMS 
# @penetrat0r
#
# GetSimple is vulnerable to a number of remote command execution exploits.  This would be a great candidate for 
# implementing the "-e" flag to enable automated exploitation.

import requests

directories = ["admin/"]

def check(header, content, targetURL):
	if "GetSimpleCMS".upper() in content:
		return True
	else:	
		for directory in directories:
			r = requests.get(targetURL + directory)
			if r.status_code == 200:
				if "GetSimple CMS".upper() in content or "getsimple.js".upper() in content or 'content="GetSimple'.upper() in content:
					return True


