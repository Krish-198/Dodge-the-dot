input.onButtonPressed(Button.A, function () {
    Player.move(-1)
})
input.onButtonPressed(Button.B, function () {
    Player.move(1)
})
let Enemy: game.LedSprite = null
let Player: game.LedSprite = null
Player = game.createSprite(2, 4)
basic.forever(function () {
    basic.pause(randint(2000, 4000))
    Enemy = game.createSprite(randint(0, 4), 0)
    for (let index = 0; index < 4; index++) {
        basic.pause(200)
        Enemy.change(LedSpriteProperty.Y, 1)
    }
    if (Player.isTouching(Enemy)) {
        game.gameOver()
    } else {
        game.addScore(1)
        Enemy.delete()
    }
})
