# 한국어 유니코드 인코딩
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 모듈 가져오기
import random

class SuperMonster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def move(self):
        print(f"[{self.name}] {self.name}! 몸통박치기!")

class JiSoo(SuperMonster):
    # 생성자 오버라이딩
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills = ("참기", "전광석화", "폭식하기")

    # 메서드 오버라이드
    def skill(self):
        print(f"[{self.name}] {self.name}! {self.skills[random.randint(2,2)]}!")
    
jisoo = JiSoo("한지수", sys.maxsize, sys.maxsize)
jisoo.move()
jisoo.skill()


