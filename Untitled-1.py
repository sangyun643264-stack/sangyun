
def gugudan():
    num = int(input("몇 단을 입력할까요? "))

    print(f"\n[{num}단]")
    
    for i in range(1, 10):
        print(f"{num} x {i} = {num * i}")


gugudan()

import turtle
import colorsys

# 화면 설정
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rainbow Galaxy Mandala")
screen.setup(900, 900)
screen.tracer(0)

# 거북이 설정
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# 무지개 만다라 그리기
for i in range(360):
    hue = i / 360
    color = colorsys.hsv_to_rgb(hue, 1, 1)

    t.pencolor(color)
    t.circle(150)
    t.left(59)
    t.circle(150)
    t.left(61)

    t.right(10)
    screen.update()

# 마무리
screen.update()
turtle.done()
