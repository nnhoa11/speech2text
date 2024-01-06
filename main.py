import speech_recognition as sr

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        text = r.recognize_google(audio, language="vi-VN")
        print(text)


if __name__ == '__main__':
    while True:
        get_audio()

