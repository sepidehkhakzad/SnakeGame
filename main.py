import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = 1
while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect collision with food

    if snake.head.distance(food) < 15:
        food.change_pos()
        scoreboard.increase_score()
        snake.increase_len(food.position())

    # Detect collision with wall
    if snake.head.ycor() > 290 or snake.head.ycor() < -290 or snake.head.xcor() < -290 or snake.head.xcor() > 290:
        game_on = 0

    for body in range(1, snake.turtle_len):
        if snake.head.distance(snake.turtle_body[body]) < 10:
            game_on = 0
            scoreboard.game_over()

screen.bgcolor("black")
scoreboard.game_over()
screen.exitonclick()
