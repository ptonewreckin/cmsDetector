# Detects AB-WEB CMS
# @charlie.campbell @penetrat0r

import requests

def check(header, content, targetURL):	
    if "AB WEB".upper() in content or "bdp_z01_z02_l".upper() in content or "hdp_z01_z03_l".upper() in content or "Imprimer".upper() in content:
        return True	
