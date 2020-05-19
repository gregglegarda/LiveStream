from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    main = layout()
    return main

#==============================================   LAYOUT  =================================================#
def layout():
    layout = header() + body() + footer()
    return layout

def header():
    from scripts.layout import header
    header1 = header.header()
    header = header1.header_samples()
    return header  + "</br>"

def body():
    nc = container_main()
    from scripts.layout import body
    body1 = body.body()
    body = body1.body_samples()
    return nc + body + "</br>"

def footer():
    from scripts.layout import footer
    footer1 = footer.footer()
    footer = footer1.footer_samples()
    return footer + "</br>"

#==============================================   CONTAINERS  =================================================#
def container_main():
    main_container =  news_container() + radio_container() + music_container()
    return main_container

def news_container():
    from scripts.channels.news import abscbn
    from scripts.channels.news import gma
    v1 = abscbn.video()
    video1 = v1.video_samples()
    v2 = gma.video()
    video2 = v2.video_samples()
    video = video1 + " " + video2
    return video + "</br>"


def radio_container():
    from scripts.channels.radio import opmlovesongs
    from scripts.channels.radio import teleradyo

    v1 = opmlovesongs.video()
    video1 = v1.video_samples()

    v2 = teleradyo.video()
    video2 = v2.video_samples()

    ###concatenate as a string
    video = video1 +" " + video2
    return video + "</br>"

def music_container():
    from scripts.channels.music import monstercat
    v1 = monstercat.video()
    video1 = v1.video_samples()
    ###concatenate as a string
    video = video1
    return video + "</br>"




