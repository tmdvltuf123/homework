from myTurtle import * # 우리가 만든 myTurtle.py의 모든 기능을 가져옴
import turtle

## 전역 변수 선언 ##
inStr = ''
swidth, sheight = 300, 300
tX, tY, tAngle, tSize = [0] * 4

## 메인 코드 부분 ##
turtle.title('거북이 글자쓰기(모듈버전)')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup() # 선이 그려지지 않게 펜을 올림
turtle.speed(5)

inStr = getString() # 1단계의 문자열 입력 함수 호출

# 입력받은 문자열을 한 글자씩 반복하며 그리기
for ch in inStr :
    # 무작위 위치, 각도, 크기 가져오기
    tX, tY, tAngle, tSize = getXYAS(swidth, sheight)
    # 무작위 색상 가져오기
    r, g, b = getRGB()
    
    turtle.goto(tX, tY)       # 거북이를 무작위 위치로 이동
    turtle.left(tAngle)      # 거북이를 무작위 각도로 회전
    turtle.pencolor((r, g, b)) # 글자 색상 설정
    
    # 글자 쓰기 (폰트, 크기, 굵기 설정)
    turtle.write(ch, font=('맑은 고딕', tSize, 'bold'))

turtle.done()