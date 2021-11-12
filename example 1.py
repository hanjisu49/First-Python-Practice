# 실습문제 5.1.1
sub_count = int(input("현재 구독자 수를 입력하세요>>>"))

if sub_count >= 1000:
     print("수익 창출이 가능합니다!")
else:
     print("수익 창출이 불가능합니다!")

# 실습문제 5.1.2
time = int(input("공부시간을 입력하세요(시간)>>>"))

if time >= 10:
    print("휴대폰 잠금이 해제 됩니다.")
elif time >= 5:
    print("휴대폰을 30분간 사용가능 합니다.")
else:
    print("휴대폰 사용이 불가능합니다.")