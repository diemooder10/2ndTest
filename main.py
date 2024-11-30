import dataModule  # 팀원 A의 파일 입출력 모듈
import graphDrawerModule  # 팀원 B의 그래프 생성 모듈

def main():
    print("===== 수능 데이터 분석 프로그램 =====")
    print("과목별 점수 분포 그래프를 확인하려면 과목명을 입력하세요.")
    print("프로그램을 종료하려면 '종료'를 입력하세요.")
    

    while True:
        subject = input("과목명을 입력하세요 (예: 국어, 수학, 영어) 또는 '종료': ")
        if subject.strip() == "종료":
            print("프로그램을 종료합니다.")
            break
        
        # 데이터 가져오기 및 그래프 그리기
        try:
            graphDrawerModule.drawGraph(subject)
        
        except ValueError as e:
            print(f"데이터 처리 중 오류가 발생했습니다: {e}")
        except Exception as e:
            print(f"예상치 못한 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()
