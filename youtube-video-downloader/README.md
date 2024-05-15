# YouTube Video Downloader

This is a simple web application built with Python and Flask that allows users to download videos from YouTube. The application provides a user-friendly interface where users can enter the YouTube video link and download the video in the highest available resolution.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.8 & above
- Flask
- pytube

You can install the required Python packages using the following command:  pip install flask pytube

## Running the Application

1. Clone or download the project repository.
2. Navigate to the project directory in your terminal or command prompt.
3. Run the following command to start the Flask development server:      flask run

4. Once the server is running, open a web browser and navigate to `http://localhost:5000`.

## Usage

1. Enter the YouTube video link in the provided input field.
2. Click the "Download" button.
3. Your browser will prompt you to save the file. Choose the desired location and click "Save".
4. The video will be downloaded with the highest available resolution.

## Project Structure

- `app.py`: The main Flask application file that handles the routes and video download logic.
- `templates/index.html`: The HTML template for the user interface.
- `static/css/styles.css`: The CSS file for styling the user interface.
- `static/js/script.js`: The JavaScript file for handling user interactions and making the download request.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).