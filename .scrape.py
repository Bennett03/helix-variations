#scrapes content from trinket.io web editor to main.py
#https://stackoverflow.com/questions/2081586/web-scraping-with-python
#https://stackoverflow.com/questions/1393324/in-python-given-a-url-to-a-text-file-what-is-the-simplest-way-to-read-the-cont

import re
import requests
import json

#get url from README.md




url = "https://trinket.io/embed/glowscript/4e40208104"
#url = url + "&inLibrary=true"

#get the html from the url
#html = urllib.request.urlopen(url).read()
html = requests.get(url).text
#get trinketObject.content from html 

trinketObject = re.search('trinketObject = (.*);', html).group(1)
trinketObject = json.loads(trinketObject)
python = trinketObject['code']
print(python)

#print datatype
print(type(trinketObject))
#write html to file
f = open("main.py", "w")
f.write(str(python))
f.close()