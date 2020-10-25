class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2
@namespace
class SpriteKind:
    coin = SpriteKind.create()

def on_up_pressed():
    if jobs.vy == 0:
        jobs.vy = -100
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def Coin_Animation():
    global coin2
    for value in tiles.get_tiles_by_type(myTiles.tile8):
        coin2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . f f f f f f f . . . . . . . . 
                            f 5 5 5 5 5 5 5 f . . . . . . . 
                            f 5 5 5 5 5 5 5 f . . . . . . . 
                            f 5 5 5 5 5 5 5 f . . . . . . . 
                            f 5 5 5 5 5 5 5 f . . . . . . . 
                            f 5 5 5 5 5 5 5 f . . . . . . . 
                            f 5 5 5 5 5 5 5 f . . . . . . . 
                            f 5 5 5 5 5 5 5 f . . . . . . . 
                            . f f f f f f f . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.coin)
        animation.run_image_animation(coin2,
            [img("""
                    f 5 5 5 5 5 5 5 f . . . . . . . 
                                5 5 5 5 5 f . . . . . . . . . . 
                                5 5 5 5 5 f . . . . . . . . . . 
                                5 5 5 5 5 f . . . . . . . . . . 
                                5 5 5 5 5 f . . . . . . . . . . 
                                5 5 5 5 5 f . . . . . . . . . . 
                                5 5 5 5 5 f . . . . . . . . . . 
                                5 5 5 5 5 f . . . . . . . . . . 
                                f 5 5 5 f . . . . . . . . . . . 
                                . f f f f . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    f 5 5 5 5 5 5 5 f . . . . . . . 
                                5 5 5 5 5 f . . . . . . . . . . 
                                5 5 5 5 5 f . . . . . . . . . . 
                                5 5 5 5 5 f . . . . . . . . . . 
                                5 5 5 5 5 f . . . . . . . . . . 
                                5 5 5 5 5 f . . . . . . . . . . 
                                5 5 5 5 5 f . . . . . . . . . . 
                                5 5 5 5 5 f . . . . . . . . . . 
                                f 5 5 5 f . . . . . . . . . . . 
                                . f f f f . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    f 5 5 5 5 5 . 5 f . . . . . . . 
                                5 5 5 5 f . . . . . . . . . . . 
                                5 5 5 5 f . . . . . . . . . . . 
                                5 5 5 5 f . . . . . . . . . . . 
                                5 5 5 5 f . . . . . . . . . . . 
                                5 5 5 5 f . . . . . . . . . . . 
                                5 5 5 5 f . . . . . . . . . . . 
                                5 5 5 5 f . . . . . . . . . . . 
                                f 5 5 f . . . . . . . . . . . . 
                                . f f f f . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    f 5 5 5 5 5 5 5 f . . . . . . . 
                                5 5 5 5 5 5 5 5 f . . . . . . . 
                                5 5 5 5 5 5 5 5 f . . . . . . . 
                                5 5 5 5 5 5 5 5 f . . . . . . . 
                                5 5 5 5 5 5 5 5 f . . . . . . . 
                                5 5 5 5 5 5 5 5 f . . . . . . . 
                                5 5 5 5 5 5 5 5 f . . . . . . . 
                                5 5 5 5 5 5 5 5 f . . . . . . . 
                                f 5 5 5 5 5 5 f . . . . . . . . 
                                . f f f f f f f . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    f 5 5 5 5 5 5 5 f . . . . . . . 
                                5 5 5 5 5 5 5 5 f . . . . . . . 
                                5 5 5 5 5 5 5 5 f . . . . . . . 
                                5 5 5 5 5 5 5 5 f . . . . . . . 
                                5 5 5 5 5 5 5 5 f . . . . . . . 
                                5 5 5 5 5 5 5 5 f . . . . . . . 
                                5 5 5 5 5 5 5 5 f . . . . . . . 
                                5 5 5 5 5 5 5 5 f . . . . . . . 
                                f 5 5 5 5 5 5 f . . . . . . . . 
                                . f f f f f f f . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    f 5 5 5 5 5 f . . . . . . . . . 
                                5 5 5 5 5 5 5 f . . . . . . . . 
                                5 5 5 5 5 5 5 f . . . . . . . . 
                                5 5 5 5 5 5 5 f . . . . . . . . 
                                5 5 5 5 5 5 5 f . . . . . . . . 
                                5 5 5 5 5 5 5 f . . . . . . . . 
                                5 5 5 5 5 5 5 f . . . . . . . . 
                                5 5 5 5 5 5 5 f . . . . . . . . 
                                f 5 5 5 5 5 f . . . . . . . . . 
                                . f f f f f . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    f 5 5 5 5 f . . . . . . . . . . 
                                5 5 5 5 5 5 f . . . . . . . . . 
                                5 5 5 5 5 5 f . . . . . . . . . 
                                5 5 5 5 5 5 f . . . . . . . . . 
                                5 5 5 5 5 5 f . . . . . . . . . 
                                5 5 5 5 5 5 f . . . . . . . . . 
                                5 5 5 5 5 5 f . . . . . . . . . 
                                5 5 5 5 5 5 f . . . . . . . . . 
                                f 5 5 5 5 f . . . . . . . . . . 
                                . f f f f . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    f 5 5 5 5 5 f . . . . . . . . . 
                                5 5 5 5 5 5 5 f . . . . . . . . 
                                5 5 5 5 5 5 5 f . . . . . . . . 
                                5 5 5 5 5 5 5 f . . . . . . . . 
                                5 5 5 5 5 5 5 f . . . . . . . . 
                                5 5 5 5 5 5 5 f . . . . . . . . 
                                5 5 5 5 5 5 5 f . . . . . . . . 
                                5 5 5 5 5 5 5 f . . . . . . . . 
                                f 5 5 5 5 5 f . . . . . . . . . 
                                . f f f f f . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """)],
            100,
            True)
        tiles.place_on_tile(coin2, value)
        tiles.set_tile_at(value, myTiles.transparency16)
