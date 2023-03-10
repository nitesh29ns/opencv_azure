from flask import Flask, render_template, request, Response
from camera import get_frame


application=Flask(__name__)

@application.route("/")
def index():
    return render_template("index.html")

@application.route("/video_feed")
def video_feed():
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    application.run()
