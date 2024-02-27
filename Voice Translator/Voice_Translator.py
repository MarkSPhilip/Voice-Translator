import googletrans
import speech_recognition
import gtts
import playsound

recognizer = speech_recognition.Recognizer()

try:
    with speech_recognition.Microphone() as source:
        print("Speak Now (in Hindi)")
        voice = recognizer.listen(source)
        print("Recognition in progress...")
        text = recognizer.recognize_google(voice, language="hi-IN")
        print("Recognized Text (Hindi):", text)

    translator = googletrans.Translator()
    translation = translator.translate(text, dest="en")
    print("Translated Text (English):", translation.text)

    converted_audio = gtts.gTTS(translation.text, lang="en")
    converted_audio.save("hello.mp3")
    playsound.playsound("hello.mp3")

except speech_recognition.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except speech_recognition.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")