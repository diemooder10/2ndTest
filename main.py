import dataModule  # 팀원 A의 파일 입출력 모듈
import graphDrawerModule  # 팀원 B의 그래프 생성 모듈

def main():
    print("===== 수능 데이터 분석 프로그램 =====")
    print("과목별 점수 분포 그래프를 확인하려면 과목명을 입력하세요.")
    print("프로그램을 종료하려면 '종료'를 입력하세요.")
    

    while True:
        try:
            yearinput = int(input("연도를 입력하세요(2023년 데이터만 존재합니다) 또는 0(종료): "))
        except ValueError:
            print("유효하지 않은 입력입니다. 연도를 숫자로 입력해주세요.")
            continue

        # 유효한 연도 확인
        if yearinput == 2023:
            subject = input("과목명을 입력하세요 (예: 국어, 수학, 윤리와 사상) 또는 '종료': ").strip()
            
            
            # 데이터 가져오기 및 그래프 그리기
            try:
                result = graphDrawerModule.drawGraph(subject, yearinput)
                if result:
                    print(result)  # "해당 과목이 없습니다." 출력
            except ValueError as e:
                print(f"데이터 처리 중 오류가 발생했습니다: {e}")
            except FileNotFoundError:
                print("필요한 데이터 파일이 존재하지 않습니다. 파일 경로를 확인하세요.")
            except Exception as e:
                print(f"예상치 못한 오류가 발생했습니다: {e}")
        
        
        elif yearinput == 0:
            print("프로그램을 종료합니다.")
            break
        
        else:
            print("연도를 다시 입력해주세요. 현재 2023년 데이터만 지원됩니다.")


if __name__ == "__main__":
    main()
