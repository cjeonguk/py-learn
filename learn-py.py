import os

if not os.path.exists('demomove.txt'):
    os.replace('demofile.txt', 'demomove.txt')