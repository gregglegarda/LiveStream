from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    main = layout()
    return main


def layout():
    layout = header() + "</br> " + body() + "</br> " + footer() + "</br> " + video()
    return layout

def header():
    from header import header
    header1 = header()
    header = header1.header_samples()
    return header


def body():
    from body import body
    body1 = body()
    body = body1.body_samples()
    return body



def footer():
    from footer import footer
    footer1 = footer()
    footer = footer1.footer_samples()
    return footer

def video():
    from video import video
    video1 = video()
    video = video1.video_samples()
    return video