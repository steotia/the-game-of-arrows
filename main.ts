namespace SpriteKind {
    export const progectile2 = SpriteKind.create()
    export const player2 = SpriteKind.create()
    export const progectile10 = SpriteKind.create()
    export const progectile45 = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.progectile2, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.changeScoreBy(1)
})
controller.player2.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function () {
    progectile45 = sprites.createProjectileFromSprite(img`
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
        `, space_plane2, 200, 0)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    progectile22 = sprites.createProjectileFromSprite(img`
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
        `, SPACE_PLANE, 200, 0)
})
sprites.onOverlap(SpriteKind.player2, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    info.player2.changeLifeBy(-1)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, SPACE_PLANE, 200, 0)
})
controller.player2.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    progectile10 = sprites.createProjectileFromSprite(img`
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
        `, space_plane2, 200, 0)
})
info.onLifeZero(function () {
    game.showLongText("player2 wins", DialogLayout.Bottom)
    game.over(false)
})
info.player2.onLifeZero(function () {
    game.showLongText("player1 wins", DialogLayout.Bottom)
    game.over(false)
})
sprites.onOverlap(SpriteKind.progectile45, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.player2.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.progectile10, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.player2.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    info.changeLifeBy(-1)
})
let bogey: Sprite = null
let progectile10: Sprite = null
let projectile: Sprite = null
let progectile22: Sprite = null
let progectile45: Sprite = null
let space_plane2: Sprite = null
let SPACE_PLANE: Sprite = null
SPACE_PLANE = sprites.create(img`
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
    `, SpriteKind.Player)
space_plane2 = sprites.create(img`
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
    `, SpriteKind.player2)
SPACE_PLANE.setFlag(SpriteFlag.StayInScreen, true)
space_plane2.setFlag(SpriteFlag.StayInScreen, true)
info.setLife(3)
info.player2.setLife(3)
controller.moveSprite(SPACE_PLANE)
controller.player2.moveSprite(space_plane2)
game.showLongText("you are being atacket by enchantet rocks.Press A AND B TOO SHOOT! ", DialogLayout.Left)
game.onUpdateInterval(500, function () {
    bogey = sprites.create(img`
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
        `, SpriteKind.Enemy)
    bogey.setVelocity(-100, 0)
    bogey.setPosition(180, Math.randomRange(0, 120))
    music.setVolume(20)
})
