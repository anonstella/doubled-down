PLR = {
    "lives": 5,
    "bombs": 3,
    "stars": 0,
    "boss_beaten": 0
}

BOSS = [
    # Boss A : Sekishin
    {
        "health": 1000,
        "pattern": 4,
        "colour": (255, 255, 0)
    },
    {
        # "phase": 2, 
        "health": 1450,
        # "health": 145,
        "pattern": 1,
        "colour": (255, 0, 255)
    },
    {
        # "phase": 3,
        "health": 2000,
        # "health": 200,
        "pattern": 2,
        "colour": (0, 255, 255)
    },

    # Boss 2: Gakuno
    {
        "health": 2300,
        "pattern": 4,
        "colour": (160, 255, 120)
    },
    {
        "health": 2540,
        "pattern": 3,
        "colour": (111, 111, 255)
    },
    {
        "health": 3000,
        "pattern": 1,
        "colour": (111, 111, 255)
    },


]

drops = [
    # by phase
    {
        "stars": 0,
        "points": 40,
        "bombs": 1
    },
    {
        "stars": 1,
        "points": 60,
        "bombs": 0
    },
    {
        "stars": 0,
        "points": 80,
        "bombs": 0
    },
    {
        "stars": 1,
        "points": 100,
        "bombs": 0
    },
    {
        "stars": 0,
        "points": 120,
        "bombs": 1
    },
    {
        "stars": 1,
        "points": 140,
        "bombs": 0
    },
]

# Patterns:
# 1 - Spread
# 2 - Spiral
# 3 - Radial
# 4 - Curved Spiral
# 5 - User-follow

print(BOSS[0])