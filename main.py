from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
# segments = []
game_is_on = True

screen = Screen()
screen.tracer(0)
screen.setup(width=500, height=500)
screen.bgcolor("grey80")
screen.title("Snake Game")

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for segment in range(len(segments) - 1, 0, -1):
    #     new_x = segments[segment - 1].xcor()
    #     new_y = segments[segment - 1].ycor()
    #     segments[segment].goto(x=new_x, y=new_y)
    # segments[0].forward(20)
    snake.move()

    # Detect collition with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()

    # Detect collition with wall

    if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        # game_is_on = False
        # score.game_over()
        score.game_reset()
        snake.snake_reset()

    # Detect collition with tail

    for segment in snake.segments[1:]:
        # if segment != snake.head and snake.head.distance(segment) < 10:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # score.game_over()
            score.game_reset()
            snake.snake_reset()


screen.exitonclick()