def anim_idle():
    global anim
    anim = animation.create_animation(ActionKind.Idle, 300)
    anim.add_animation_frame(img("""
        . . . f f f f f f f . . . . . . 
                . f f f 2 2 2 2 2 f . . . . . . 
                f f 2 2 2 2 2 2 2 f . . . . . . 
                f 2 2 2 f f f 2 2 f f f . . . . 
                f 2 2 f f f 2 2 2 2 f f f . . . 
                f f f f f e e e e e e f f f . . 
                . . f f e 2 2 2 2 2 2 e e f . . 
                . . f e 2 f f f f f f 2 e f . . 
                . . f f f f e e e e f f f f . . 
                . f f e f b f 4 4 f b f e f f . 
                . f e e 4 1 f d d f 1 4 e e f . 
                . . f e e d d d d d d e e f . . 
                . . . f e e 4 4 4 4 e e f . . . 
                . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
    """))
    anim.add_animation_frame(img("""
        . . . . . . f f f f f f . . . . 
                . . . . . . f 2 2 2 2 f f f . . 
                . . . . . . f 2 2 2 2 2 2 f f . 
                . . . . f f f 2 2 f f f 2 2 f f 
                . . . f f f 2 2 2 2 f f f 2 2 f 
                . . f f f e e e e e e f f f f f 
                . . f f e 2 2 2 2 2 2 e e f . . 
                . . f e 2 f f f f f f 2 e f . . 
                . . f f f f e e e e f f f f . . 
                . f f e f b f 4 4 f b f e f f . 
                . f e e 4 1 f d d f 1 4 e e f . 
                . . f e e d d d d d d e e f . . 
                . . . f e e 4 4 4 4 e e f . . . 
                . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
    """))
    animation.attach_animation(jobs, anim)
    animation.set_action(jobs, ActionKind.Idle)

def on_a_pressed():
    if jobs.vy == 0:
        jobs.vy = -100
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite, location):
    game.over(False, effects.star_field)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava0,
    on_overlap_tile)

