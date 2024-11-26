#파일 입출력 및 관련 데이터 리스트,딕셔너리화
import csv

with open('20231231.csv') as f:
 reader = csv.reader(f)
 header = reader.__next__()
 data = [row for row in reader]
# 첫 줄 분리하기(헤더이므로)

result = {}
for row in data:
    subject = row[1]  # 현재 과목명
    man = row[3]  # 남성 데이터
    woman = row[4]# 여성 데이터
    standard_score=row[2]

    if subject not in result:
        result[subject] = {'man': [], 'woman': [],'standard_score':[]}  # 과목별 초기 구조 생성

    # 남성과 여성 데이터를 추가
    result[subject]['man'].append(man)
    result[subject]['woman'].append(woman)
    result[subject]['standard_score'].append(standard_score)
