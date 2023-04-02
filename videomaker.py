from moviepy.editor import *
import audioread
import os
from pathlib import Path

def videomaking(name):
    duration = []
    audio=[]


    for dir1 in os.listdir('audio'):
        a=audioread.audio_open(Path('audio/'+dir1))
        audio.append(dir1)
        duration.append(round(a.duration, 1))

    clips=[]

    time = 0.0

    for i in range(4):
        clip = VideoFileClip('default.mp4').subclip(time, duration[i])
        aclip = AudioFileClip(Path('audio/'+audio[i]))
        clip = clip.set_audio(aclip)
        

        title = ImageClip(Path("images/"+audio[i].replace(".mp3", "")+".png")).set_start(0).set_duration(duration[i]).set_pos(("center","center"))

        final = CompositeVideoClip([clip, title])
        
        clips.append(final)
        time+duration[i]
        


    combined = concatenate_videoclips(clips)
    combined.write_videofile(Path("videos/"+name+".mp4"))


