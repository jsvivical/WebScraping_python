#findAll(tag, attributes, recursive, text, limit, keywords)
#find(tag, attributes, recursive, text, keywords)
# HTML페이지에서 원하는 태그를 속성에 따라 쉽게 필터링할 수 있음.

# tag : 태그 이름인 문자열을 넘기거나, 태그 이름으로 이루어진 파이썬 리스트를 넘길 수 있음.
#bs.findAll({'h1', 'h2', 'h3'})

# attributes : 속성으로 이루어진 파이썬 딕셔너리를 받고, 그중 하나를 일치하는 태그를 찾음.
#bs.findAll('span', {'class' : {'green', 'red'}}) html문서에서 녹색과 빨간색 span태그를 모두 반환

#recursive : 문서에서 얼마나 깊이 찾아 들어가고 싶은지 지정하는 불리언, default는 True

#text : 해당 문자열이 몇번 나왔는지 확인
#nameList = bs.findAll(text = 'the prince')
#print(len(nameList))

#limit : 페이지의 항목 중 처음 몇 개헤만 관심이 잇을 때 사용 

#keyword : 특정 속성이 포함된 태그를 선택할 때 사용 
#title = bs.findAll(id = 'title', class_ = 'text')
