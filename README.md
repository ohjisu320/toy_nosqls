# 역할분담
|이름|역할|
|--|--|
|한동철|문제 제출자 작성 하기|
|김유진|응시자 문제 풀기-db에서 find|
|오지수|응시자 문제 풀기-db에 insert|
|공명윤|통계|

## 컬렉션 정보

### 컬렉션 이름
|이름|역할|
|--|--|
|questions|question(문제)/correct(정답)/score(배점) 저장|
|answers|answer(답항), question_id 저장|
|users|user_name, user_answer, user_score 저장|
|results|user_name, result_score 저장|

### 컬럼 이름
|이름|역할|
|--|--|
|question|문제|
|correct|정답|
|score|배점|
|answer|답항|
|question_id|question collection에 있는 question에 대한 id|
|user_name|사용자 이름|
|user_answer|사용자의 답항|
|user_score|사용자 문제에 대한 배점|
|result_score|user 별 총점|

## class/function/변수 정보

### class 이름
|이름|역할|
|--|--|


### function 이름
|이름|역할|
|--|--|
|dbconnect()|db에 연결|
|make_test()|문제 제출자 인터페이스|
|format()|db에 넣은 값을 초기화|
|user_interface()|문제 풀이 인터페이스|
|user_interface()|문제 채점 시스템|

### 변수 이름

#### file : test_contents.py

|이름|역할|
|--|--|
|question_num|출제할 문제의 개수|
|answer_num|출제할 선택지의 개수|
|col_questions|collection이름이 questions인 collection 생성(접속)|
|col_answers|collection이름이 answers collection 생성(접속)|
|question|출제자가 문제를 입력한 값|
|answer|출제자가 문제를 입력한 값|
|answer_list|출제자가 문제를 입력한 값들의 list|
|score|출제한 문제의 배점(점수)|
|correct|출제한 문제의 정답|
|question_result|col_questions에 question값, score값, correct값이 한 행씩 insert한 결과값|
|question_id|question_result의 행별 id값 ?? 의미 없는 듯 함.|


#### file : test_ing_merged.py

|이름|역할|
|--|--|
|col_questions|collection이름이 questions인 collection 생성(접속)|
|col_answers|collection이름이 answers인 collection 생성(접속)|
|col_users|collection이름이 users인 collection 생성(접속)|
|list_row|col_questions에서 "question"과 "score" 의 dictionary를 list화 한 것|
|list_question|출제자가 입력한 문제들을 묶을 list|
|list_scores|출제자가 입력한 배점들을 묶을 list|


#### file : test_contents.py

|이름|역할|
|--|--|
|make_test()|문제 제출자 인터페이스|
|user_interface()|문제 풀이 인터페이스|
|user_interface()|문제 채점 시스템|