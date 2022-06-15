# Game Info
gameName = "Test Game"
screenWidth = 640
screenHeight = 736
FPS = 30
tileSize = 32

# Misc.
blackRGB = (0,0,0)
tsBlack = (8,14,22)
redRGB = (255,0,0)
scaleFac = 2.7

# dirs.
iconPath = "data/img/testIcon.jpg"

# Player
loadingFrame = "data/graphics/anim_mc/up_idle/up_idle0000.png"
player_data = {
    'health': 100,
    'damage': 10,
    'speed' : 5,
    'canAttack': True
}

# Weapons
attack_data = {
    'sword': {
        'cooldown': 100,
        'damage' : 20,
        'graphic': None
    }
}

# Enemy
skeleton_data= {
    'health': 100,
    'damage': 10,
    'speed': 4.25,
    'knockback': 3,
    'attack_radius': 50,
    'notice_radius': 300
}