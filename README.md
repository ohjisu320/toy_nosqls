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