from gtts import gtts

def play_audio(path_of_audio)
from playsound import playsound
playsound(path_of_audio)


def convet_to_audio(text):
    my_audio = gTTS(text)
    my_audio.save('hello.mp3')
    play_audio(hello.mp3)


    
    convet_to_audio('hey this is the test which i am try to demonstrade right now i hope it work ')