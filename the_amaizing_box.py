import random
import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


window_width = 800
window_height = 600

point_size = 5
base_speed = 100.0           
transition_period = 1.0      



points = []  #  {"x","y","dx","dy","r","g","b"}

speed_mod = 1.0             
blink = False                
frozen = False               

last_frame_time = None
blink_time = 0.0



def mouse_cor_convert(x, y):
    w_x = float(x)
    w_y = float(window_height - y)
    w_x = max(0.0, min(window_width, w_x))
    w_y = max(0.0, min(window_height, w_y))
    return w_x, w_y


def random_color():
    red = random.uniform(0.3, 1.0)
    green = random.uniform(0.3, 1.0)
    blue = random.uniform(0.3, 1.0)
    return red, green, blue


def random_direction():
    dx = random.choice([-1, 1])
    dy = random.choice([-1, 1])
    return dx, dy



def update(dt):
    global blink_time

    if frozen:
        return

    blink_time += dt
    if not points:
        return

    step = base_speed * speed_mod * dt
    for p in points:
        n_x = p["x"] + p["dx"] * step
        n_y = p["y"] + p["dy"] * step

        if n_x <= 0.0 or n_x >= window_width:
            p["dx"] *= -1
            n_x = max(0.0, min(window_width, n_x))
        if n_y <= 0.0 or n_y >= window_height:
            p["dy"] *= -1
            n_y = max(0.0, min(window_height, n_y))

        p["x"] = n_x
        p["y"] = n_y


def draw_points():
    visible = True
    if blink:
        temp = blink_time % transition_period
        visible = temp < (transition_period / 2)

    glPointSize(point_size)
    glBegin(GL_POINTS)
    for p in points:
        if visible:
            glColor3f(p["r"], p["g"], p["b"])
        else:
            glColor3f(0.0, 0.0, 0.0)
        glVertex2f(p["x"], p["y"])
    glEnd()


def setup_projection():
    glViewport(0, 0, window_width, window_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, window_width, 0, window_height, -1, 1)
    glMatrixMode(GL_MODELVIEW)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    setup_projection()
    draw_points()
    glutSwapBuffers()



def mouse(button, state, x, y):
    global blink

    if frozen:
        return

    if state != GLUT_DOWN:
        return

    if button == GLUT_RIGHT_BUTTON:
        wx, wy = mouse_cor_convert(x, y)
        dx, dy = random_direction()
        r, g, b = random_color()
        points.append({
            "x": wx,
            "y": wy,
            "dx": dx,
            "dy": dy,
            "r": r,
            "g": g,
            "b": b
        })
    elif button == GLUT_LEFT_BUTTON:
        blink = not blink


def special_keys(key, x, y):
    global speed_mod

    if frozen:
        return

    if key == GLUT_KEY_UP:
        speed_mod = min(10.0, speed_mod * 1.25)
    elif key == GLUT_KEY_DOWN:
        speed_mod = max(0.05, speed_mod / 1.25)


def keyboard(key, x, y):
    global frozen, last_frame_time
    if key == b' ':
        frozen = not frozen
        last_frame_time = None


def reshape(width, height):
    global window_width, window_height
    window_width = max(200, width)
    window_height = max(200, height)
    glutPostRedisplay()



def timer(value):
    global last_frame_time

    now = time.perf_counter()
    if last_frame_time is None:
        dt = 0.0
    else:
        dt = now - last_frame_time
    last_frame_time = now

    dt = min(dt, 0.05)  
    update(dt)
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)  




    



def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(window_width, window_height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"The Amazing Box")

    glClearColor(0.0, 0.0, 0.0, 1.0)

    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutSpecialFunc(special_keys)
    glutKeyboardFunc(keyboard)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, timer, 0)

    glutMainLoop()


if __name__ == "__main__":
    main()