from os import write
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
user_bet = screen.textinput(title="Welcome to Snake Game", prompt="Enter your name : ")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

if user_bet:
    game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with food
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for timmy in snake.timmy[1:]:
        if snake.head.distance(timmy) < 10:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()