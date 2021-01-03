import eel

def start():
    eel.init("web")

    # Прием сообщения с сайта
    @eel.expose
    def call_in_js(msg):
        print(msg)

    eel.start("index.html", mode='chrome', size=(640, 400))
    #edge, opera, electron, custom, none, false