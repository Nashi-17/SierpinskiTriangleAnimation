from manim import *
import numpy as np

config.frame_height = 16
config.frame_width = 9

config.pixel_height = 1280
config.pixel_width = 720

FRAME_WIDTH = config["frame_x_radius"] * 2
FRAME_HEIGHT = config["frame_y_radius"] * 2

class Test(MovingCameraScene):
    def construct(self):
        axes = NumberPlane(
            x_length= FRAME_WIDTH,
            x_range= [0, 1, 0.1],
            y_length= FRAME_HEIGHT,
            y_range= [0, 1, 0.1]
        ).set_color(BLACK)
        self.bring_to_back(axes)

        # Importing Points from file names as points.txt
        points = list()
        with open("points.txt", "r") as file:
            for i in file:
                temp = i.rstrip().split()
                point= list()
                for j in temp:
                    point.append(float(j))
                points.append(point)

        # Adding Dot mobjects on given points and also adding updater
        dots = list()
        for i in range(len(points)):
            dots.append(
                Dot(point= axes.c2p(points[i][0], points[i][1], 0)).scale(0.15)
            )
            dots[i].add_updater(lambda mobj, i=i : mobj.move_to(axes.c2p(points[i][0], points[i][1], 0)))
        self.add(VGroup(*dots))
        
        self.wait(3)
        self.play(
            self.camera.frame.animate.move_to([-5, -5, 0]),
            axes.animate.scale(8).shift(RIGHT * 0.5 + DOWN * 0.5),
            run_time= 20
        )
        self.wait(3)
