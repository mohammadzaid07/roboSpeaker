import pyttsx3
engine = pyttsx3.init()

print("welcome to Robo speaker!!")
while True:
    x = input("Enter what do you want me to speak or press q to exit: ")
    if x.lower() == 'q':
        break
    engine.say(x)
    engine.runAndWait()
engine.say("")
engine.runAndWait()

