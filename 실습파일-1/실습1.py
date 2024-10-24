oecd_cnty={'AUS': '오스트레일리아',
            'KOR': '대한민국',
            'USA': '미국'}

#json파일 저장
import json
with open('ex1.json', 'w') as f:
    # json.dump : 파이썬의 dict 객체를 JSON형태로 변환
    json.dump(oecd_cnty, f)

#json파일 불러오기
import json
with open('ex1.json') as f:
    data = json.load(f)

type(data)

print(data)