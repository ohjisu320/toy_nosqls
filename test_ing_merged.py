def connect(col_name):
    from pymongo import MongoClient   # mongodb compass 띄우기
    mongoClient = MongoClient("mongodb://192.168.10.235:27017") 
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
    list_row=list(col_questions.find({},{"question":1, "score":1}))
    list_question =[]
    list_scores = []
    pass
    for i in range(len(list_row)) :
        list_question.append(list_row[i]["question"])
        list_scores.append(list_row[i]["score"])
    
    while True :
        list_user_answer=[]
        username=input("User name : ")  
        list_col_questions = list(col_questions.find({}))
        for i in range(len(list_col_questions)): # 질문 갯수만큼 반복
            # db에서 받은 값 프린트
            # print(str(x+1) + ". " + question[x]["question"]) # 질문 출력
            print("{}. {}".format(i+1, list_col_questions[i]["question"])) # 질문 출력
            answer_count = 0 # answer 5개 나올수 있는 카운트 변수
            list_col_answers = list(col_answers.find({}))
            for j in range(len(list_col_answers)): # list화된 answer 갯수만큼 반복
                if answer_count < 5:  # 5개의 answer 만 출력할수 있게 조건문 
                    answers = list_col_answers[j]
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

user_interface ()


