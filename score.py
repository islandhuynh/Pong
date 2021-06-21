from turtle import Turtle
STYLE = ("Comic Sans", 20, "normal")

class Score(Turtle):
  def __init__(self, position):
    super().__init__()
    self.score_count = 0
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(position)
    self.update_score()

  def update_score(self):
    self.write(f"{self.score_count}", align="center", font=STYLE)

  def increase_score(self):
    self.score_count += 1
    self.clear()
    self.update_score()
