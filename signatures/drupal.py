# Detects Drupal CMS
# @penetrat0r

import requests

directories = ["admin/", "robots.txt"]

def check(header, content, targetURL):
	if "Drupal.settings".upper() in content or "drupal.js".upper() in content:
		return True
	else:	
		for directory in directories:
			r = requests.get(targetURL + directory)
			if r.status_code == 200:
				if directory == "/robots.txt" and "Disallow: /?q=admin/".upper() in content \
				and "Disallow: /?q=comment/reply/".upper() in content \
				and "Disallow: /?q=user/password/".upper() in content \
				and "Disallow: /?q=user/login/".upper() in content:
					return True
