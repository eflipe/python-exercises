class Ball(object):
    DEFAULT = 'regular'

    def __init__(self, ball_type=None):
        self.ball_type = ball_type if ball_type is not None else DEFAULT

class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

ball_1 = Ball()
print(ball_1.ball_type)
