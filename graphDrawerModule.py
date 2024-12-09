import dataModule
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager

#그래프를 그리는 함수 (과목 이름과 년 받음)
def drawGraph(subject,year):
    #한글 잘 표시하려고 font를 바꾸기
    rc("font", family="AppleGothic")
    try:
        font_manager.findfont("AppleGothic", fallback_to_default=False) #맥에서 문제 없이 실행할 것입니다
    except:
        rc("font", family="Malgun Gothic") #윈도우스이면 지난 코드가 문제가 있을 거라서 이걸로 바꿈

    #데이터 얻기
    data = dataModule.dataGetter(year)

    #부탁한 과목 없으면...
    if(subject not in data):
        return "해당 과목이 없습니다."
    data = data[subject] #해당 과목 정보를 얻기

    #그래프를 그리기
    # 데이터 정리
    man = [int(x.strip()) for x in data["man"]]
    woman = [int(x.strip()) for x in data["woman"]]
    standard_score = [int(x.strip()) for x in data["standard_score"]]

    # 그래프를 설정하기
    plt.figure(figsize=(15, 7))
    plt.plot(standard_score, man, label="남자", marker="o", linestyle="-")
    plt.plot(standard_score, woman, label="여자", marker="o", linestyle="-")

    # 그래프의 문자들
    plt.xlabel("표준편차")
    plt.ylabel("사람 수")
    plt.title(f"{year}학년도 수능 {subject} 과목 분포")
    plt.legend()
    plt.grid()

    # 그래프를 보여주기
    plt.show()