# Detects Amiro
# @charlie.campbell @penetrat0r

import requests

def check(header, content, targetURL):
    if "_mod_files/".upper() in content or "var AMI_SessionData".upper() in content or "var active_module_link".upper() in content:
        return True
    else:
        if "Powered by: Amiro CMS".upper() in content or "www.amirocms.com".upper() in content or "www.amiro.ru".upper() in content:
            return True

                ### for finding version
                ###home&_cv=6.0.4.8#####ttp://www.amiro.ru/
                ###home&_cv=5.14.6.6####http://horsnaroundstables.com/
