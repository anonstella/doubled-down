PLR = {
    "lives": 5,
    "bombs": 3,
    "stars": 0,
    "boss_beaten": 0,
    "score": 0,
    "firepower_addition": 0
}

VEL_MILESTONE = [
    0,
    4,
    12,
    24,
    60
]

BOSS = [
    # Boss A : Sekishin
    {
        "health": 1000,
        "pattern": 4,
        # "colour": (255, 255, 0),
        "decals": 'src/Rinnosuke Morichika.png'
    },
    {
        # "phase": 2, 
        "health": 1450,
        # "health": 145,
        "pattern": 1,
        # "colour": (255, 0, 255)
        "decals": 'src/Rinnosuke Morichika.png'
    },
    {
        # "phase": 3,
        "health": 2000,
        # "health": 200,
        "pattern": 2,
        "decals": 'src/Rinnosuke Morichika.png'
        # "colour": (0, 255, 255),
    },

    # Boss 2: Gakuno
    {
        "health": 2300,
        "pattern": 4,
        # "colour": (160, 255, 120)
        "decals": 'src/Fortune Teller.png'
    },
    {
        "health": 2540,
        "pattern": 3,
        # "colour": (111, 111, 255)
        "decals": 'src/Fortune Teller.png'
    },
    {
        "health": 3000,
        "pattern": 1,
        # "colour": (111, 111, 255)
        "decals": 'src/Fortune Teller.png'
    },


]

drops = [
    # by phase
    {
        "stars": 0,
        "points": 40,
        "firepower": 10,
        "bombs": 1,
        "lives": 0
    },
    {
        "stars": 1,
        "points": 60,
        "firepower": 15,
        "bombs": 0,
        "lives": 0
    },
    {
        "stars": 0,
        "points": 80,
        "firepower": 20,
        "bombs": 0,
        "lives": 1
    },
    {
        "stars": 1,
        "points": 100,
        "firepower": 25,
        "bombs": 0,
        "lives": 1
    },
    {
        "stars": 0,
        "points": 120,
        "firepower": 20,
        "bombs": 1,
        "lives": 0
    },
    {
        "stars": 1,
        "points": 140,
        "firepower": 32,
        "bombs": 0,
        "lives": 0
    },
]

# Patterns:
# 1 - Spread
# 2 - Spiral
# 3 - Radial
# 4 - Curved Spiral
# 5 - User-follow

print(BOSS[0])