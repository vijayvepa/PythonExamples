import bpy
from mathutils import *
D = bpy.data
C = bpy.context

cube = D.objects["Cube"]
cube.location += mathutils.Vector(1,1,1)