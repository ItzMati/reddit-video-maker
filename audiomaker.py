import thing
import pyttsx3


def audio(text1, name):
    main = text1
    
    engine = pyttsx3.init()

    voices = engine.getProperty("voices")

    engine.setProperty("voice", voices[1].id)

    engine.save_to_file(main, Path("audio/"+name+".mp3"))

    engine.runAndWait()
