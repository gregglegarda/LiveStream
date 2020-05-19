from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    main = layout()
    return main


def layout():
    layout = header() + news_container() + radio_container() + body()  + footer()
    return layout

def header():
    from scripts.header import header
    header1 = header()
    header = header1.header_samples()
    return header  + "</br> "


def body():
    from scripts.body import body
    body1 = body()
    body = body1.body_samples()
    return body + "</br> "


def news_container():
    from scripts.channels.news import abscbn
    video1 = abscbn.video()
    video = video1.video_samples()
    return video + "</br> " + "</br> "



def radio_container():
    from scripts.channels.radio import opmlovesongs
    from scripts.channels.radio import teleradyo

    v1 = opmlovesongs.video()
    video1 = v1.video_samples()

    v2 = teleradyo.video()
    video2 = v2.video_samples()


    ###concatenate as a string
    video = video1 +" " + video2
    return video + "</br> "

def footer():
    from scripts.footer import footer
    footer1 = footer()
    footer = footer1.footer_samples()
    return footer + "</br> "

