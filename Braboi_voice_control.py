############################
#   Braboi-voice-control   #
#    Pranav and Aadesh     #
#    using Google-API      #
############################

import os
from gtts import gTTS
import speech_recognition as sr
import string
from pymodbus.client.sync import ModbusTcpClient
"""def modcom():
    client = ModbusTcpClient('192.168.0.250')
    stats = client.connect()
    print("connected ?",stats)
    reg = [945,946,947,948,949]
    for i in reg:
        val = client.read_holding_registers(i).registers[0]
        print(i,val)"""
        
def reg():
    client = ModbusTcpClient('192.168.0.250')
    client.write_register(945,0)
    client.write_register(946,0)
    client.write_register(947,0)
    client.write_register(948,0)
    client.write_register(949,0)


r = sr.Recognizer()
mic = sr.Microphone()

how = "How are you Nancy?"
nancy = "Hello Nancy"
google = "Search for"
you = "Open youtube"



left  = "turn left"
right = "turn right"
up    = "up"
down  = "down"
back  = "home"


try:
    reg()
    print("Please wait calibrating the microphone, please be silent")
    with mic as source: r.adjust_for_ambient_noise(source,duration = 5)
    print("Set min energy threshold value to {} ".format(r.energy_threshold))
    print("=======================================================")
    while True:
        with mic as source:
            try:

                audio= r.listen(source, timeout = None) #LISTENING THE AUDIO
                print("Wait! I am analysing..")
                message = str(r.recognize_google(audio)) # RECOGNISING THE AUDIO USING GOOGLE-API



                if how in message:
                    tts = gTTS(text="I am good Pranav", lang='en')
                    tts.save("pcvoice.mp3")
                    os.system("mpg321 pcvoice.mp3")

                elif nancy in message:
                    tts = gTTS(text = "Yes Pranav")
                    tts.save("pcvoice.mp3")
                    os.system("mpg321 pcvoice.mp3")

                elif google in message:
                    words = message.split()
                    del words[0:2]
                    st = ' '.join(words)
                    tts = gTTS(text="Google results for "+str(st) , lang='en')
                    tts.save("pcvoice.mp3")
                    os.system("mpg321 pcvoice.mp3")
                    url = 'http://google.com/search?q='+st
                    webbrowser.open(url)

                elif you in message:
                    words = message.split()
                    del words[0:1]
                    st =' '.join(words)
                    tts = gTTS(text="Okay! Opening "+str(st),lang='en')
                    tts.save("pcvoice.mp3")
                    os.system("mpg321 pcvoice.mp3")
                    url = 'http://youtube.com'
                    webbrowser.open(url)


                elif left in message:
                    tts = gTTS(text = "Okay! Turning left now")
                    tts.save("pcvoice.mp3")
                    os.system("mpg321 pcvoice.mp3")
                    client = ModbusTcpClient('192.168.0.250')

                    client.write_register(946,0)
                    client.write_register(947,0)
                    client.write_register(948,0)
                    client.write_register(949,0)

                    client.write_register(945,1) #setting 1 for turnign left


                elif right in message:
                    tts = gTTS(text = "Okay! Turning right now")
                    tts.save("pcvoice.mp3")
                    os.system("mpg321 pcvoice.mp3")
                    client = ModbusTcpClient('192.168.0.250')
                    #modcom()
                    client.write_register(945,0)
                    client.write_register(947,0)
                    client.write_register(948,0)
                    client.write_register(949,0)

                    client.write_register(946,2)

                elif up in message:
                    tts = gTTS(text = "Okay! Moving up now")
                    tts.save("pcvoice.mp3")
                    os.system("mpg321 pcvoice.mp3")
                    client = ModbusTcpClient('192.168.0.250')
                    #modcom()
                    client.write_register(945,0)
                    client.write_register(946,0)
                    client.write_register(948,0)
                    client.write_register(949,0)

                    client.write_register(947,3)

                elif down in message:
                    tts = gTTS(text = "Okay! Moving down now")
                    tts.save("pcvoice.mp3")
                    os.system("mpg321 pcvoice.mp3")
                    client = ModbusTcpClient('192.168.0.250')
                    #modcom()
                    client.write_register(945,0)
                    client.write_register(946,0)
                    client.write_register(947,0)
                    client.write_register(949,0)

                    client.write_register(948,4)

                elif back in message:
                    tts = gTTS(text = "Okay! I will come back now")
                    tts.save("pcvoice.mp3")
                    os.system("mpg321 pcvoice.mp3")
                    client = ModbusTcpClient('192.168.0.250')
                    #modcom()
                    client.write_register(945,0)
                    client.write_register(946,0)
                    client.write_register(947,0)
                    client.write_register(948,0)

                    client.write_register(949,5)

            except sr.UnknownValueError:
                print("Didnt catch")

except KeyboardInterrupt:
    pass
