"""
Бот, ретранслирующий голос в текст

1. **telebot**: Библиотека для работы с Telegram Bot API.
2. **os**: Модуль для взаимодействия с операционной системой.
3. **speech_recognition**: Библиотека для распознавания речи.
4. **pydub**: Библиотека для работы с аудиофайлами.
"""

import telebot
import os
import speech_recognition as sr
from pydub import AudioSegment

language = 'ru-RU'
TOKEN = 'your_token'
bot = telebot.TeleBot(TOKEN)
r = sr.Recognizer()


def recognise(filename):
    with sr.AudioFile(filename) as source:
        audio_text = r.record(source)
        try:
            text = r.recognize_google(audio_text, language=language)
            print('Перевод аудио в текст...')
            print(text)
            return text
        except sr.UnknownValueError:
            print('Извините, не смог разобрать звук.')
            return "Извините, не смог разобрать звук."
        except sr.RequestError as e:
            print(f"Google не отвечает; {e}")
            return "Что-то пошло не так..."


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        'Привет! Записывай мне голосовуху, а я её переведу в текст.'
    )


@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    file_id = message.voice.file_id
    file_name = f"voice/{file_id}.ogg"
    file_path = bot.get_file(file_id).file_path
    downloaded_file = bot.download_file(file_path)

    with open(file_name, 'wb') as new_file:
        if new_file.write(downloaded_file):
            print("Голос записан")

    # Конвертация из OGG в WAVE формат
    audio = AudioSegment.from_ogg(file_name)
    wav_file_name = f"ready/{file_id}.wav"
    audio.export(wav_file_name, format="wav")

    text = recognise(wav_file_name)
    bot.reply_to(message, text)

    # Удаление файлов
    os.remove(file_name)
    os.remove(wav_file_name)


bot.polling()
