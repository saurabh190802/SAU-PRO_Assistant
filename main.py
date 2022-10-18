import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os 

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


talk('Hello, This is sau..... only yours assistant. What can i do for you?')

def take_command():
    try:
            with sr.Microphone() as source:
                print("Listening...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if "sau" in command:
                    talk("ya boy tell further")
                    command = command.replace('sau', '')
                    return command
                else:
                    talk("I cannot continue until you say sau")
                    take_command()
    except:
            pass


def run_jarvis():
    command = take_command()
    if not command:
            take_command()
    else:
            print(command)
            if "play" in command:
                song = command.replace("play", "")
                talk("playing" + song)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                talk(time)
            elif 'joke' in command:
                joke = pyjokes.get_joke()
                print(joke)
                talk(joke)
            elif 'downloads' in command:
                path = "C:/Users\Mayur\Downloads"
                path = os.path.realpath(path)
                os.startfile(path)
            elif "whatsapp" in command:
                msg = command.replace("whatsapp", "")
                pywhatkit.sendwhatmsg_instantly("+91xxxxxxxxxx", msg)
                print("Successfully Sent!")
                talk("successfully sent")
            elif 'who is' or 'what is' or 'where is' or 'when is' or 'information' or 'which is' or "how is" in command:
                result = pywhatkit.info(command, 3, True)
                talk(result)
                print(result)
            else:
                talk('Sorry sir can you repeat again')


while True:
        run_jarvis()
