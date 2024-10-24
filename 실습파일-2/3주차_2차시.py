
#3-2
#3-1차시 이어서 진행
#뉴스명, 언론사명, 뉴스링크, 시간, 분 DF 만들기
import pandas as pd
news_name_list = []
news_link_list = []
press_name_list = []
hour_list = []
minute_list = []

for li in news_li:
    news_name_tag = li.find('a', attrs = {'class' : 'link_txt'})
    press_name_tag = li.find('span', attrs = {'class' : 'info_news'})
    
    news_name = news_name_tag.text
    if press_name_tag != None:
        press_name = press_name_tag.text.split('·')[0]
        hour = press_name_tag.text.split('·')[1].split(':')[0]
        minute = press_name_tag.text.split('·')[1].split(':')[1]
    else:
        press_name = None
    news_link = news_name_tag["href"]
    
    news_name_list.append(news_name)
    press_name_list.append(press_name)
    news_link_list.append(news_link)
    hour_list.append(hour)
    minute_list.append(minute)

#데이터 프레임으로 변환
data = pd.DataFrame({'뉴스명' : news_name_list,
                    '언론사명' : press_name_list,
                    '링크' : news_link_list,
                    '발행 시간' : hour_list,
                    '발행 분' : minute_list})

data.head(10)

#데이터 프레임 자료형 확인
data.info()

#발행 시간 및 발행 분 int 타입으로 변경
data['발행 시간'] = data['발행 시간'].astype(int)
data['발행 분'] = data['발행 분'].astype(int)

#변경된 데이터 및 구조 확인
data.info()

#정규표현식 예제1
import re

text = "궁금한 사항이 있으시다면 010-123-4567 으로 연락주시기 바랍니다."

regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchobj = regex.search(text)
phonenumber = matchobj.group()
print(phonenumber)

#정규표현식 예제2
import re
text = "일등뉴스 이등뉴스 삼등뉴스 안녕ㄴㅠ스"
pattern = r'[가-힣]*[ㄴ]*[ㅠ]*[스]+[가-힣]*'

result = re.findall(pattern, text)

for word in result:
    print("찾은 패턴:", word)

#정규 표현식 예제 3
import re

text = '10 20 30 -20'
pattern = r'-\d*'
matches = re.findall(pattern, text)

for match in matches:
    print("찾은 패턴:", match)