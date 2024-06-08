from turtle import *

cat = Turtle()
cat.speed(0)  # устанавливаем максимальную скорость

#  голова животного
cat.begin_fill()
cat.fillcolor("black")
cat.circle(100)

#  уши животины
cat.penup()
cat.goto(50, 150)
cat.setheading(240)
cat.pendown()
cat.begin_fill()
cat.fillcolor("black")
cat.circle(50, -120)
cat.end_fill()

cat.penup()
cat.setheading(60)
cat.goto(-50, 150)
cat.pendown()
cat.begin_fill()
cat.fillcolor("black")
cat.circle(50, 120)
cat.end_fill()

#  глаза 
cat.penup()
cat.goto(-30, 50)
cat.dot(30, "white")
cat.goto(-25, 50)
cat.dot(10, "black")

cat.goto(30, 50)
cat.dot(30, "white")
cat.goto(25, 50)
cat.dot(10, "black")

#  нос 
cat.goto(0, 20)
cat.stamp()

cat.hideturtle()

# Надо, чтобы окно не закрывалось само, а только по клику мышки
cat.screen.exitonclick()
cat.screen.mainloop()