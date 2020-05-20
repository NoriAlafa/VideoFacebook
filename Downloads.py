import requests
import re
url=input('masukkan url)
req=r.get(url)
video_url=re.search('sd_src:"(.+)"', reqtext).group(1)
short=r.get('https://tinyurl.com/api-create.php?url='+video_url)

print('|||Succes|||')
print('Url Video', short.text)

print('|||Succes|||')
