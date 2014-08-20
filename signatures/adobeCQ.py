# Detects Magento CMS
# @penetrat0r
# Need to add version checks
# Detects Adobe CQ
# @MR AWESOME

import requests

directories = ["apps/cq/personalization/","/content/wiki"]

def check(header, content, targetURL):
    if 'cq-colctrl'.upper() in content:
        return "Adobe CQ"
    else:
        for directory in directories:
            try:
                r = requests.get(targetURL + directory)
                content = str(r.content).upper()
                if r.status_code == 200:
                    if "version %wiki.version%'".upper() in content:
                        return "Adobe CQ"
            except Exception as e:
                print (e)
                pass