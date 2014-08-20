# Detects Caobox CMS
# @charlie.campbell @penetrat0r

# Need to add further logic for the condition as false positves have been occurring.  Modified code to take out an explicit 200 response, but we should
# set up a sample server and examine the admin page if we can't find one online

import requests

directories = ["dao", "cms/dao"]

def check(header, content, targetURL):
    if "cms/?mod=user&act=login&token=".upper() in header:
        return True
    else:
        for directory in directories:
            r = requests.get(targetURL + directory)
            if r.status_code == 200:
                if "cms/?mod=user&act=login&token=".upper() in header:
                    return True

