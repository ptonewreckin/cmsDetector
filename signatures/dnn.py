# Detects DNN Software CMS (Formerly Dot Net Nuke)
# @penetrat0r
#
# The script files may not be referenced in all instances on the home page.  The code may look
# redundant but in the test cases it worked correctly given some odd configurations that were found.

import requests

directories = ["login.aspx", "js/dnn.js", "js/dnncore.js"]

def check(header, content, targetURL):
	if "DNNModuleContent".upper() in content or "/js/dnn.js".upper() in content or "/js/dnncore.js".upper() in content:
		return True
	else:	
		for directory in directories:
			r = requests.get(targetURL + directory)
			if r.status_code == 200:
				if "DNNModuleContent".upper() in content or "/js/dnn.js".upper() in content or "/js/dnncore.js".upper() in content:
					return True


				
				
				
