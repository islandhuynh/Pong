from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
PLAYER_START_POSITON = [(-360, 30), (-360, 10), (-360, -10),(-360, -30)]
COMPUTER_START_POSITION = [(360, 30), (360, 10), (360, -10),(360, -30)]

class Paddle(Turtle):
  def __init__(self):
    self.paddle = []
    self.init_paddle()

  def init_paddle(self):
    for position in PLAYER_START_POSITON:
      block = Turtle("square")
      block.color("white")
      block.speed("fastest")
      block.penup()
      block.goto(position)
      self.paddle.append(block)
  
  def move_up(self):
    if self.paddle[0].ycor() < 290:
      for block_num in range(0, len(self.paddle)):
        self.paddle[block_num].goto(PLAYER_START_POSITON[block_num][0], self.paddle[block_num].ycor() + MOVE_DISTANCE)

  def move_down(self):
    if self.paddle[len(self.paddle) - 1].ycor() > -290:
      for block_num in range(0, len(self.paddle)):
        self.paddle[block_num].goto(PLAYER_START_POSITON[block_num][0], self.paddle[block_num].ycor() - MOVE_DISTANCE)
    