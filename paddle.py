from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle:
  def __init__(self, starting_position):
    self.starting_positon = starting_position
    self.blocks = []
    self.init_paddle()

  def init_paddle(self):
    for position in self.starting_positon:
      block = Turtle("square")
      block.color("white")
      block.speed("fastest")
      block.penup()
      block.goto(position)
      self.blocks.append(block)
  
  def move_up(self):
    if self.blocks[0].ycor() < 290:
      for block_num in range(0, len(self.blocks)):
        self.blocks[block_num].sety(self.blocks[block_num].ycor() + MOVE_DISTANCE)

  def move_down(self):
    if self.blocks[len(self.blocks) - 1].ycor() > -290:
      for block_num in range(0, len(self.blocks)):
        self.blocks[block_num].sety( self.blocks[block_num].ycor() - MOVE_DISTANCE)
    
