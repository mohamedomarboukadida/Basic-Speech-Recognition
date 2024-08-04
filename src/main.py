import speech_recognition as sr

recognizer = sr.Recognizer()

def listen_and_recognize():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("I am listening ...")
        audio = recognizer.listen(source)
    try:
        print("Processing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized: {command}")
        return command
    except sr.UnknownValueError:
        print("I could not understand the audio.")
    except sr.RequestError:
        print("API request error; check your internet connection.")
    return 

command = listen_and_recognize()

if "start" in command:
    print("Initiating start sequence...")
elif "stop" in command:
    print("Initiating stop sequence...")
elif "pause" in command:
    print("Pausing operation...")
elif "resume" in command:
    print("Resuming operation...")    
elif "shut down" in command:
    print("Shutting down system...")
elif "turn off" in command:
    print("Turning off...")
elif command:
    print("Command not recognized.")
