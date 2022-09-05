import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import locale
import datetime


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
locale.setlocale(locale.LC_TIME, 'en')
wikipedia.set_lang("en")


def run_juanita(rec):
    if "search" in rec:
        if "news" in rec:
            webbrowser.open('https://www.lavanguardia.com/')
    
        if "Youtube" in rec:
            webbrowser.open('https://www.youtube.com/')

        if "virtual" in rec:
            webbrowser.open("https://aulasvirtuales.epn.edu.ec/")

        if "Google" in rec:
            if "" in rec:
                webbrowser.open("https://www.google.com")
            else:
                webbrowser.open("https://www.google.com")

        if "Amazon" in rec:
            rec.replace("Amazon", "")
            if "" in rec:
                webbrowser.open("https://www.amazon.es/s?k="+rec+"&__mk_es_ES=ÅMÅŽÕÑ&ref=nb_sb_noss_2")
            else:
                webbrowser.open("https://www.amazon.es/")

        if "Wikipedia" in rec:
            rec.replace("Wikipedia", "")
            if "" in rec:
                webbrowser.open("https://es.wikipedia.org/wiki/"+rec)
            else:
                pass

    if "help" in rec:
        if 'time' in rec:
            time = datetime.datetime.now().strftime('%I:%M %p')
            return "It's " + time

        if 'date' in rec:
            fecha = datetime.datetime.now().strftime('%A, %B %d, %Y')
            return 'The date is: ' + fecha

        if "Who is" or "Who was" or "who is" or "who was" in rec:
            person = rec.replace("Who is", "")
            person = rec.replace("who is", "")
            person = rec.replace("help", "")
            person = rec.replace("Who was", "")
            person = rec.replace("who was", "")
            info = wikipedia.summary(person, 1)
            return info