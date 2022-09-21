kor, eng, math, sci = map(int,input().split())

avr = (kor+eng+math+sci)/4

if kor>=0 and kor<=100 and eng>=0 and eng<=100 and math>=0 and math<=100 and sci>=0 and sci<=100:
    if avr>=80:
        print("합격")
    elif avr<80:
        print("불합격")
else:
    print("잘못된 점수")
