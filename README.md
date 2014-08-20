cmsDetector
===========

This project is designed to enumerate back-end hosting Content Management Systems and aid security professionals in detecting vulnerabilities within them.

Example Syntax and Output:

The '-e' flag queries Exploit-db for known vulnerabilities of the discovered CMS. It is still experimental but I'm working to add more functionality to it across all modules.

python cmsDetector.py http://www.somesitehere.com -e


  ______ .___  ___.      _______. _______   _______ .___________. _______   ______ .___________.  ______   .______      
 /      ||   \/   |     /       ||       \ |   ____||           ||   ____| /      ||           | /  __  \  |   _  \     
|  ,----'|  \  /  |    |   (----`|  .--.  ||  |__   `---|  |----`|  |__   |  ,----'`---|  |----`|  |  |  | |  |_)  |    
|  |     |  |\/|  |     \   \    |  |  |  ||   __|      |  |     |   __|  |  |         |  |     |  |  |  | |      /     
|  `----.|  |  |  | .----)   |   |  '--'  ||  |____     |  |     |  |____ |  `----.    |  |     |  `--'  | |  |\  \----.
 \______||__|  |__| |_______/    |_______/ |_______|    |__|     |_______| \______|    |__|      \______/  | _| `._____|


[*] Enumeration is enabled...
[Stage One] cmsDetector is currently analyzing the application...

** Potentially serious vulnerability discovered.  The /app/etc/local.xml configuration file is exposed to the internet. **

   >> MAGENTO

[Stage Two] Enumerating other potential vulnerabilities..

[**] ExploitDB has returned the following potential exploits:

   >> Magento eCommerce Local File Disclosure
   >> Magento 1.2 app/code/core/Mage/Admin/Model/Session.php login[username] Parameter XSS 
   >> Magento 1.2 app/code/core/Mage/Adminhtml/controllers/IndexController.php email Parameter XSS 
   >> Magento 1.2 downloader/index.php URL XSS


[***] Detection took: 12.3 seconds 
