def connect(col_name):
    from pymongo import MongoClient   # mongodb compass 띄우기
    mongoClient = MongoClient("mongodb://192.168.10.235:27017")  # 동철님 mongodb에 connection
    database = mongoClient["toy_nosqls"]  # database 연결하는 변수
    collection = database[col_name]  # collection 작업 변수
    return collection
def test_result():
    col_answers=connect('answers')
    col_questions=connect('questions')
    col_users=connect('users')
    col_result = connect('result') # result collection 연결

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
    
    list_user_id=[] # user_id의 묶음
    for i in range(len(list_user_answer)): # range(10)
        list_user_id.append(list_user_answer[i]['_id']) # list_user_id에 list_user_answer에 있는 모든 id값 append
        pass
    for i in range(len(list_user_id)): # range(10)
        col_users.update_many({'_id':list_user_id[i]},{"$set":{'user_score' : user_score[i]}},upsert=True) # users(collection)에 id가 같은 행에 user_score upsert
        pass


    list_user_names=[] # user name들의 list 
    for i in range(int(len(list_user_name)/len(list_answer))): # = range(2)
        user_names=list_user_name[i*len(list_answer)]['user_name'] # list_user_name에 있는 0, 5번째의 user name 추출
        list_user_names.append(user_names) # list_user_names에 append
    

    pass 

    list_result_score=[] # list_result_score를 생성
    for i in range(int(len(list_user_name)/len(list_answer))):  # range(2) 
        # user_score=[0,30,0,20,15,0,0,0,0,0] 일 때, user_score[0]+[1]+[2]+[3]+[4] / [5]+[6]+[7]+[8]+[9] 끼리 합하기 -- 이 부분 =+ 사용해야 함.
        score_result_sum=0
        for x in range(len(list_answer)) :
            score_result=+user_score[x+len(list_answer)*i]
            score_result_sum=score_result_sum+score_result 
        list_result_score.append(score_result_sum)

    for i in range(int(len(list_user_name)/len(list_answer))): 
        # list_user_names=['one','two'] / list_score_result=[65,0]
        # user_name : one / result_score : 65인 행 넣기
        col_result.insert_one({"user_name":list_user_names[i], "result_score":list_result_score[i]})

    for x in range(int(len(list_user_names))):
        print("사용자 : {}".format(list_user_names[x]))
        for y in range(int(len(list_user_answer)/(len(list_user_names)))) :
            print("답항 결과 : {}번 : {}".format(y+1, list_user_answer_sheet[x][y]), end=", "  )      
        print("")
        print("{}의 합산 점수 : {}".format(list_user_names[x],list_result_score[x]))


    






    
