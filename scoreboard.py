from turtle import Turtle
STYLE = ("Comic Sans", 20, "normal")

class Scoreboard:
  def __init__(self):
    self.player_one_score = 0
    self.player_two_score = 0
    self.p1_score_display = Turtle()
    self.p1_score_display.color("white")
    self.p1_score_display.hideturtle()
    self.p1_score_display.penup()
    self.p1_score_display.goto(30, 260)
    self.p2_score_display = Turtle()
    self.p2_score_display.color("white")
    self.p2_score_display.hideturtle()
    self.p2_score_display.penup()
    self.p2_score_display.goto(-30, 260)