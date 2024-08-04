from vpython import canvas, box ,cylinder, vector, color, rate
# SETTING THE SCREEN AS CANVAS
scr = canvas(width =800, height=600, bg = color.white)

# DEFINING FUNCTIONS FOR DIFFERENT SHAPES
# 2 SHAPS ---> CUBOID
#        ---> CYLINDER
def draw_cuboid(pos,l,w,h,color):
    cub_var = box(pos= vector(*pos),l=l,w=w,h=h,color=color)
    return cub_var

def draw_cylinder(pos,r,h,color):
    cyl_var = cylinder(pos=vector(*pos),r=r,h=h,color=color)
    return cyl_var

# DIFFERENT 3D TRANSFORMATIONS
#             1) TRANSLATE
#             2) ROTATE
#             3) SCALE
def translate(obj,dx,dy,dz):
    obj.pos +=vector(dx,dy,dz)
def rotate(obj,angle,axis):
    obj.rotate(angle=angle, axis = vector(*axis))

def scaling(obj,sx,sy,sz):
    obj.size = vector(obj.size.x * sx, obj.size.y * sy, obj.size.z * sz)

#DRAWING THE SHAPES
cuboid = draw_cuboid((-2, 0, 0),  2,  2,  2, color.blue)
#                    vector pos   l   w   h  color
cylinder = draw_cylinder(( 2 , 2 , 0 ), 1, 10 ,color.red)
#                         vector pos    r   h  color

#TRANSLATING OBJECTS
translate(cuboid,4,0,0)
rotate(cuboid, angle = 45, axis=(0,1,0))
scaling(cuboid,3,3,3)

translate(cylinder,0,-2,0)
rotate(cylinder,angle = 30, axis=(1,0,0))
scaling(cylinder,1.5,1.5,1.5)

while True:
    rate(30)


