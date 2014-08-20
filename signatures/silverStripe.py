# Detects SilverStripe CMS
# @penetrat0r

import requests

directories = ["/Security/login?BackURL=%2Fadmin%2Fpages"]

def check(header, content, targetURL):
    if '<content="SilverStripe'.upper() in content:
        return True
    else:
        for directory in directories:
            try:
                r = requests.get(targetURL + directory)
                content = str(r.content).upper()
                if r.status_code == 200:
                    if 'content="SilverStripe'.upper() in content:
                        return True
            except Exception:
                pass


