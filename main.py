from turtle import Screen
from paddle import Paddle
from pong import Pong
from score import Score
import time

PLAYER_ONE_START_POSITON = [(-360, 30), (-360, 10), (-360, -10),(-360, -30)]
PLAYER_TWO_START_POSITION = [(360, 30), (360, 10), (360, -10),(360, -30)]
PLAYER_ONE_SCORE_POSITION = (30, 260)
PLAYER_TWO_SCORE_POSITION = (-30, 260)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong by Island Huynh")

player_one_paddle = Paddle(PLAYER_ONE_START_POSITON)
player_two_paddle = Paddle(PLAYER_TWO_START_POSITION)
player_one_score = Score(PLAYER_ONE_SCORE_POSITION)
player_two_score = Score(PLAYER_TWO_SCORE_POSITION)
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
  time.sleep(0.02)
  pong.move()
  
  # Detect collision with wall
  if pong.ycor() > 280 or pong.ycor() < -280:
    pong.bounce_y()

  if pong.xcor() > 400:
    player_one_score.increase_score()
    pong.reset()
  
  if pong.xcor() < -400:
    player_two_score.increase_score()
    pong.reset()

  detect_paddle_collision(player_one_paddle)
  detect_paddle_collision(player_two_paddle)

screen.exitonclick()
