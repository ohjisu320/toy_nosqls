# 나의 업무
# 1번 업무 끌어와서 문제와 answer 프린트

# 몽고db connect
def connect(col_name):
    from pymongo import MongoClient   # mongodb compass 띄우기
    mongoClient = MongoClient("mongodb://192.168.0.14:27017")  # 동철님 mongodb에 connection
    database = mongoClient["toy_nosqls"]  # database 연결하는 변수
    collection = database[col_name]  # collection 작업 변수
    return collection

col_answers=connect('answers')
col_questions=connect('questions')
col_users=connect('users')

# 초기화 시스템
def format(col_name) :
    col_name.delete_many({})
format(col_users)

pass
pass
list_col_questions=list(col_questions.find({}))

while True :
    username=input("User name : ") 
    list_user_answer=[]
    for x in range(len(list_col_questions)) : # 문제 개수 만큼
        # db에서 받은 값 프린트
        user_answer=int(input("Answer : ")) #사용자의 입력 값 인풋
        list_user_answer.append(user_answer)  
    pass
    user_result=col_users.insert_one({"user_name":username, "user_answer":list_user_answer})
    pass




# list_questions = [
#     {'question': '다음 중 Python 언어의 특징이 아닌 것은 무엇인가요?'},
#     {'quesiton': 'HTML에서 웹페이지의 제목을 설정하는 태그는 무엇인가요?'},
#     {'quesiton': '다음 중 Java 언어에서 \'final\' 키워드의 역할로 틀린 것은 무엇인가요?'},
#     {'quesiton': 'SQL에서 테이블의 데이터를 조회하는 명령어는 무엇인가요?'},
#     {'quesiton': '다음 중 JavaScript에서 비동기 처리를 위한 객체는 무엇인가요?'}
# ]
# list_answer = [
#         {'answer':'간결하고 읽기 쉬운 문법'},
#         {'answer':'객체 지향적 프로그래밍 지원'},
#         {'answer':'메모리 관리가 수동적으로 이루어짐'},
#         {'answer':'동적 타이핑 지원'},
#         {'answer':'광범위한 표준 라이브러리 제공}'},
#         {'answer': '<head>'},
#         {'answer':'<title>'},
#         {'answer':'<h1>'},
#         {'answer':'<body>'},
#         {'answer': '<p>'},
#         {'answer': '변수: 한번 초기화하면 값 변경 불가'},
#         {'answer': '메소드: 오버라이딩(재정의) 불가'},
#         {'answer':  '클래스: 상속 불가'},
#         {'answer': '배열: 배열의 크기 변경 불가'},
#         {'answer': '모든 위의 사항들'},
#         {'answer':'INSERT'},
#         {'answer': 'UPDATE'},
#         {'answer': 'DELETE'},
#         {'answer': 'SELECT'},
#         {'answer': 'CREATE'},
#         {'answer': 'Callback'},
#         {'answer': 'Promise'},
#         {'answer': 'Async/Await'},
#         {'answer': 'jQuery'},
#         {'answer': '모든 위의 사항들'}
# ]