enum ActionKind {
    Walking,
    Idle,
    Jumping
}
namespace SpriteKind {
    export const coin = SpriteKind.create()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (jobs.vy == 0) {
        jobs.vy = -100
    }
})
function Coin_Animation () {
    for (let value of tiles.getTilesByType(myTiles.tile8)) {
        coin2 = sprites.create(img`
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
            `, SpriteKind.coin)
        animation.runImageAnimation(
        coin2,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        100,
        true
        )
        tiles.placeOnTile(coin2, value)
        tiles.setTileAt(value, myTiles.transparency16)
    }
}
function anim_idle () {
    anim = animation.createAnimation(ActionKind.Idle, 300)
    anim.addAnimationFrame(img`
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
        `)
    anim.addAnimationFrame(img`
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
        `)
    animation.attachAnimation(jobs, anim)
    animation.setAction(jobs, ActionKind.Idle)
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (jobs.vy == 0) {
        jobs.vy = -100
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardLava0, function (sprite, location) {
    game.over(false, effects.starField)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    anim = animation.createAnimation(ActionKind.Walking, 300)
    anim.addAnimationFrame(img`
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
        `)
    anim.addAnimationFrame(img`
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
        `)
    animation.attachAnimation(jobs, anim)
    animation.setAction(jobs, ActionKind.Walking)
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    anim_idle()
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    anim_idle()
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    anim = animation.createAnimation(ActionKind.Walking, 300)
    anim.addAnimationFrame(img`
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
        `)
    anim.addAnimationFrame(img`
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
        `)
    animation.attachAnimation(jobs, anim)
    animation.setAction(jobs, ActionKind.Walking)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.coin, function (sprite, otherSprite) {
    music.pewPew.play()
    info.changeScoreBy(1)
    otherSprite.destroy()
})
scene.onOverlapTile(SpriteKind.Player, myTiles.tile10, function (sprite, location) {
    music.jumpUp.play()
    tiles.setTilemap(tilemap`level_7`)
    Coin_Animation()
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleRedCrystal, function (sprite, location) {
    music.jumpUp.play()
    game.showLongText("You did it!", DialogLayout.Bottom)
    tiles.setTilemap(tilemap`level_8`)
    tiles.placeOnRandomTile(jobs, myTiles.tile11)
    Coin_Animation()
})
let anim: animation.Animation = null
let coin2: Sprite = null
let jobs: Sprite = null
music.baDing.playUntilDone()
game.showLongText("Made by Ashar Hussein", DialogLayout.Bottom)
jobs = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(jobs, 100, 0)
scene.setBackgroundColor(9)
tiles.setTilemap(tilemap`level_6`)
jobs.ay = 200
jobs.setPosition(8, 37)
scene.cameraFollowSprite(jobs)
for (let value2 of tiles.getTilesByType(myTiles.tile8)) {
    coin2 = sprites.create(img`
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
        `, SpriteKind.coin)
    animation.runImageAnimation(
    coin2,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    100,
    true
    )
    tiles.placeOnTile(coin2, value2)
    tiles.setTileAt(value2, myTiles.transparency16)
}
anim_idle()
