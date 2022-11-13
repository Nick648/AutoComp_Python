# import SpeechRecognition as sr
import pyttsx3
import sys


def check_en_voices():
    engine = pyttsx3.init()

    """ RATE"""
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    print(f"Rate: {rate}")  # printing current voice rate
    engine.setProperty('rate', 175)  # setting up new voice rate

    """VOLUME"""
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    print(f"Volume: {volume}")  # printing current volume level
    engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

    voices = engine.getProperty('voices')
    print(f'American voices:\nВсего {len(voices)}\n', '-' * 50)
    for voice in voices:
        words = f"Hi, I am assistant {voice.name}. How are you?\nHave a good day!"
        print(f'Name: {voice.name}\nID: {voice.id}\n{voice}\ntalking...\n', '-' * 50)
        engine.setProperty('voice', voice.id)
        engine.say(words)
        engine.runAndWait()


def check_rus_voices():
    engine = pyttsx3.init()

    """ RATE"""
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    print(f"Rate: {rate}")  # printing current voice rate
    engine.setProperty('rate', 175)  # setting up new voice rate

    """VOLUME"""
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    print(f"Volume: {volume}")  # printing current volume level
    engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

    # engine.setProperty('voice', 'ru')
    voices = engine.getProperty('voices')
    print(f'Russian voices:\nВсего {len(voices)}\n', '-' * 50)
    for voice in voices:
        words = f"Здравствуйте, я ассистент {voice.name}. Как Ваши дела?\nХорошего вам дня!"
        print(f'Name: {voice.name}\nID: {voice.id}\n{voice}\ntalking...\n', '-' * 50)
        engine.setProperty('voice', voice.id)
        engine.say(words)
        engine.runAndWait()


def voicePlay(string):  # try_2

    engine = pyttsx3.init()
    engine.say(string)
    try:
        engine.runAndWait()
    except Exception as e:
        print("Error:", e)
        pass
    engine.runAndWait()
    print("voicePlay")


def talk(words):
    engine = pyttsx3.init()
    # engine.setProperty('voice', 'ru')
    voices = engine.getProperty('voices')
    print('Voices:\n', '-' * 50)
    for voice in voices:
        print(f'Name: {voice.name}\nID: {voice.id}\n{voice}\ntalking...\n', '-' * 50)
        engine.setProperty('voice', voice.id)
        engine.say(words)
        engine.runAndWait()


if __name__ == '__main__':
    check_rus_voices()
    # check_en_voices()
    # talk('Добрый день')
    # talk('Hi, I am Gina!')
    # voicePlay('Добрый день')
    # voicePlay('Hi, I am Gina!')
