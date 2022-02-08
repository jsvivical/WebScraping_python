from urllib.request import urlopen
from urllib.request import HTTPError
import ssl

context = ssl._create_unverified_context()

try:
    html = urlopen(
        "http://www.pythonscraping.com/pages/error.html", context=context)
except HTTPError as e:
    print(e)
    #null을 반환하거나 , break문을 실행하거나, 기타 다른 방법을 사용
    
else :
    # 프로그램을 계속 실행
    #except절에서 return이나 break를 사용했다면 else절은 필요없음.
    
    # HTTPError :  페이지를 찾을 수 없으 때, url해석에서 에러가 생긴 걍우
    #              서버를 찾을 수 없는 경우
    
    #URLError : 해당 웹페이지가 다운, url에 오타 등