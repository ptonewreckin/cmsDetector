
# Detects Django CMS
# @penetrat0r
# Test site verified http://www.sandmanhotels.com/, http://www.orange.ch/
# Error occurs on http://djangosuit.com/.  I believe its because you aren't allowed to prepend "www".

import requests

directories = ["en/admin/", "admin/"]

def check(header, content, targetURL):
    if "django_language=".upper() in header or "d_lang=".upper() in header:
        return True
    else:
        for directory in directories:
            r = requests.get(targetURL + directory)
            if "Django".upper() in content:
                return True