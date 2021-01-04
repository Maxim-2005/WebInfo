import eel

def start():
    eel.init("web")

    # Прием сообщения с сайта
    @eel.expose
    def call_in_js(msg):
        call_in_python(msg)

    # Отправка сообщения на сайт
    def call_in_python(msg):
        eel.call_in_python(msg)

    eel.start("index.html", mode='chrome', size=(640, 400))
    #edge, opera, electron, custom, none, false