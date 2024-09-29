for n in range(1, len(xiao.segment), 1):
    if xiao.segment[0].position() == xiao.segment[n].position():
        game_is_on = False
        print("you lose")


self.segment_number = []
self.direction = 0
self.b = 0
self.c = 0
self.d = 0
self.e = 0
self.down_coordinate = [(1000, 1000)]
self.right_coordinate = [(1000, 1000)]
self.straight_coordinate = [(1000, 1000)]
self.left_coordinate = [(1000, 1000)]

self.segment_number.append([0, 0, 0, 0])

if a != 0:
    self.direction = self.segment[a].heading()
if self.segment[a].position() == self.straight_coordinate[self.segment_number[a][0]] and a != 0:
    self.segment[a].setheading(90)
    self.segment_number[a][0] += 1
    if self.direction != self.segment[a].heading() and self.b == 1:
        self.straight_coordinate += [(1000, 1000)]
        self.b = 2
elif self.segment[a].position() == self.left_coordinate[self.segment_number[a][1]] and a != 0:
    self.segment[a].setheading(180)
    self.segment_number[a][1] += 1
    if self.direction != self.segment[a].heading and self.c == 1:
        self.left_coordinate += [(1000, 1000)]
        self.c = 2
elif self.segment[a].position() == self.right_coordinate[self.segment_number[a][2]] and a != 0:
    self.segment[a].setheading(0)
    self.segment_number[a][2] += 1
    if self.direction != self.segment[a].heading and self.d == 1:
        self.right_coordinate += [(1000, 1000)]
        self.d = 2
elif self.segment[a].position() == self.down_coordinate[self.segment_number[a][3]] and a != 0:
    self.segment[a].setheading(-90)
    self.segment_number[a][3] += 1
    if self.direction != self.segment[a].heading and self.e == 1:
        self.down_coordinate += [(1000, 1000)]
        self.e = 2