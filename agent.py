import gtts
import playsound
import googletrans
import speech_recognition


class TranslationAgent:
    def __init__(self, src, dest):
        self.validate_lang(src)
        self.validate_lang(dest)
        self.src = src
        self.dest = dest

    def speak_now(self):
        obj = speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone() as sr:
                print('Speak Now...')
                voice = obj.listen(sr)
                text = obj.recognize_google(voice, language=self.src)
        except Exception as e:
            print(f'Error... {e}')
            return
        return text

    def translate(self, text):
        obj = googletrans.Translator()
        translation = obj.translate(text=text, dest=self.dest)
        return translation.text

    def save_audio(self, text, path):
        audio = gtts.gTTS(text, lang=self.dest)
        audio.save(path)
        return True

    def play_audio(self, path):
        playsound.playsound(path)
        return

    def get_lang(self):
        return googletrans.LANGUAGES

    def validate_lang(self, lang):
        if lang not in self.get_lang():
            raise ValueError(f"Invalid language code: {lang}")
