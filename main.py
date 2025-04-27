import speech_recognition as sr
import pyttsx3
import webbrowser
import sys
import datetime
import pyjokes

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def get_time():
    now = datetime.datetime.now()
    return now.strftime("It's %I:%M %p.")

def get_date():
    now = datetime.datetime.now()
    return now.strftime("Today is %A, %B %d, %Y.")

def tell_joke():
    joke = pyjokes.get_joke()
    return joke

def processCommand(command):
    print(f"Processing command: {command}")
    speak(f"You said: {command}")

    command = command.lower()

    if "open google" in command:
        speak("Zooming you to Google! Don't get lost in memes.")
        webbrowser.open("https://www.google.com")
    elif "open instagram" in command:
        speak("Let’s scroll through some influencer drama, shall we?")
        webbrowser.open("https://www.instagram.com")
    elif "open whatsapp" in command:
        speak("Time to ignore some messages on WhatsApp.")
        webbrowser.open("https://www.whatsapp.com")
    elif "open linkedin" in command:
        speak("Opening LinkedIn. Pretend to be professional!")
        webbrowser.open("https://www.linkedin.com")
    elif "open youtube" in command:
        speak("Launching YouTube. Try not to fall into a 3-hour cat video loop.")
        webbrowser.open("https://www.youtube.com")
    elif "open news" in command:
        speak("Let’s see what’s going wrong in the world today.")
        webbrowser.open("https://www.timesofindia.com")
    elif "play song" in command:
        speak("Cue the music! May I suggest Rick Astley?")
        webbrowser.open("https://www.spotify.com")
    elif "what is your name" in command:
        speak("I’m Jarvis. Not to brag, but I’m 30% sass, 70% genius.")
    elif "what time is it" in command or "tell me the time" in command:
        speak(get_time())
    elif "what is the date" in command or "tell me the date" in command:
        speak(get_date())
    elif "tell me a joke" in command or "joke" in command:
        joke = tell_joke()
        speak(joke)
    elif "stop" in command:
        speak("Alright, shutting down. But I’ll be watching...")
        sys.exit()
    else:
        speak("Sorry, I don’t speak nonsense—yet.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            print("Recognizing wake word...")
            wake_word = recognizer.recognize_google(audio)
            print(f"You said: {wake_word}")

            if "jarvis" in wake_word.lower():
                speak("Yes boss, I’m all ears... virtually.")
                
                with sr.Microphone() as source:
                    print("Listening for your command...")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)

                command = recognizer.recognize_google(audio)
                print(f"Command: {command}")
                processCommand(command)

        except sr.WaitTimeoutError:
            print("No speech detected. Waiting again...")
            continue

        except sr.UnknownValueError:
            print("Could not understand audio.")

        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak("Houston, we have a connection problem.")

        except Exception as e:
            print(f"Unexpected error: {e}")
            speak("Whoa, something broke. Probably not my fault.")
