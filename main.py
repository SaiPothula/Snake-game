import turtle
import snake
import time
import food
import scoreboard

game_screen = turtle.Screen()
#game_screen.screensize(100, 100)
game_screen.setup(600, 600)
print(game_screen.screensize())
game_screen.bgcolor("black")
game_screen.tracer(0)

snake_action = snake.Snake()
food = food.Food()
score = scoreboard.Score()

game_screen.listen()
game_screen.onkey(snake_action.up, "Up")
game_screen.onkey(snake_action.down, "Down")
game_screen.onkey(snake_action.left, "Left")
game_screen.onkey(snake_action.right, "Right")

game_on = True
while game_on:
    snake_action.move()
    time.sleep(0.1)
    game_screen.update()

    # If food is ate - create food at other place, increase score, increase snake size
    if snake_action.head.distance(food) < 20:
        food.refresh()
        score.score_update()
        snake_action.extend_snake()

    # End game if snake hits walls
    head_x = snake_action.head.xcor()
    head_y = snake_action.head.ycor()
    if head_x >= 290 or head_x <= -290 or head_y >= 290 or head_y <= -290:
        score.game_over()
        game_on = False

    # End game if snake hits itself
    for seg in snake_action.snake_body[1:]:
        if snake_action.head.distance(seg) < 10:
            score.game_over()
            game_on = False

game_screen.exitonclick()
