from vosk import Model,KaldiRecognizer
import pyaudio

model = Model("#Here you have to enter path for your vosk package files")
recognizer = KaldiRecognizer(model,16000)

mic = pyaudio.PyAudio()
stream = mic.open(rate=16000,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    # if len(data) == 0:
    #     break
    if recognizer.AcceptWaveform(data):
        print(recognizer.Result())
              
#Modify this solution
#Wyłączanie aplikacji po jakimś czasie bezwładności np. 30 sekund
#zapis tekstu do notatnika
#czy jest możliwość rozpoznania mowy automatycznie (uzycie kilku języków naraz) -> czy wgranie dodatkowego języka np. polskiego w ta sama lokalizacje zadziała ?