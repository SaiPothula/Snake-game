import turtle
SNAKE_SEG_SIZE = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    # The initial snake is created using 3 squares
    def create_snake(self):
        pos_x = 0
        for _ in range(3):
            self.add_segment(pos_x, 0)
            pos_x -= SNAKE_SEG_SIZE

    def add_segment(self, x_pos, y_pos):
        snake = turtle.Turtle(shape="square")
        snake.penup()
        self.snake_body.append(snake)
        snake.color("white")
        snake.setpos(x_pos, y_pos)

    def extend_snake(self):
        pos_x = self.snake_body[-1].xcor()
        pos_y = self.snake_body[-1].ycor()
        self.add_segment(pos_x, pos_y)

    def move(self):
        for index in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[index].penup()
            x = self.snake_body[index-1].xcor()
            y = self.snake_body[index-1].ycor()
            self.snake_body[index].goto(x, y)
        self.head.penup()
        self.head.forward(SNAKE_SEG_SIZE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        # for index in range(len(self.snake_body)-1, 0, -1):
        #     print(f"right() index seg {index}")
        #     self.snake_body[index].penup()
        #     x = self.snake_body[index-1].xcor()
        #     y = self.snake_body[index-1].ycor()
        #     self.snake_body[index].goto(x, y)
        # self.snake_body[0].penup()
        # self.snake_body[0].forward(20)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        # for index in range(0, len(self.snake_body)-1):
        #     self.snake_body[index].penup()
        #     x = self.snake_body[index+1].xcor()
        #     y = self.snake_body[index+1].ycor()
        #     self.snake_body[index].goto(x, y)
        # self.snake_body[len(self.snake_body)-1].penup()
        # self.snake_body[len(self.snake_body)-1].backward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # for index in range(len(self.snake_body) - 1, 0, -1):
        #     self.snake_body[index].penup()
        #     x = self.snake_body[index - 1].xcor()
        #     y = self.snake_body[index - 1].ycor()
        #     self.snake_body[index].goto(x, y)
        # self.snake_body[0].penup()
        # x = self.snake_body[0].xcor()
        # y = self.snake_body[0].ycor()
        # self.snake_body[0].goto(x, y+20)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        # for index in range(len(self.snake_body) - 1, 0, -1):
        #     self.snake_body[index].penup()
        #     x = self.snake_body[index - 1].xcor()
        #     y = self.snake_body[index - 1].ycor()
        #     self.snake_body[index].goto(x, y)
        # self.snake_body[0].penup()
        # x = self.snake_body[0].xcor()
        # y = self.snake_body[0].ycor()
        # self.snake_body[0].goto(x, y-20)
