from flask import Flask, render_template, request, make_response
from pytube import YouTube
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()

        filename = secure_filename(f"{yt.title}.mp4")

        def generate_video_stream():
            video.stream_to_buffer()
            with video.streams.get_highest_resolution().stream_to_buffer() as stream:
                yield from stream

        response = make_response(generate_video_stream())
        response.headers.set('Content-Type', 'video/mp4')
        response.headers.set('Content-Disposition', f'attachment; filename="{filename}"')
        return response

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)