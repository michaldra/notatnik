import speech_recognition
import random

def speech():
    mic = speech_recognition.Microphone()
    recog = speech_recognition.Recognizer()
    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        print("Nagrywanie rozpoczęte")
        audio = recog.listen(audio_file)
        print("Nagrywanie zakończone")
        return recog.recognize_google(audio, language="fr-FR")

points = 0
diffi = ""
levels = {
    "łatwy": ["agenda", "ami", "souris"],
    "średni": ["ordinateur", "algorithme", "développeur"],
    "trudny": ["réseau neuronal", "apprentissage automatique", "intelligence artificielle"]
}

def play_game(level):
    word = levels[level][random.randint(0,2)]
    print("Wypowiedz podane słowo:", word)
    detected = speech()
    print("Wykryte słowo:", detected)
    if detected == word:
        print("Dobrze!")
    else:
        print("Źle!")

while diffi != "łatwy" and diffi != "średni" and diffi != "trudny":
    diffi = input("Wybierz poziom trudności: łatwy, średni, trudny: ")

play_game(diffi)