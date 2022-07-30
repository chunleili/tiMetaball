import taichi as ti
import taichi.math as tm
ti.init()

N= 128
pixels = ti.field(float, (N, N))
x = ti.Vector.field(2, float, (N, N))

center1 = tm.vec2(0.5, 0.5)
center2 = ti.Vector.field(2, float, ())
radius1 = 0.3
radius2 = 0.2

@ti.kernel
def set_sdf():
    for i,j in ti.ndrange(N,N):
        x[i,j] = tm.vec2(i/N, j/N)
        pixels[i,j] = 0
        if (x[i,j] - center1).norm() < radius1:
            pixels[i,j] = 1.0
        if (x[i,j] - center2[None]).norm() < radius2:
            pixels[i,j] = 1.0

def move():
    mouse_x, mouse_y = gui.get_cursor_pos()
    center2[None] = tm.vec2(mouse_x, mouse_y)

center2[None] = tm.vec2(0.2, 0.5)
gui = ti.GUI("metaBall", res=(6*N, 6*N))

while gui.running and not gui.get_event(gui.ESCAPE):
    move()
    set_sdf()
    gui.set_image(ti.tools.imresize(pixels, *gui.res))
    gui.show()