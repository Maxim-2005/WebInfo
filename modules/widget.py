import eel

def start():
    eel.init("web")
    eel.start("index.html", mode = 'chrome', size = (480, 320))
    #edge, opera, electron, custom, none, false