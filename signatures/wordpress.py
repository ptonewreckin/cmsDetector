# Detects WordPress CMS
# @penetrat0r
#
# Need to add in additional logic within the directory check.  Search for cookies within the listed directories.
# wp-content/ wp-admin/   wp-login.php and /wp-content/themes/master/style.css
# magnoliaav.com is now wordpress

import requests

directories = ["wp-admin/", "wp-content/", "wp-login/", "wp/", "blog/"]

def check(header, content, targetURL):
    if "wordpress_test_cookie".upper() in header or 'content="Wordpress'.upper() in content or "<!-- end of wordpress head -->".upper() in content or "wp-content".upper() in content:
        return True
    else:
        for directory in directories:
            try:
                r = requests.get(targetURL + directory)
                content = str(r.content).upper()
                if r.status_code == 200:
                    if "Powered by WordPress".upper() in content or "wp-content".upper() in content or "wp-includes".upper in content:
                        return True
            except Exception:
                pass

def checkVersion(header, content, targetURL):
    versionURL = ["/","wp-admin/", "wp-content/", "wp-login/", "wp/", "blog/"]

    for url in versionURL:
        r = requests.get(targetURL + url)
        content = str(r.content).upper()
        if r.status_code == 200:
            try:
                print "testing wordpress version"
                version = splitXML(content)
                return "WordPress " + version
            except Exception:
                pass  

def splitXML(content):
    print "testing splitter"
    m = re.compile('<meta name="generator(.*?)/>').search(content)
    print m.group(1)
    print "testing splitter 2 "
    #print m
    #y = m.group(1).split(" ")
    #print y
    #x = y[1]
    #z = x.split('"')
    #return z[0]