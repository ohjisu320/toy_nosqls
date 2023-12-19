
user_name = ["",""]
user_answer = [[0,0,0,0,0],[0,0,0,0,0]]# one,two 사용자 답항 변수, 추후 초기화
list_answer = [3,2,4,4,5]

list_score = [20,30,15,20,15] # 답항별 점수

#정답 3,2,4,4,5

user_score = [0,0]

# 사용자 입력
for x in range(len(user_name)):
    input_user = input("사용자 이름 : ")
    user_name[x] = input_user

    for i in range(len(user_answer[x])): #문제에 대한 답변 입력
        input_answer = int(input("정답 : "))
        user_answer[x][i] = input_answer

        if user_answer[x][i] == list_answer[i]:
            user_score[x] += list_score[i]   
    
    print("사용자 : {}".format(user_name[x]))
    print("답항 결과 : 1번 : {}, 2번 : {}, 3번 : {}, 4번 : {}, 5번 : {}".format(user_answer[x][0],user_answer[x][1],user_answer[x][2],user_answer[x][3],user_answer[x][4]))
    print("{}의 합산 점수 : {}".format(user_name[x],user_score[x]))
    # user_score = 0
