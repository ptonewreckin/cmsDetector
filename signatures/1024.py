# Detects 1024 CMS
# @charlie.campbell @penetrat0r

import requests

directories = ["index.php"]

def check(header, content, targetURL):
    if "1024 CMS".upper() in content or "otatfpowered".upper() in content or "includes/admin_default_ajax.js".upper() in content:
        return True    
