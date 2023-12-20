# 나의 업무
# 1번 업무 끌어와서 문제와 answer 프린트
# 응시자 문제 풀기 : 응시자 이름 입력 -> 문제 풀기 -> 다음 응시자 여부(계속:c, 종료:x)
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
# document_quesiton = col_questions.count_documents({})
# document_answer = col_answers.count_documents({})

# username = input("User name : ")
question = list(col_questions.find({}))
answer = list(col_answers.find({}))

for i in range(len(question)): # 질문 갯수만큼 반복
    questions = question[i]
    print(str(i+1) + ". " + questions["question"]) # 질문 출력
    
    answer_count = 0 # answer 5개 나올수 있는 카운트 변수
    for j in range(len(answer)): # list화된 answer 갯수만큼 반복
        if answer_count < 5:  # 5개의 answer 만 출력할수 있게 조건문 
            answers = answer[j]
            print(" "+str(answer_count+1) + ") " + answers["answer"]) # 답항 출력
            answer_count += 1 # 하나씩 추가
        else:
            break  # 이미 5개를 출력했으므로 루프를 중단하고 다음 user_question으로 넘어갑니다.
    
    print()  # question 사이에 공백을 추가합니다.
    





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