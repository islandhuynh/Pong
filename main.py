from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong by Island Huynh")

player_paddle = Paddle()

screen.onkey(player_paddle.move_up, "Up")
screen.onkey(player_paddle.move_down, "Down")
screen.listen()

screen.exitonclick()