def on_left_pressed():
    global anim
    anim = animation.create_animation(ActionKind.Walking, 300)
    anim.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . f f f f f f . . . . . 
                . . . . f 2 f e e e e f f . . . 
                . . . f 2 2 2 f e e e e f f . . 
                . . . f e e e e f f e e e f . . 
                . . f e 2 2 2 2 e e f f f f . . 
                . . f 2 e f f f f 2 2 2 e f . . 
                . . f f f e e e f f f f f f f . 
                . . f e e 4 4 f b e 4 4 e f f . 
                . . f f e d d f 1 4 d 4 e e f . 
                . f d d f d d d d 4 e e e f . . 
                . f b b f e e e 4 e e f . . . . 
                . f b b e d d 4 2 2 2 f . . . . 
                . . f b e d d e 4 4 4 f f . . . 
                . . . f f e e f f f f f f . . . 
                . . . . f f f . . . f f . . . .
    """))
    anim.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . f f f f f f . . . . . 
                . . . . f 2 f e e e e f f . . . 
                . . . f 2 2 2 f e e e e f f . . 
                . . . f e e e e f f e e e f . . 
                . . f e 2 2 2 2 e e f f f f . . 
                . . f 2 e f f f f 2 2 2 e f . . 
                . . f f f e e e f f f f f f f . 
                . . f e e 4 4 f b e 4 4 e f f . 
                . . . f e d d f 1 4 d 4 e e f . 
                . . . . f d d d e e e e e f . . 
                . . . . f e 4 e d d 4 f . . . . 
                . . . . f 2 2 e d d e f . . . . 
                . . . f f 5 5 f e e f f f . . . 
                . . . f f f f f f f f f f . . . 
                . . . . f f f . . . f f . . . .
    """))
    animation.attach_animation(jobs, anim)
    animation.set_action(jobs, ActionKind.Walking)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    anim_idle()
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    anim_idle()
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_right_pressed():
    global anim
    anim = animation.create_animation(ActionKind.Walking, 300)
    anim.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . f f f f f f . . . . . 
                . . . f f e e e e f 2 f . . . . 
                . . f f e e e e f 2 2 2 f . . . 
                . . f e e e f f e e e e f . . . 
                . . f f f f e e 2 2 2 2 e f . . 
                . . f e 2 2 2 f f f f e 2 f . . 
                . f f f f f f f e e e f f f . . 
                . f f e 4 4 e b f 4 4 e e f . . 
                . f e e 4 d 4 1 f d d e f . . . 
                . . f e e e e e d d d f . . . . 
                . . . . f 4 d d e 4 e f . . . . 
                . . . . f e d d e 2 2 f . . . . 
                . . . f f f e e f 5 5 f f . . . 
                . . . f f f f f f f f f f . . . 
                . . . . f f . . . f f f . . . .
    """))
    anim.add_animation_frame(img("""
        . . . . . f f f f f f . . . . . 
                . . . f f e e e e f 2 f . . . . 
                . . f f e e e e f 2 2 2 f . . . 
                . . f e e e f f e e e e f . . . 
                . . f f f f e e 2 2 2 2 e f . . 
                . . f e 2 2 2 f f f f e 2 f . . 
                . f f f f f f f e e e f f f . . 
                . f f e 4 4 e b f 4 4 e e f . . 
                . f e e 4 d 4 1 f d d e f f . . 
                . . f e e e 4 d d d d f d d f . 
                . . . f f e e 4 e e e f b b f . 
                . . . . f 2 2 2 4 d d e b b f . 
                . . . . e 2 2 2 e d d e b f . . 
                . . . . f 4 4 4 f e e f f . . . 
                . . . . . f f f f f f . . . . . 
                . . . . . . f f f . . . . . . .
    """))
    animation.attach_animation(jobs, anim)
    animation.set_action(jobs, ActionKind.Walking)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite, otherSprite):
    music.pew_pew.play()
    info.change_score_by(1)
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.coin, on_on_overlap)

def on_overlap_tile2(sprite, location):
    music.jump_up.play()
    tiles.set_tilemap(tilemap("""
        level_7
    """))
    Coin_Animation()
scene.on_overlap_tile(SpriteKind.player, myTiles.tile10, on_overlap_tile2)

def on_overlap_tile3(sprite, location):
    music.jump_up.play()
    game.show_long_text("You did it!", DialogLayout.BOTTOM)
    tiles.set_tilemap(tilemap("""
        level_8
    """))
    tiles.place_on_random_tile(jobs, myTiles.tile11)
    Coin_Animation()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_red_crystal,
    on_overlap_tile3)

anim: animation.Animation = None
coin2: Sprite = None
jobs: Sprite = None
music.ba_ding.play_until_done()
game.show_long_text("Made by Ashar Hussein", DialogLayout.BOTTOM)
jobs = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f f f f d d d d d e e f . . 
            . f d d d d f 4 4 4 e e f . . . 
            . f b b b b f 2 2 2 2 f 4 e . . 
            . f b b b b f 2 2 2 2 f d 4 . . 
            . . f c c f 4 5 5 4 4 f 4 4 . . 
            . . . f f f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(jobs, 100, 0)
scene.set_background_color(9)
tiles.set_tilemap(tilemap("""
    level_6
