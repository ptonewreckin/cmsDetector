# Detects Joomla CMS
# @penetrat0r

import requests
import re

directories = ["administrator", "joomla.xml", "templates/system/css/template.css", "templates/system/css/system.css"]

def check(header, content, targetURL):
	if "powered by joomla".upper() in content or "Joomla!".upper() in content:
		return True
	else:	
		for directory in directories:
			r = requests.get(targetURL + directory)
			if r.status_code == 200 or r.status_code == 403:
				if "Joomla! Administration Login".upper() in content or "http://www.joomla.org".upper() in content or "joomla".upper() in header:
					return True
				else:
					if directory == "joomla.xml" and r.status_code == 200:
						if "extension version".upper() in content:
							return True
						else:
							if requests.get(targetURL + "notarealpagenotarealpage.php") == 200:
								if "File not found".upper() not in content or "Page not found".upper() not in content:
									return True				

def checkVersion(header, content, targetURL):
	versionURL = ["language/en-GB/en-GB.xml", "templates/system/css/system.css", "media/system/js/mootools-more.js", "templates/system/css/template.css"]

	if '<meta name="Generator" content="Joomla! - Copyright (C) 2005 - 2007 Open Source Matters." />'.upper() in content:
		return "Joomla 1.0"
	elif '<meta name="generator" content="Joomla! 1.5 - Open Source Content Management" />'.upper() in content:
		return "Joomla 1.5"
	else:	
		for url in versionURL:
			r = requests.get(targetURL + url)
			content = str(r.content).upper()
			if r.status_code == 200:
				if url == "language/en-GB/en-GB.xml":
					version = splitXML(content)
					return "Joomla " + version
				elif url == "templates/system/css/system.css":
					if '@version $Id: system.css 20196 2011-01-09'.upper() in content:
						return "Joomla 1.6"
					if '@version $Id: system.css 21322 2011-05-11'.upper() in content:
						return "Joomla 1.7"
					if 'Copyright (C) 2005 - 2012 Open Source Matters'.upper() in content or 'Copyright (C) 2005 - 2013 Open Source Matters'.upper() in content:
						return "Joomla 2.5"
				elif url == "media/system/js/mootools-more.js":
					if "MooTools={version:'1.12'}".upper() in content:
						return "Joomla 1.5"
					if 'MooTools.More={version:"1.3.0.1'.upper() in content:
						return "Joomla 1.6"
					if 'MooTools.More={version:"1.3.2.1'.upper() in content:
						return "Joomla 1.7"
					if 'MooTools.More={version:"1.4.0.1'.upper() in content:
						return "Joomla 2.5.6 or Joomla 3.0 Alpha 2"
				elif url == "templates/system/css/template.css":
					# Newer versions of Joomla do not have this file
					return "Joomla 1.5"
				else:
					return "Joomla CMS - Specific version was unable to be enumerated"

def splitXML(content):
	m=re.compile('<VERSION>(.*?)</VERSION>').search(content)
	return m.group(1)
