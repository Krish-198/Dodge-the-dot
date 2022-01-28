def on_button_pressed_a():
    Player.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    Player.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

Enemy: game.LedSprite = None
Player: game.LedSprite = None
Player = game.create_sprite(2, 4)

def on_forever():
    global Enemy
    basic.pause(randint(2000, 4000))
    Enemy = game.create_sprite(randint(0, 4), 0)
    for index in range(4):
        basic.pause(200)
        Enemy.change(LedSpriteProperty.Y, 1)
    if Player.is_touching(Enemy):
        game.game_over()
    else:
        game.add_score(1)
        Enemy.delete()
basic.forever(on_forever)
