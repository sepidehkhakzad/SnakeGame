from turtle import Turtle


class Snake:

    def __init__(self):
        self.game_len = 1
        self.turtle_len = 2 + self.game_len
        self.turtle_body = []
        self.x_pos = 0
        self.y_pos = 0
        self.create_snake()
        self.head = self.turtle_body[0]
        self.tail = self.turtle_body[-1]

    def create_snake(self):
        for len_t in range(0, self.turtle_len):
            t = Turtle("square")
            t.color("white")
            t.pu()
            t.setpos((self.x_pos + len_t * (-20), self.y_pos))
            self.turtle_body.append(t)

    def move(self):
        move_len = self.turtle_len - 1
        while move_len > 0:
            self.turtle_body[move_len].goto(self.turtle_body[move_len - 1].pos())
            move_len -= 1

        self.head.forward(20 * 1)

    def up(self):
        if self.check_180(90):
            pass
        else:
            self.head.setheading(90)

    def down(self):
        if self.check_180(270):
            pass
        else:
            self.head.setheading(270)

    def right(self):
        if self.check_180(0):
            pass
        else:
            self.head.setheading(0)

    def left(self):
        if self.check_180(180):
            pass
        else:
            self.head.setheading(180)

    def check_180(self, dir_m):
        if abs(self.head.heading() - dir_m) == 180:
            return True
        else:
            return False

    def increase_len(self, food_pos):
        self.game_len = self.game_len + 1
        self.turtle_len = 2 + self.game_len
        t = Turtle("square")
        t.color("white")
        t.pu()
        t.setpos((food_pos[0], food_pos[1]))
        self.turtle_body.append(t)
