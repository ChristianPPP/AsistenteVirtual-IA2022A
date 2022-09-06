# AsistenteVirtual-IA2022A
Repositorio para almacenar el proyecto de asistente virtual desarrollado en Python con inteligencia artificial.
El asistente virtual "Angel" implementa reonocimiento de voz para determinar que función cumplir, ademas de implementar funcionalidades como la búsqueda por internet, ejecutar programas; el asistente puede mantener una conversación casual, traducción y completar frases gracias a la implementación de un modelos de inteligencia artificial usando la librería transformers, el sistema fue diseñado para trabajar como una aplicación web para lo cual se empleó Flask para el manejo de peticiones.

# Integrantes

- Poleth Arias
- María José Chalá
- Christian Palacios

# Videos de YouTube

Video de explicación técnica del código y la funcionalidad: https://youtu.be/xthvE5shJZk

Video de manual de usuario: https://youtu.be/crf7l3lqmjs

Link del informe:  [Informe](https://epnecuador-my.sharepoint.com/:b:/g/personal/maria_chala_epn_edu_ec/Ed8GS1kvk-1FgWtfcHlZK5IB6q2pH3nXARwxWJHs-qKY9g?e=K6FHqH)

# 
### Explicación general📋

Para el reconocimiento automático del habla se utilizan varios algoritmos y técnicas de cálculo para reconocer el habla y convertirla en texto y mejorar la precisión de la transcripción. En dicho contexto, para la implementación de la página web se tomo en cuenta el siguiente método:
-	Procesamiento de lenguaje natural (NLP). - es el área de la inteligencia artificial que se centra en la interacción entre humanos y máquinas a través del lenguaje y a través del habla y el texto. Muchos dispositivos móviles incorporan el reconocimiento de voz en sus sistemas para realizar búsquedas de voz, por ejemplo, Siri, o aumentar la accesibilidad de la escritura.
A partir de este método, se definieron los modelos a tomar en cuenta para implementarlos como parte de las funcionalidades de la aplicación. A continuación, se detallan los modelos tomados en consideración: 
-	 ChatBot. – Se implementó este modelo para mantener una charla fluida con el asistente virtual y que este sea capaz de responder a preguntas o peticiones que se realicen.
-	Translate. – Este método permite traducir alguna palabra o frase.
-	TextGeneration. -  Este método permite escribir contenidos automáticamente


### Módulo de conversación 

A.	Conversación con el asistente virtual
Primero se importaron las librerías requeridas y las funciones fun1 y fun2, que contienen algunas funcionalidades que se implementaron para el Chatbot.

```
from transformers import *
import speech_recognition as sr
import pyttsx3
import fun1, fun2
from flask import Flask, request, render_template, redirect
```

Luego, se definieron las variables necesarias como se muestra a continuación.

```
app = Flask(__name__)
UPLOAD_FOLDER = 'files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 4.0)
history = []
responses = []
```

En cuanto al desarrollo del Chatbot, fue necesario entrenar al bot para que detecte la intención en la entrada de texto del usuario, para ello, le proporcionamos a la herramienta algunas frases o palabras clave que recibirá como entradas y dependiendo de ello se ejecutará lo que el usuario pida, ya sea entablar una conversación o pedirle que realice consultas o abra un programa en específico, entre otros.




### Módulo para traducir una palabra o texto 
Para la implementación del traductor de texto, se definió la función predict1, en donde, a partir de la variable “translator” se inicializa el pipeline, que recibe como parámetros: el idioma al cual se desea traducir, en este caso se traducirá el texto a español; el modelo de procesamiento de lenguaje natural "Helsinki-NLP/opus-mt-en-es" para la respectiva traducción; y el tokenizer, que almacena el vocabulario del modelo establecido. Finalmente, a través de la variable “resul”, se presentará la traducción del texto ingresado.
 



Para que la implementación de este método funcioné, dentro de las funcionalidades que presenta el Chatbot, tenemos que, si al asistente se le presenta como entrada la palabra “translate” como se muestra en la figura a continuación, se accederá a la función para luego realizar el respectivo procedimiento mencionado anteriormente
 




### Módulo para la generación de texto

Para la implementación de este método, se definió la función predict2 en donde, a partir de la variable “text_gen_pipeline” se inicializa el pipeline, que recibe como primer parámetro “text-generation” que hace al generador de texto como tal; el siguiente parámetro que recibe es el modelo GPT-2 el cual es el más popular en la generación de lenguaje. Esta función retorna el texto generado en una variable llamada output como se muestra en la figura a continuacion.



Para acceder a este método, si el asistente recibe como entrada la palabra “Complete”, se accederá a la función “predict2” que como ya se mencionó anteriormente, contiene toda la lógica para que dicho método funcione.
 


