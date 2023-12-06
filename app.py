import os
from pytube import YouTube
import time 
from urllib.parse import urlparse, parse_qs
import gradio as gr

def get_youtube_object(url):
    try:
        yt = YouTube(url)
        return yt
    except Exception as e:
        print('Failed to process video. Please check your URL or try again later.')
        return None 

def download_audio_from_youtube_url(url: str) -> gr.outputs.File:

    parsed_url = urlparse(url)
    video_id = parse_qs(parsed_url.query).get("v")
   
    if video_id:
        url = f"https://www.youtube.com/watch?v={video_id[0]}"
          
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = f"Audio_{timestr}.mp4"

        yt = get_youtube_object(url)    
        if yt is None:
            return 'Failed to process video. Please check your URL or try again later.'
        
        # Create a persistent downloads directory if it doesn't exist
        downloads_dir = "./"
        os.makedirs(downloads_dir, exist_ok=True)

        stream = yt.streams.get_audio_only("mp4")  
        stream.download(output_path=downloads_dir, filename=filename)

        # returns a File object that can be downloaded by the user
        return os.path.join(downloads_dir, filename) 
   
    else:
        return 'Invalid YouTube URL! Please check your URL.'

iface = gr.Interface(fn=download_audio_from_youtube_url,
                     inputs=["text"],  # no longer need the download path input
                     outputs=gr.outputs.File())

iface.launch(share=True)
