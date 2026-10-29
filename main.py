import turtle

# إعداد الشاشة والسلحفاة
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Geometric Shapes Pattern - Turtle")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# ألوان متدرجة ومبهرة
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

# رسم الأشكال المتداخلة
for x in range(360):
    t.color(colors[x % len(colors)])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)  # زاوية الدوران تصنع شكلاً هندسياً متسلسلاً

turtle.done()
