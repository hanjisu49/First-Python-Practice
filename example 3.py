kor_score = int(input("국어>>>"))
math_score = int(input("수학>>>"))
eng_score = int(input("영어>>>"))

if 0 <= kor_score <= 100 and 0<= math_score <= 100 and 0<= eng_score <= 100:
    if kor_score >= 80 or math_score >= 80 or eng_score >= 80:
        print("불합격")
    else:
        print("합격")
else:
    print("잘못 입력하였습니다.")
