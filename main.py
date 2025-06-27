from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import platform

# Android TTS
if platform == "android":
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
    Locale = autoclass('java.util.Locale')

class Comunicador(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.frases = [
            "Olá!",
            "Obrigado!",
            "Sim",
            "Não",
            "Quero comer.",
            "Estou com sede.",
            "Estou com frio.",
            "Estou com calor.",
            "Youtube.",
            "Estou com dor.",
            "Me ajude, por favor.",
            "Estou cansado.",
        ]

        # Iniciar TTS no Android
        if platform == "android":
            self.tts = TextToSpeech(PythonActivity.mActivity, None)
            self.tts.setLanguage(Locale("pt", "BR"))
        else:
            self.tts = None

        # Criar botões
        for frase in self.frases:
            botao = Button(text=frase, font_size=24, size_hint_y=None, height=80)
            botao.bind(on_press=self.falar)
            self.add_widget(botao)

    def falar(self, instance):
        frase = instance.text
        if self.tts:
            self.tts.speak(frase, TextToSpeech.QUEUE_FLUSH, None, None)
        else:
            print(f"(Simulação de fala): {frase}")

class ComunicadorApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # fundo branco
        return Comunicador()

if __name__ == '__main__':
    ComunicadorApp().run()