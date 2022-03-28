import sounddevice as sd
from scipy.io.wavfile import write
import Timer
def recordquestion(q,t):
    fs = 44100
    seconds = t

    myrecording = sd.rec(int(seconds*fs), samplerate=fs, channels= 2)
    print("Recording Started")
    #sd.wait()
    Timer.countdown(t)
    print("Finished Recording")
    write('{}.wav'.format(q),fs,myrecording)
