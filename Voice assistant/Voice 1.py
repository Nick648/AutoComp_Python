import pyttsx3
import speech_recognition as sr
import pyaudio  # for speech_recognition -> microphone
import sys

MICROPHONE_INDEX = 0


def get_property_settings() -> None:
    text = 'какой-нибудь текст'
    tts = pyttsx3.init()
    rate = tts.getProperty('rate')  # Скорость произношения
    # tts.setProperty('rate', rate - 40)

    volume = tts.getProperty('volume')  # Громкость голоса
    # tts.setProperty('volume', volume + 0.9)

    voices = tts.getProperty('voices')
    count_voices = len(voices)

    # Задать голос по умолчанию
    # tts.setProperty('voice', 'ru')

    # Попробовать установить предпочтительный голос
    # for voice in voices:
    #     if voice.name == 'Anna':
    #         tts.setProperty('voice', voice.id)
    #
    # tts.say(text)
    # tts.runAndWait()

    print(f"{rate=}; {volume=}; {voices=}; {count_voices=}\n")


def get_microphone_index() -> None:
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    print()


def check_record_speech() -> None:
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        r = sr.Recognizer()
        try:
            with sr.Microphone(device_index=index) as source:
                print(f'\tНастраиваюсь. mic = {index}')
                r.adjust_for_ambient_noise(source, duration=0.5)  # настройка посторонних шумов
                print('Слушаю...')
                audio = r.listen(source)
            print('Услышала.')

            try:
                query = r.recognize_google(audio, language='ru-RU')
                text = query.lower()
                print(f'Вы сказали: {text}')
            except Exception as ex:
                print(f'{type(ex).__name__}: Not recognize!')

        except Exception as ex:
            print(f"{type(ex).__name__}: device_index={index} does not work!")


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


def voice_play(string):  # try_2

    engine = pyttsx3.init()
    try:
        engine.say(string)
        engine.runAndWait()
    except Exception as e:
        print("Error:", e)
        pass
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
    get_property_settings()
    get_microphone_index()
    check_record_speech()
    # check_rus_voices()
    # check_en_voices()
    # talk('Добрый день')
    # talk('Hi, I am Gina!')
    # voice_play('Добрый день')
    # voice_play('Hi, I am Gina!')
