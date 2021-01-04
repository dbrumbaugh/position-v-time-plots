import stddraw
import sys
from picture import Picture


def prepare_canvas():
    stddraw.setCanvasSize(1500, 500)
    stddraw.setXscale(0, 3)


def draw_plot():
    stddraw.line(2, 0, 2, 1)
    stddraw.line(2, 0, 3, 0)


def draw_picture(background, car, carx):
    stddraw.picture(background, 1, .5)
    stddraw.picture(car, carx, .44)


def main(argv):
    background = Picture('../img/background.png')
    car = Picture('../img/car.png')
    carx = .4
    t = 0
    dt = .001
    v0 = .001
    a0 = 0
    j0 = 0
    prepare_canvas()

    while True:
        draw_picture(background, car, carx)
        draw_plot()
        stddraw.setPenColor(stddraw.BLUE)
        stddraw.point(2 + t, carx - .4)
        stddraw.setPenColor(stddraw.BLACK)
        t += dt
        carx += v0
        v0 += a0
        a0 -= j0

        if carx > 1 and a0 > 0:
            a0 = -a0
        stddraw.show(0)


if __name__ == '__main__':
    main(sys.argv)
