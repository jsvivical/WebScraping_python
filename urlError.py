from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError
import ssl

context = ssl._create_unverified_context()

try :
    html = urlopen("https://pythonscrapingthisurldoesnotexist.com", context = context)
except HTTPError as e :
    print(e)
except URLError as e:
    print('the server could not be found!')
else:
    print("it worked!")

#URLError : url다운, url에 오타, 