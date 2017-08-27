import os
import glob

types = ["actions", "items", "levels", "achievments"]
root = os.path.dirname(__file__)

game_data = {}

for t in types:
    path = os.path.join(root, t)
    modules = [f for f in os.listdir(path) if f.endswith(".py")]
    data = {}
    for module in modules:
        identifier = module[:-3] # ???.py
        with open(os.path.join(path, module), 'r', encoding='utf-8') as f:
            if identifier != 'checkers':
                data[identifier] = eval(f.read())
    game_data[t] = data