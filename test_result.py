def connect(col_name):
    from pymongo import MongoClient   # mongodb compass 띄우기
    mongoClient = MongoClient("mongodb://192.168.0.14:27017")  # 동철님 mongodb에 connection
    database = mongoClient["toy_nosqls"]  # database 연결하는 변수
    collection = database[col_name]  # collection 작업 변수
    return collection

col_answers=connect('answers')
col_questions=connect('questions')
col_users=connect('users')
collection = connect('result') # result collection 연결

list_user_name = list(col_users.find({},{"_id":1,"user_name":1})) # 입력한 유저의 id/name 찾기
list_user_answer = list(col_users.find({},{"user_answer":1})) # 유저의 답변 찾기
list_correct = list(col_questions.find({},{"correct":1})) # 문제에 대한 정답 찾기
list_question_score = list(col_questions.find({},{"score":1})) # 문제에 대한 점수


user_name = list_user_name # user 이름 받을 초기화 변수
user_answer = list_user_answer# one,two 사용자 답항 변수, 추후 초기화[1,2,3,4,5,5,4,3,2,1]
list_answer = list_correct # 정답에 대한 인덱스

list_score = list_question_score # 답항별 점수

#정답 3,2,4,4,5

user_score = [] # 점수 초기 변수
list_user_answer_sheet = [] #user_answer를 user별로 넣을 리스트 생성
num_repeat = len(user_name)/len(list_answer)
    # 사용자 입력 및 점수 계산
for x in range(int(num_repeat)): #range 값이 : 2로된다
    list_answer_sheet = []
    for y in range(len(list_answer)): # range(len(list_answer)) = 5로된다
        list_answer_sheet.append(user_answer[5*x + y]["user_answer"]) # 
    
    list_user_answer_sheet.append(list_answer_sheet)
    
for x in range(int(num_repeat)): # 연산 시켜주는 구문
    for y in range(len(list_answer)):
        if list_user_answer_sheet[x][y] ==  int(list_answer[y]['correct']):
            user_score.append(int(list_score[y]['score']))
        else:
            user_score.append(0)
        pass

for x in range(10):
    col_users.update_one({},{{"$set" : {"user_score":user_score[x]}}})


    
# print(list_user_answer_sheet)

        # if list_answer[y] == user_answer[5*x + y]:

    # for i in range(len(user_answer[x])): #문제에 대한 답변 입력
            
    #     if user_answer[x]["user_answer"] == list_answer[i]:
    #        user_score[x] += list_score[i]   
        
    #     print("사용자 : {}".format(user_name[x]))
    #     print("답항 결과 : 1번 : {}, 2번 : {}, 3번 : {}, 4번 : {}, 5번 : {}".format(user_answer[x]["user_answer"],user_answer[x]["user_answer"],user_answer[x]["user_answer"],user_answer[x]["user_answer"],user_answer[x]["user_answer"]))
    #     print("{}의 합산 점수 : {}".format(user_name[x],user_score[x]))
    #     # user_score = 0

    # print("{}의 합산 점수 : {}".format(user_name[0],user_score[0]))
    # print("{}의 합산 점수 : {}".format(user_name[1],user_score[1]))

    
