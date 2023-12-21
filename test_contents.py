# 안녕하세요! 프로그래밍 관련 문제를 만들어 드리겠습니다. 다양한 주제에서 문제를 선정해 보겠습니다.
# 다음 중 Python 언어의 특징이 아닌 것은 무엇인가요? 
# 1) 간결하고 읽기 쉬운 문법
# 2) 객체 지향적 프로그래밍 지원
# 3) 메모리 관리가 수동적으로 이루어짐
# 4) 동적 타이핑 지원
# 5) 광범위한 표준 라이브러리 제공
# 20
# 3

# HTML에서 웹페이지의 제목을 설정하는 태그는 무엇인가요?
# 1) <head>2) <title>3) <h1>4) <body> 5) <p>
# 30
# 2

# 다음 중 Java 언어에서 'final' 키워드의 역할로 틀린 것은 무엇인가요? 15
# 1) 변수: 한번 초기화하면 값 변경 불가
# 2) 메소드: 오버라이딩(재정의) 불가
# 3) 클래스: 상속 불가
# 4) 배열: 배열의 크기 변경 불가
# 5) 모든 위의 사항들
# # 15
# 4

# SQL에서 테이블의 데이터를 조회하는 명령어는 무엇인가요? 20
# 1) INSERT2) UPDATE3) DELETE4) SELECT5) CREATE
# 4
# 20

# 다음 중 JavaScript에서 비동기 처리를 위한 객체는 무엇인가요? 15
# 1) Callback 2) Promise 3) Async/Await 4) jQuery 5) 모든 위의 사항들
# 5
# 15

# 정답:32445문제 풀이 잘 해보세요!
# 코드 기본 형식
# import 시 주로 사용하는 방식
# from classes_formats import Person, Arithmetics, Class_name
# class basic format

# class Class_name :
#     def __init__(self) : # 생성자
#         pass
#     def function_name(self) :  # self 키워드 필요(class 소속 확인용)
#         try :
#             pass    # 업무 코드
#         except :
#             pass    # 업무 코드 문제 발생 시 대처 코드(수정하기 위해 쓰일 때도 있음.)
#         finally :
#             pass    # try나 except가 끝난 후 무조건 실행되는 코드
#         return 0
# # 기본 function 형식 - :을 통해 불릴 때만 기능함
# def function_name():
#     try :
#         pass    # 업무 코드
#     except :
#         pass    # 업무 코드 문제 발생 시 대처 코드(수정하기 위해 쓰일 때도 있음.)
#     finally :
#         pass    # try나 except가 끝난 후 무조건 실행되는 코드
#     return 0
# if __name__=="__main__":
#     # 기본 구문
#     try :
#         pass    # 업무 코드
#     except :
#         pass    # 업무 코드 문제 발생 시 대처 코드(수정하기 위해 쓰일 때도 있음.)
#     finally :
#         pass    # try나 except가 끝난 후 무조건 실행되는 코드

def dbconnect(collection_name):
    from pymongo import MongoClient
    # mongodb 에 접속 -> 자원에 대한 class
    mongoclient = MongoClient("mongodb://192.168.10.235:27017")
    database = mongoclient["toy_nosqls"]
    # collection 작업 
    collection = database[collection_name]
    collection.delete_many({})
    return collection


def make_test() :
    question_num=int(input("문제 개수를 입력하세요 : "))
    answer_num=int(input("선택지 개수를 입력하세요 : "))

    print("문제와 선택지를 입력하세요.")
    list_question=[]
    list_answer=[]
    col_questions=dbconnect('questions')
    col_answers=dbconnect('answers')
    for x in range(question_num) :
        question=input("문제{} : ".format(x+1))    
        answer_list = []
        for y in range(answer_num) :
            answer=input("선택지{} : ".format(y+1))       
            answer_list.append(answer)
            
        score=input("점수 : ")
        correct=input("정답  : ")    
        question_result=col_questions.insert_one({"question":question, "score":score, "correct":correct})
        question_id=question_result.inserted_id

        for answer in answer_list:
            col_answers.insert_one({"answer":answer, "question_id":question_id})
        pass



# for x in range(question_num) :
#     question=input("문제{} : ".format(x+1))
#     for y in range(answer_num) :
#         answer=input("문항{} : ".format(y+1))
#         col_answers=dbconnect('answers')
#         col_answers.insert_one({"answer":answer})
#     score=input("점수 : ")
#     correct=input("정답  : ")
#     col_questions=dbconnect('questions')
#     col_questions.insert_one({"question":question, "score":score, "correct":correct})
pass