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

def user_interface ():

    list_col_questions=list(col_questions.find({}))
    question = list(col_questions.find({}))
    answer = list(col_answers.find({}))
    col_questions.find({},{})
    list_id=list(col_questions.find({},{"question":1}))
    list_question =[]
    list_score = list(col_questions.find({},{"score":1}))
    list_scores = []
    for i in range(len(list_id)) :
        list_question.append(list_id[i]["question"])
        list_scores.append(list_score[i]["score"])
    
    while True :
        list_user_answer=[]
        username=input("User name : ")  
        question = list(col_questions.find({}))
        for i in range(len(question)): # 질문 갯수만큼 반복
            # db에서 받은 값 프린트
            # print(str(x+1) + ". " + question[x]["question"]) # 질문 출력
            print("{}. {}".format(i+1, question[i]["question"])) # 질문 출력
            answer_count = 0 # answer 5개 나올수 있는 카운트 변수
            answer = list(col_answers.find({}))
            for j in range(len(answer)): # list화된 answer 갯수만큼 반복
                if answer_count < 5:  # 5개의 answer 만 출력할수 있게 조건문 
                    answers = answer[j]
                    print(" "+str(answer_count+1) + ") " + answers["answer"]) # 답항 출력
                    answer_count += 1 # 하나씩 추가
                else:
                    break  # 이미 5개를 출력했으므로 루프를 중단하고 다음 user_question으로 넘어갑니다.
            user_answer=int(input("Answer : ")) #사용자의 입력 값 인풋
            list_user_answer.append(user_answer)

            
        for i in range(len(list_col_questions)):
                question = list_col_questions[i]["question"]
                answer = list_user_answer[i]
                score = int(list_scores[i])
                col_users.insert_one({"user_name": username, "question": question, "user_answer": answer, "score":score})
        
        endsign=input("종료하려면 x : ")
        if endsign!='x':    
            pass
        elif endsign=='x':
            break
        pass
user_interface()




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