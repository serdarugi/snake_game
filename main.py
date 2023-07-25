from turtle import Screen
from snake import Snake
from food import Food
from score_table import ScoreTable
import time

snake = Snake()
food = Food()
score = ScoreTable()
screen = Screen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

is_game = True
while is_game:
    screen.update()
    time.sleep(0.09)
    snake.move()
    score.create_score()

    # Detect Collision with food.
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.clear()
        score.score_screen += 1

    # Detech Collision with food.
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score.game_over()
        is_game = False
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            is_game = False
    # Detect collision with tail.
    # if head collides with any segment.
    # trigger game_over sequance.

screen.exitonclick()
