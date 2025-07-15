import speech_recognition as sr

# Inicializa o reconhecedor
reconhecedor = sr.Recognizer()

# Usa o microfone como fonte de áudio
with sr.Microphone() as fonte:
    print("Fale algo:")
    audio = reconhecedor.listen(fonte)

    try:
        texto = reconhecedor.recognize_google(audio, language='pt-BR')
        print("Você disse:", texto)
    except sr.UnknownValueError:
        print("Não entendi o que foi dito.")
    except sr.RequestError:
        print("Erro ao se conectar com o serviço de reconhecimento.")
