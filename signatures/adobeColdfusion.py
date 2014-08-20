# Detects Adobe ColdFusion
# @penetrat0r

import requests
import re

directories = ["CFIDE/administrator/","CFIDE/Administrator/index.cfm"]

def check(header, content, targetURL):
    r = requests.get(targetURL + "CFIDE/adminapi/administrator.cfc?method=getSalt")
    
    if r.status_code == 200:
        if "wddxPacket".upper() in str(r.content).upper():
            print "\n** Potentially serious vulnerability discovered. **"
            print "The URL: /CFIDE/adminapi/administrator.cfc?method=getSalt exposes the following SALT used for password hashing: "
            salt = splitXML(r.content).upper()
            print salt
            return "Adobe ColdFusion"
    else:
        r = requests.get(targetURL)
        if 'ColdFusion Administrator'.upper() in content:
            return "Adobe ColdFusion"
        else:
            for directory in directories:
                try:
                    r = requests.get(targetURL + directory)
                    content = str(r.content).upper()
                    if r.status_code == 200:
                        if "ColdFusion Administrator".upper() in content:
                            return "Adobe ColdFusion"
                except Exception:
                    pass

def splitXML(content):
    m = re.compile('<string>(.*?)</string>').search(content)
    return m.group(1)

# Will add this functionality soon
#def extraResources:
#   urlsOfInterest = ["http://nileshkapoor.blogspot.com/2013/12/coldfusion-10-remote-file-disclosure.html"]