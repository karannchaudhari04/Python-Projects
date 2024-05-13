from flask import Flask, render_template, request, send_file
from pytube import YouTube
from werkzeug.utils import secure_filename
import os
import tempfile

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
        
        # Save video to a temporary location
        temp_dir = tempfile.mkdtemp()
        filepath = os.path.join(temp_dir, filename)
        video.download(output_path=temp_dir, filename=filename)

        return filepath  # Return the path to the downloaded video
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
