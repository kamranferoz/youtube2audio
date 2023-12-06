![image](https://github.com/kamranferoz/youtube2audio/assets/34434270/3327beba-fe50-44f7-9cf0-23475da84d3b)


This program is a YouTube Audio Downloader. It allows users to input a YouTube video URL and downloads the audio from the video. The program uses the pytube library to fetch the YouTube video and extract the audio stream.

The audio is saved as an MP4 file with a unique filename based on the current date and time. The file is saved in the same directory as the script. If the directory doesn't exist, the program creates it.

The program checks if the provided URL is a valid YouTube video URL. If the URL is invalid or the video cannot be processed, the program displays an error message.

The program uses gradio to provide a simple and intuitive user interface. The interface consists of a text input field for the YouTube URL and a download link for the audio file.

The program is designed to be robust and user-friendly, providing clear error messages and handling exceptions gracefully.

The sample app can be found at [https://youtube2audio.streamlit.app/](https://huggingface.co/spaces/kamranferoz/youtube2audio)https://huggingface.co/spaces/kamranferoz/youtube2audio
