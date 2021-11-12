a = []

day1 = int(input("1일차 턱걸이 횟수>>>"))
a.append(day1)
day2 = int(input("2일차 턱걸이 횟수>>>"))
a.append(day2)
day3 = int(input("3일차 턱걸이 횟수>>>"))
a.append(day3)
day4 = int(input("4일차 턱걸이 횟수>>>"))
a.append(day4)
day5 = int(input("5일차 턱걸이 횟수>>>"))
a.append(day5)
day6 = int(input("6일차 턱걸이 횟수>>>"))
a.append(day6)
day7 = int(input("7일차 턱걸이 횟수>>>"))
a.append(day7)

avg = (day1 + day2 + day3 + day4 + day5 + day6 + day7)/len(a)
print(avg)