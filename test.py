from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# cube = Entity(model="cube", color=color.red, texture="white_cube", scale=2)
# player = Entity(model="cube", color=color.blue, scale=2)

# def update():
#     cube.rotation_x = cube.rotation_x + 0.25
#     cube.rotation_y = cube.rotation_y + 0.5
#     player.x += held_keys["d"] * 0.1
#     player.x -= held_keys["a"] * 0.1
#     player.y += held_keys["w"] * 0.1
#     player.y -= held_keys["s"] * 0.1
#     player.rotation_x += held_keys["r"] * 5
#     player.rotation_y += held_keys["r"] * 5

for z in range(10):
    for x in range(10):
        Entity(
            model="cube", 
            color=color.dark_gray, collider="box", 
            ignore=True,
            position = (x, 0, z), 
            parent=scene, 
            origin_y = 0.5,
            text = "white_cube"
        )

class TextureBox(Button):
    def __init__(self, position=(5,2,5)):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            origin_y=0.5,
            texture="texture.jpg",
            color=color.color(0,0,1)
        )

        self.texture_choice = 0
        self.textures = ["texture.jpg", "wood.jpg", "stones.jpg"]

        def input(self, key):
            if self.hovered:
                if key == 'left mouse down':
                    self.texture_choice += 1
                    self.texture_choice %= len(self.textures)
                    self.texture = self.textures[self.texture_choice]

TextureBox() 
player = FirstPersonController()
app.run()