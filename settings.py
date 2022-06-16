# whole bunch of data used within other game files
# sound files, redudant data is stored here to keep the code a bit cleaner 
from random import randrange

# Game Info
gameName = "What lies ahead?"
screenWidth = 640
screenHeight = 736
FPS = 30
tileSize = 32

# Misc.
blackRGB = (0,0,0)
whiteRGB = (255,255,255)
tsBlack = (8,14,22)
redRGB = (255,0,0)
scaleFac = 2.7

# dirs.
iconPath = "data/img/icon.png"
SFX = {
    'sword': {
        'file': "data/sound/entity/sword.wav",
        '_vol': 0.05
    },
    'footsteps': {
        'file': "data/sound/entity/concrete2.wav",
        '_vol': 0.2
    },
    'enemy_death': {
        'file': "data/sound/entity/Enemy_Dies.wav",
        '_vol': 0.15
    },
    'enemy_damage': {
        'file': "data/sound/entity/Enemy_Damage.wav",
        '_vol': 0.15
    },
    'BG Music': {
        'file': "data/sound/BG.wav",
        '_vol': 0.15
    },
    'enemy_swing': {
        'file': "data/sound/entity/slash.wav",
        '_vol': 0.05
    },
    'ambient_sound': {
        'file': "data/sound/ambience/NDKG_CreepyAtmosphere_Looped.wav",
        '_vol': 0.1
    },
    'confirm_sound': {
        'file': 'data/sound/interface/confirm_style_1_001.wav',
        '_vol': 0.1
    },
    'cursor_sound': {
        'file': 'data/sound/interface/cursor_style_2.wav',
        '_vol': 0.1
    },
    'plr_death': {
        'file': 'data/sound/entity/Scream.wav',
        '_vol': 0.15
    }
}

# Player
loadingFrame = "data/graphics/anim_mc/up_idle/up_idle0000.png"
player_data = {
    'health': 200,
    'damage': 10,
    'speed' : 5,
    'canAttack': True
}

# Enemy
skeleton_data= {
    'health': 80,
    'damage': 20,
    'speed': randrange(2,4),
    'knockback': -4,
    'attack_radius': 35,
    'notice_radius': 50
}