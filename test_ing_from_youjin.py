# 나의 업무
# 1번 업무 끌어와서 문제와 answer 프린트

# 몽고db connect
def connect():
    from pymongo import MongoClient   # mongodb compass 띄우기
    mongoClient = MongoClient("mongodb://192.168.0.165:27017")  # 동철님 mongodb에 connection
    database = mongoClient["toy_nosqls"]  # database 연결하는 변수
    collection = database['answers']  # collection 작업 변수
    collection = database['questions']  # collection 작업 변수
    return collection

list_questions = [
    {
        'question': '다음 중 Python 언어의 특징이 아닌 것은 무엇인가요?',
        'answer': [
            '간결하고 읽기 쉬운 문법',
            '객체 지향적 프로그래밍 지원',
            '메모리 관리가 수동적으로 이루어짐',
            '동적 타이핑 지원',
            '광범위한 표준 라이브러리 제공'
        ]
    },
    {
        'quesiton': 'HTML에서 웹페이지의 제목을 설정하는 태그는 무엇인가요?',
        'answer': [
            '<head>',
            '<title>',
            '<h1>',
            '<body>',
            '<p>'
        ]
    },
    {
        'quesiton': '다음 중 Java 언어에서 \'final\' 키워드의 역할로 틀린 것은 무엇인가요?',
        'answer': [
            '변수: 한번 초기화하면 값 변경 불가',
            '메소드: 오버라이딩(재정의) 불가',
            '클래스: 상속 불가',
            '배열: 배열의 크기 변경 불가',
            '모든 위의 사항들'
        ]
    },
    {
        'quesiton': 'SQL에서 테이블의 데이터를 조회하는 명령어는 무엇인가요?',
        'answer': [
            'INSERT',
            'UPDATE',
            'DELETE',
            'SELECT',
            'CREATE'
        ]
    },
    {
        'quesiton': '다음 중 JavaScript에서 비동기 처리를 위한 객체는 무엇인가요?',
        'answer': [
            'Callback',
            'Promise',
            'Async/Await',
            'jQuery',
            '모든 위의 사항들'
        ]
    }
]

username=input("User name : ")
print("문제를 풀어주세요.")
print("문항{}. {}")

for i, question in enumerate(list_questions):
    answer = input("{}에 대한 answer을 입력해주세요: ".format(question[i]['quesiton']))
    user_answers[f"quesiton {i+1}"] = int(answer)

for i, question in enumerate(list_questions):
    print(f"{question['quesiton']}의 정답은 {question['answer'][user_answers[f'quesiton {i+1}']-1]}")

# user_one_answers = {
#     'quesiton 1': 5,
#     'quesiton 2': 3,
#     'quesiton 3': 4,
#     'quesiton 4': 5,
#     'quesiton 5': 1
# }

# user_two_answers = {
#     'quesiton 1': 1,
#     'quesiton 2': 2,
#     'quesiton 3': 2,
#     'quesiton 4': 4,
#     'quesiton 5': 5
# }

## collections_name : users
## column
user_one = 'user_one'
user_two = 'user_two'
user_score = 'user_score'

# for i, question in enumerate(questions):
#     print(f"{question['quesiton']}의 정답은 {question['answer'][user_one_answers[f'quesiton {i+1}']-1]} (사용자1)")
#     print(f"{question['quesiton']}의 정답은 {question['answer'][user_two_answers[f'quesiton {i+1}']-1]} (사용자2)")

# 배점 : 20 30 15 20 15(점)


## collections_name : questions
## column
# 문제 : question
# 정답 : correct
# 배점 : score

## collections_name : answers
## column
# answer : answer
# question_id

## collections_name : result
## column
# user_name
# result_score