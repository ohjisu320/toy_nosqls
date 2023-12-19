# 나의 업무
# 1번 업무 끌어와서 문제와 answer 프린트
# 지수님 : input 받아 넣기

# 몽고db connect
def connect(col_name):
    from pymongo import MongoClient   # mongodb compass 띄우기
    mongoClient = MongoClient("mongodb://192.168.0.14:27017")  # 지수님 mongodb에 connection
    database = mongoClient["toy_nosqls"]  # database 연결하는 변수
    collection = database[col_name]  # collection 작업 변수
    return collection

col_answers=connect('answers')
col_questions=connect('questions')
col_users=connect('users')

# 초기화 시스템
def format(col_name) :
    col_name.find({})
format(col_users)


#while문으로 감싸줄 예정!

# username= 'user_one'
username = input("User name : ")
print("문제를 풀어주세요:")
print()





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