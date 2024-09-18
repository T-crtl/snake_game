from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score((0, 260))

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(snake.down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.tail[0].distance(food) < 15:
        food.refresh()
        snake.extends()
        score.add()
    
    if snake.tail[0].xcor() > 280 or snake.tail[0].xcor() < -280 or snake.tail[0].ycor() > 280 or snake.tail[0].ycor() < -280:
        score.score_reset()
        snake.snake_reset()
        food.refresh()
        #game_on = False
        #score.game_over()

    for segment in snake.tail[1:]:
        if snake.tail[0].distance(segment) < 10:
            score.score_reset()
            snake.snake_reset()
            food.refresh()
            #game_on = False
            #score.game_over()

screen.exitonclick()