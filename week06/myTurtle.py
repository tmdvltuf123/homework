import random
from tkinter.simpledialog import *

# 1. 사용자로부터 문자열을 입력받는 함수
def getString() :
    retStr = ''
    retStr = askstring('문자열 입력', '거북이가 쓸 문자열을 입력하세요')
    return retStr

# 2. 무작위 RGB 색상을 생성하는 함수
def getRGB() :
    r, g, b = 0, 0, 0
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

# 3. 무작위 위치(X, Y), 각도, 글자 크기를 생성하는 함수
def getXYAS(sw, sh) :
    x, y, angle, size = 0, 0, 0, 0
    x = random.randrange(-sw / 2, sw / 2)
    y = random.randrange(-sh / 2, sh / 2)
    angle = random.randrange(0, 360)
    size = random.randrange(10, 50)
    return [x, y, angle, size]