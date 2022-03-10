# WiFiLoginExample
While working at the hotel and living on site, access to the WiFi in my apartment required login via a pop up window at every connect.
I got around this by investigating the login process, finding a python module that handled this for the brand of router used (Mikrotik) and implementing a python file to connect/test, a batch file to run it at will and a scheduled task to automatically run it at every login of my machine.

# mikrotik.py
This is the core python file which handles the login

# vue_login.bat
This is an easily runnable container for the python file, with a pause to be able to see the results

# Vue Login.xml
This is the scheduled task for importing to Windows, which runs the .bat at every startup

# Vue Login.lnk
This is the shortcut for running at will, pointing to the .bat file

# vue.ico
An icon to make it look better on my desktop
