import thing
import cropping_comment
import cropping_main
import audiomaker
import videomaker
import os

for i in range(1):
    thing.main3(i+2)
    videomaker.videomaking(str(i))

    dir = 'audio'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    dir = 'images'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    print("done")
