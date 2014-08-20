# Detects AutoCMS
# @charlie.campbell @penetrat0r

import requests
directories = ["public_tpl/basic.css"]

def check(header, content, targetURL):
    if "Powered by Auto CMS".upper() in content or "public_tpl/basic.css".upper() in content:
        return True
    else:    
        for directory in directories:
            r = requests.get(targetURL + directory)
            file_contents = str(r.content).upper()
            if r.status_code == 200:
                if 'basic.gif'.upper() in file_contents:
                    return True