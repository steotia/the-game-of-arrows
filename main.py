@namespace
class SpriteKind:
    progectile2 = SpriteKind.create()
    player2 = SpriteKind.create()
    progectile10 = SpriteKind.create()
    progectile45 = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.progectile2, SpriteKind.enemy, on_on_overlap)

def on_player2_button_b_pressed():
    global progectile452
    progectile452 = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . 6 6 6 6 6 6 6 6 . . 9 9 9 9 . 
                    . . . . . . . 9 9 9 9 9 . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        space_plane2,
        200,
        0)
controller.player2.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player2_button_b_pressed)

def on_b_pressed():
    global progectile22
    progectile22 = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . 2 . 
                    . . 2 2 2 2 2 2 2 2 2 2 2 2 4 2 
                    . . . . . . . . . . . . . . 2 . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SPACE_PLANE,
        200,
        0)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    info.player2.change_life_by(-1)
sprites.on_overlap(SpriteKind.player2, SpriteKind.enemy, on_on_overlap2)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . 8 . 
                    . . 8 8 8 8 8 8 8 8 8 8 8 8 5 8 
                    . . . . . . . . . . . . . . 8 . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SPACE_PLANE,
        200,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_player2_button_a_pressed():
    global progectile102
    progectile102 = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . 9 . 
                    . . 9 9 9 9 9 9 9 9 9 9 9 9 6 9 
                    . . . . . . . . . . . . . . 9 . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        space_plane2,
        200,
        0)
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_life_zero():
    game.show_long_text("player2 wins", DialogLayout.BOTTOM)
    game.over(False)
info.on_life_zero(on_life_zero)

def on_player2_life_zero():
    game.show_long_text("player1 wins", DialogLayout.BOTTOM)
    game.over(False)
info.player2.on_life_zero(on_player2_life_zero)

def on_on_overlap3(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.player2.change_score_by(1)
sprites.on_overlap(SpriteKind.progectile45, SpriteKind.enemy, on_on_overlap3)

def on_on_overlap4(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.player2.change_score_by(1)
sprites.on_overlap(SpriteKind.progectile10, SpriteKind.enemy, on_on_overlap4)

def on_on_overlap5(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap5)

def on_on_overlap6(sprite, otherSprite):
    otherSprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap6)

bogey: Sprite = None
progectile102: Sprite = None
projectile: Sprite = None
progectile22: Sprite = None
progectile452: Sprite = None
space_plane2: Sprite = None
SPACE_PLANE: Sprite = None
SPACE_PLANE = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . b b b . b . . . . . 
            . . . . . . b . b . b b . . . . 
            . . . . . . b b b . b . b . . . 
            . . . . . . . b b b b 2 b . . . 
            . . . . . . . b b b b 8 b . . . 
            . . . . . . b b b . b b . . . . 
            . . . . . . b . b . b . . . . . 
            . . . . . . b . b . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
space_plane2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . e . . . . . . . . 
            . . . e e e e . e . . . . . . . 
            . . . e . e e . . e . . . . . . 
            . . . e e e e 9 9 e . . . . . . 
            . . . . e e e e 6 e . . . . . . 
            . . . . e e e e . e . . . . . . 
            . . . . e . e e e . . . . . . . 
            . . . . e . . e . . . . . . . . 
            . . . . e . . . . . . . . . . . 
            . . . e e e . . . . . . . . . . 
            . . . e e e . . . . . . . . . . 
            . . . e e e . . . . . . . . . . 
            . . . e e e . . . . . . . . . . 
            . . . e . e . . . . . . . . . .
    """),
    SpriteKind.player2)
SPACE_PLANE.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
space_plane2.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.set_life(3)
info.player2.set_life(3)
controller.move_sprite(SPACE_PLANE)
controller.player2.move_sprite(space_plane2)
game.show_long_text("you are being atacket by enchantet rocks.Press A AND B TOO SHOOT! ",
    DialogLayout.LEFT)

def on_update_interval():
    global bogey
    bogey = sprites.create(img("""
            . . . . . . c c c c c c . . . . 
                    . . . . c c b b d d d d c . . . 
                    . . . c c b b d d d d d d c . . 
                    . . c b b d b d d d d d d b c . 
                    . c b b b d b b d d d d d b c . 
                    . c b b b d d b d d d d b b c . 
                    c b c b b b d d b b b b b c c . 
                    c b c c b b b b d d d b c c c . 
                    c b b c c c c c c c c c c c c . 
                    c c b b b b b b c c b d d d b c 
                    c c c c c c c c c d d d d d d c 
                    c c c c c c c b c b d d d d d b 
                    c b b b c c c b c c b d d d c b 
                    c c b b b c c b b c c c c b b c 
                    c c c c c c c c b b b b b b c c 
                    c c c c c c c c c c c c c c c c
        """),
        SpriteKind.enemy)
    bogey.set_velocity(-100, 0)
    bogey.set_position(180, Math.random_range(0, 120))
    music.set_volume(20)
game.on_update_interval(500, on_update_interval)
