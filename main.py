from turtle import Screen
from paddle import Paddle
from pong import Pong
from scoreboard import Scoreboard
import time

PLAYER_ONE_START_POSITON = [(-360, 30), (-360, 10), (-360, -10),(-360, -30)]
PLAYER_TWO_START_POSITION = [(360, 30), (360, 10), (360, -10),(360, -30)]

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong by Island Huynh")

player_one_paddle = Paddle(PLAYER_ONE_START_POSITON)
player_two_paddle = Paddle(PLAYER_TWO_START_POSITION)
score_keeper = Scoreboard()
pong = Pong()

def detect_paddle_collision(paddle):
  for block in paddle.blocks:
    if block.distance(pong) < 20:
      pong.bounce_x()

screen.listen()
screen.onkey(player_one_paddle.move_up, "w")
screen.onkey(player_one_paddle.move_down, "s")
screen.onkey(player_two_paddle.move_up, "Up")
screen.onkey(player_two_paddle.move_down, "Down")

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)
  pong.move()
  
  # Detect collision with wall
  if pong.ycor() > 280 or pong.ycor() < -280:
    pong.bounce_y()

  detect_paddle_collision(player_one_paddle)
  detect_paddle_collision(player_two_paddle)

screen.exitonclick()
