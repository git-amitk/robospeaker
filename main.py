import os
if __name__ == '__main__':
    os.system(
        "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{welcome to Robospeaker 1.1 created by Amit}')\"")
    os.system(
        "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{enter what you want me to speak}')\"")

    while True:
       x = input("enter what you want me to speak")
       if x=='q':
           os.system("powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{bye bye}')\"")
           break
       command = f"powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}')\""
       os.system(command)


