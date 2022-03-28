from gtts import gTTS
from gtts.tokenizer.pre_processors import abbreviations, end_of_line
from pygame import mixer
import time
import os
# Create the text
def play_questions(q):
    text = q
    tts = gTTS(text, slow=False, pre_processor_funcs = [abbreviations, end_of_line]) 
    # Save the audio in a mp3 file
    tts.save('hello.mp3')
    # Play the audio
    mixer.init()
    mixer.music.load("hello.mp3")
    mixer.music.play()
    # Wait for the audio to be played
    time.sleep(8)
    #closed mixer
    mixer.quit()
    os.remove("hello.mp3")
