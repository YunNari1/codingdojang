# codingdojang

chapter11: 
range는 인덱싱할 때 ,로 구분/ 리스트를 인덱싱할 때는 :로 구분

chapter12:
dict에서 zip 함수로 키 리스트 값 리스트를 묶을 수 있다.
ex)lux2 = dict(zip(['health', 'mana', 'melee', 'armor],[490, 334,550,18.72]))

chapter24:
금액에서 천단위로 콤마 넣기
ex) '%20s' % format(1493500, ',') # 길이 20, 오른쪽으로 정렬

chapter25: 딕셔너리 응용
- setdefault: 키-값 쌍 추가 ex) x.setdefault('e',100)
- update: 키의 값 수정, 키가 없으면 키-값 쌍 추가 ex) x.update(e=50)
- x.items(): 키-값 쌍을 모두 가져옴