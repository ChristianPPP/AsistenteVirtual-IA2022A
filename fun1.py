import pywhatkit, os

name="angel" #nombre del asistente

programs ={
    'soon':r"C:\\Users\\USER\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe",
    'word':r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word 2016.exe",
    'navigator':r"C:\Program Files\Google\Chrome\Application\chrome.exe"
}

def run_angel(rec):
    if 'reproduce' in rec:
        music=rec.replace('reproduce', '')
        print("Reproduciendo..."+music)
        pywhatkit.playonyt(music)
    elif 'open' in rec:
        for app in programs:
            if app in rec:
                os.startfile(programs[app])