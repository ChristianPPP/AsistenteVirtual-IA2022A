#In[1]
#Librerías
from transformers import *
import speech_recognition as sr
import pyttsx3
import fun1, fun2
from flask import Flask, request, render_template, redirect

#In[2]
#Variables
app = Flask(__name__) #Definición de aplicación de flask
UPLOAD_FOLDER = 'files' #Variable para el sistema de archivos de flask

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #Confiuración de la carpeta files 

engine=pyttsx3.init() #Inicialización del módulo para el speech
voices=engine.getProperty('voices') #obtener la variable voices, servirá para escoger voces
engine.setProperty('voice', voices[1].id) #Selección de voz
engine.setProperty('rate', 150) #Selección de velocidad 
engine.setProperty('volume', 4.0) #Selección de volumen

history = [] #Variable para almacenar las entradas del usuario
responses = [] #Varibale para almacenar las respuestas del asistente

#In[2]
#Clase principal
#En ella se definen la mayoría de métodos que serán manejados por la inteligencia ariticial 
class Chatbot():
    def __init__(self, nombre):
        self.nombre = nombre
        print("Iniciando Bot ", nombre)

#In[4]
#Respuestas
    #Función para conversar con el asistente
    @staticmethod    
    def predict(text, history=[]):
        # Se define el tokenizer el cual nos permitirá codificar y decodificar los inputs 
        # del usuario, esto es necesario para que los datos sean legibles por el modelo 
        tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
        # Se define el modelo, en este caso haciendo uso de transformers se utiliza un modelo
        # "conversational" en este caso el modelo de facebook preentrenado  
        model = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-400M-distill")
        # Se codifica el input del usuario usando el tokenizador
        new_user_input_ids = tokenizer.encode(text, return_tensors='pt')
        # Se almacena la respuesta del modelo en su historial
        history = model.generate(new_user_input_ids, max_new_tokens=1000, pad_token_id=tokenizer.eos_token_id)
        # Se decofica la respuesta generada 
        response = tokenizer.decode(history[0], skip_special_tokens=True)
        return response
    
    #Función para la traducción
    @staticmethod
    def predict1(text):
        # Se emplea el pipeline de transformers para no emplear un tokenizador automático
        # en este caso para la traducción se emplea el modelo de Helsinki 
        translator = pipeline("translation_en_to_es", model="Helsinki-NLP/opus-mt-en-es", tokenizer="Helsinki-NLP/opus-mt-en-es")
        resul = translator(text)[0]["translation_text"]
        return resul
    
    @staticmethod
    def predict2(text):
        # Se emplea el pipeline de transformers para no emplear un tokenizador automático
        # en este caso para la traducción se emplea el modelo de Helsinki 
        text_gen_pipeline = pipeline('text-generation', model='gpt2')
        output = text_gen_pipeline(text, max_length=60)[0]["generated_text"]
        return output

#In[]
#Flask 
#Esta función permite que el asistente hable
def talks(text):
    try:
        # Se emplea el motor definido en las variables 
        # para generar una respuesta con el método say 
        # y con el método runAndWait se inicia el loop
        engine.endLoop()
        engine.say(text) 
        engine.runAndWait()
    except:
        engine.say(text) 
        engine.runAndWait()

# Se define una función para el manejo de la vista index con flask
@app.route("/", methods=["POST", "GET"])
def index():
    ai = Chatbot(nombre="angel")
    response=""
    
    listener=sr.Recognizer()
    if request.method == "POST":
        # En esta sección se manejan las respuestas enviadas desde
        # el navegador y a su vez se maneja el almacenamiento del
        # archivo de audio generado desde el frontend
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        file.save("file_name5.wav")
        with sr.AudioFile("file_name5.wav") as source:
            voice = listener.record(source)
        response=listener.recognize_google(voice, language="en")
        print(response.__str__().replace('Angel', ''))
        response_out_angel=response.__str__().replace('Angel', '')
        history.append(response.__str__())
        print(history)
        
        # En este bloque se maneja la lógica del asistente para responder en base 
        # a las diferentes opciones definidas, siendo aquí donde se llaman a los
        # métodos en base a lo que el usuario requiera 
        if "angel" in response.__str__() or "Angel" in response.__str__():
            print("Welcome to angel")
            if "hello" in history[-1]:
                talks("Hello! i'm angel IA, what can I do for you?")
            else:
                if "talk" in response_out_angel.__str__():
                    talks("Of course, we can talk.")
                else:
                    if "reproduce" in history[-1]:
                        print("Reproduce")
                        fun1.run_angel(response_out_angel.__str__())
                        talks(response_out_angel.__str__())
                    if "open" in history[-1]:
                        print("Open")
                        res_out_open = response_out_angel.replace("open", "")
                        fun1.run_angel(response_out_angel.__str__())
                        talks("Opening "+res_out_open.__str__())
                    if "search" in history[-1] or "help" in history[-1]:
                        talks(fun2.run_juanita(response_out_angel.__str__()))
                    if "translate" in history[-1]:
                        trasnlate_replace = response_out_angel.__str__().replace("translate", "")
                        responses.append(ai.predict1(trasnlate_replace))
                        talks(responses[-1])
                    if "complete" in history[-1]:
                        complete_replace = response_out_angel.__str__().replace("complete", "")
                        responses.append(ai.predict2(complete_replace))
                        print(responses[-1])
                        talks(responses[-1])
                    if "hello" not in history[-1] or "reproduce" not in history[-1] or "search" not in history[-1] or "help" not in history[-1] or "complete" not in history[-1] or "translate" not in history[-1]:
                        print("conversacion")
                        respu = ai.predict(response_out_angel[1:])
                        responses.append(respu)
                        print(responses)
                        talks(respu)
        else:
            print("Try again")
            talks("Try again calling me first.")
    return render_template("index.html", responses=responses, history=history)