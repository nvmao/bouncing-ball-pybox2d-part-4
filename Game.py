from pygame import Vector2

from Ball import Ball
from Ring import Ring
from Sounds import sounds
from utils import utils


class Game:
    def __init__(self):
        self.center = Vector2(utils.width/2,utils.height/2)
        self.balls = [
            Ball(Vector2(utils.width / 2, utils.height / 2), 1, (255, 255, 255))
        ]
        self.rings = [
            Ring(Vector2(utils.width / 2, utils.height / 2), 25, -1, 100),
        ]

    def update(self):
        utils.world.Step(1.0 / 60.0, 6, 2)
        if utils.contactListener:
            for bodyA,bodyB in utils.contactListener.collisions:
                sounds.play()
                break
            utils.contactListener.collisions = []


        for ball in self.balls:
            if ball.getPos().distance_to(self.center) > 500:
                ball.destroyFlag = True
                self.balls.append(Ball(Vector2(utils.width / 2 - 50, utils.height / 2), 1, (255, 23, 255)))
                self.balls.append(Ball(Vector2(utils.width / 2 + 50, utils.height / 2), 1, (255, 255, 23)))

        for ball in self.balls:
            if ball.destroyFlag:
                utils.world.DestroyBody(ball.circle_body)
                self.balls.remove(ball)


    def draw(self):
        for ring in self.rings:
            ring.draw()
        for ball in self.balls:
            ball.draw()