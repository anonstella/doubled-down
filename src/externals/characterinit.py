PLR = {
    "lives": 5,
    "bombs": 3,
    "stars": 0,
    "boss_beaten": 0
}

BOSS = [
    {
        # "phase": 1, 
        "health": 1000,
        # "health": 100,
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
    }

]

# Patterns:
# 1 - Spread
# 2 - Spiral
# 3 - Radial
# 4 - Curved Spiral
# 5 - User-follow

print(BOSS[0])