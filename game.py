from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.color = color.blue

def input(key):
    if key == 'escape':
        quit()

floor = Entity(
    model='cube',
    scale=(100, 1, 1000),  
    color=color.gray,
    collider='box'
)
cube = Entity(
    model="cube",
    color=color.dark_gray,
    scale = 2, 
    position=Vec3(10,2,3),
    collider='box'
)
circle = Entity(
    model="sphere",
    color=color.red,
    scale=5,
    position=Vec3(4,3,10),
    collider='sphere'
)

player = FirstPersonController()
player.cursor.visible = False

def update():
    if held_keys["r"]:
        player.rotation_x += time.dt * 50
    if held_keys["q"]:
        player.rotation_x -= time.dt * 50
    if held_keys["space"]:
        player.y += time.dt * 10
    

app.run()
