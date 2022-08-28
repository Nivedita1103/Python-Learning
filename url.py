import urllib.request
import webbrowser
weburl=urllib.request.urlopen("http://www.ted.com/")
html=weburl.read()
data=weburl.getcode()
hd=weburl.headers
url=weburl.headers
inf=weburl.info()
print("the url is",url)
print("HTTP status code is:",data)
print("header returned\n",hd)
print("the info() returned:\n",inf)
print("now opening the url",url)
webbrowser.open_new(url)
#pg.157
