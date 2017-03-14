cmsDetector
===========

This project is designed to enumerate back-end hosting Content Management Systems and aid security professionals in detecting vulnerabilities within them.

Example Syntax and Output:

The '-e' flag queries Exploit-db for known vulnerabilities of the discovered CMS. It is still experimental but I'm working to add more functionality to it across all modules.

python cmsDetector.py http://www.somesitehere.com -e
