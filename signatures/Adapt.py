# Detects Adapt CMS
# @charlie.campbell @penetrat0r

import requests


def check(header, content, targetURL):    
    if "adaptcms".upper() in header:
        return True    
    else:
        if "AdaptCMS".upper() in content or "www.adaptcms.com".upper() in content:
            return True
            