"""))
jobs.ay = 200
jobs.set_position(8, 37)
scene.camera_follow_sprite(jobs)
for value2 in tiles.get_tiles_by_type(myTiles.tile8):
    coin2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . f f f f f f f . . . . . . . . 
                    f 5 5 5 5 5 5 5 f . . . . . . . 
                    f 5 5 5 5 5 5 5 f . . . . . . . 
                    f 5 5 5 5 5 5 5 f . . . . . . . 
                    f 5 5 5 5 5 5 5 f . . . . . . . 
                    f 5 5 5 5 5 5 5 f . . . . . . . 
                    f 5 5 5 5 5 5 5 f . . . . . . . 
                    f 5 5 5 5 5 5 5 f . . . . . . . 
                    . f f f f f f f . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.coin)
    animation.run_image_animation(coin2,
        [img("""
                f 5 5 5 5 5 5 5 f . . . . . . . 
                        5 5 5 5 5 f . . . . . . . . . . 
                        5 5 5 5 5 f . . . . . . . . . . 
                        5 5 5 5 5 f . . . . . . . . . . 
                        5 5 5 5 5 f . . . . . . . . . . 
                        5 5 5 5 5 f . . . . . . . . . . 
                        5 5 5 5 5 f . . . . . . . . . . 
                        5 5 5 5 5 f . . . . . . . . . . 
                        f 5 5 5 f . . . . . . . . . . . 
                        . f f f f . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                f 5 5 5 5 5 5 5 f . . . . . . . 
                        5 5 5 5 5 f . . . . . . . . . . 
                        5 5 5 5 5 f . . . . . . . . . . 
                        5 5 5 5 5 f . . . . . . . . . . 
                        5 5 5 5 5 f . . . . . . . . . . 
                        5 5 5 5 5 f . . . . . . . . . . 
                        5 5 5 5 5 f . . . . . . . . . . 
                        5 5 5 5 5 f . . . . . . . . . . 
                        f 5 5 5 f . . . . . . . . . . . 
                        . f f f f . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                f 5 5 5 5 5 . 5 f . . . . . . . 
                        5 5 5 5 f . . . . . . . . . . . 
                        5 5 5 5 f . . . . . . . . . . . 
                        5 5 5 5 f . . . . . . . . . . . 
                        5 5 5 5 f . . . . . . . . . . . 
                        5 5 5 5 f . . . . . . . . . . . 
                        5 5 5 5 f . . . . . . . . . . . 
                        5 5 5 5 f . . . . . . . . . . . 
                        f 5 5 f . . . . . . . . . . . . 
                        . f f f f . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                f 5 5 5 5 5 5 5 f . . . . . . . 
                        5 5 5 5 5 5 5 5 f . . . . . . . 
                        5 5 5 5 5 5 5 5 f . . . . . . . 
                        5 5 5 5 5 5 5 5 f . . . . . . . 
                        5 5 5 5 5 5 5 5 f . . . . . . . 
                        5 5 5 5 5 5 5 5 f . . . . . . . 
                        5 5 5 5 5 5 5 5 f . . . . . . . 
                        5 5 5 5 5 5 5 5 f . . . . . . . 
                        f 5 5 5 5 5 5 f . . . . . . . . 
                        . f f f f f f f . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                f 5 5 5 5 5 5 5 f . . . . . . . 
                        5 5 5 5 5 5 5 5 f . . . . . . . 
                        5 5 5 5 5 5 5 5 f . . . . . . . 
                        5 5 5 5 5 5 5 5 f . . . . . . . 
                        5 5 5 5 5 5 5 5 f . . . . . . . 
                        5 5 5 5 5 5 5 5 f . . . . . . . 
                        5 5 5 5 5 5 5 5 f . . . . . . . 
                        5 5 5 5 5 5 5 5 f . . . . . . . 
                        f 5 5 5 5 5 5 f . . . . . . . . 
                        . f f f f f f f . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                f 5 5 5 5 5 f . . . . . . . . . 
                        5 5 5 5 5 5 5 f . . . . . . . . 
                        5 5 5 5 5 5 5 f . . . . . . . . 
                        5 5 5 5 5 5 5 f . . . . . . . . 
                        5 5 5 5 5 5 5 f . . . . . . . . 
                        5 5 5 5 5 5 5 f . . . . . . . . 
                        5 5 5 5 5 5 5 f . . . . . . . . 
                        5 5 5 5 5 5 5 f . . . . . . . . 
                        f 5 5 5 5 5 f . . . . . . . . . 
                        . f f f f f . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                f 5 5 5 5 f . . . . . . . . . . 
                        5 5 5 5 5 5 f . . . . . . . . . 
                        5 5 5 5 5 5 f . . . . . . . . . 
                        5 5 5 5 5 5 f . . . . . . . . . 
                        5 5 5 5 5 5 f . . . . . . . . . 
                        5 5 5 5 5 5 f . . . . . . . . . 
                        5 5 5 5 5 5 f . . . . . . . . . 
                        5 5 5 5 5 5 f . . . . . . . . . 
                        f 5 5 5 5 f . . . . . . . . . . 
                        . f f f f . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                f 5 5 5 5 5 f . . . . . . . . . 
                        5 5 5 5 5 5 5 f . . . . . . . . 
                        5 5 5 5 5 5 5 f . . . . . . . . 
                        5 5 5 5 5 5 5 f . . . . . . . . 
                        5 5 5 5 5 5 5 f . . . . . . . . 
                        5 5 5 5 5 5 5 f . . . . . . . . 
                        5 5 5 5 5 5 5 f . . . . . . . . 
                        5 5 5 5 5 5 5 f . . . . . . . . 
                        f 5 5 5 5 5 f . . . . . . . . . 
                        . f f f f f . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        100,
        True)
    tiles.place_on_tile(coin2, value2)
    tiles.set_tile_at(value2, myTiles.transparency16)
anim_idle()