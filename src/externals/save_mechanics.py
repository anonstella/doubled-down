import os, json, pygame

def load_existing_save(f):
    with open(os.path.join(f), 'r+') as file:
        settings = json.load(file)
    return settings

def w_save(data):
    with open(os.path.join(os.getcwd(), 'settings.json'),  'w') as file:
        json.dump(data, file)

def load_save():
    try:
        save = load_existing_save('settings.json')
    except:
        save = save_create()
        w_save(save)
    return save

def save_create():
    new_save = {
    "music_vol": 0.4,
    "sfx_vol": 0.6,
    "FPS": 120
    }
    return new_save