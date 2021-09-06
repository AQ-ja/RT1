from numpy import dot
from GL import Raytracer, V3, _color
from obj import Obj, Texture

from Figu import Sphere, Material

width = 980
height = 850


# ------------- MATERIALES ---------------------
nose = Material(diffuse = _color(0.890, 0.372, 0.050))
snow = Material(diffuse=_color(1, 1, 1))
dots = Material(diffuse=_color(0, 0, 0))


rtx = Raytracer(width,height)

# Snow
rtx.scene.append(Sphere(V3(0, -3, -10), 2, snow))
rtx.scene.append(Sphere(V3(0, 0, -15), 2.25, snow))
rtx.scene.append(Sphere(V3(0, 2, -10), 1, snow))

# Smile
rtx.scene.append(Sphere(V3(0.28, 0.80, -5), 0.05, dots))
rtx.scene.append(Sphere(V3(-0.28, 0.80, -5), 0.05, dots))
rtx.scene.append(Sphere(V3(0.12, 0.70, -5), 0.05, dots))
rtx.scene.append(Sphere(V3(-0.12, 0.70, -5), 0.05, dots))

# Nose
rtx.scene.append(Sphere(V3(0, 1, -5), 0.15, nose))

# Eyes
rtx.scene.append(Sphere(V3(0.18, 1.18, -5), 0.08, dots))
rtx.scene.append(Sphere(V3(-0.18, 1.19, -5), 0.08, dots))

# Dots
rtx.scene.append(Sphere(V3(0, -2.5, -8), 0.5, dots))
rtx.scene.append(Sphere(V3(0, -1, -8), 0.35, dots))
rtx.scene.append(Sphere(V3(0, 0.25, -8), 0.30, dots))

rtx.glRender()

rtx.glFinish('RT1.bmp')