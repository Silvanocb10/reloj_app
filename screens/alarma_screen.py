from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from datetime import datetime

class AlarmaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.alarma_activada = False
        self.hora_alarma = None
        self.sonido = SoundLoader.load("assets/alarma_sonido.mp3")  # Ruta relativa
        Clock.schedule_interval(self.verificar_alarma, 1)
        Clock.schedule_interval(self.actualizar_reloj_visual, 1)


    def establecer_alarma(self, hora_str):
        try:
            hora_obj = datetime.strptime(hora_str.strip(), "%H:%M").time()
            self.hora_alarma = hora_obj
            self.alarma_activada = True
            print(f"✅ Alarma activada para las {hora_str}")
        except ValueError:
            print("⚠️ Formato incorrecto. Usa HH:MM.")

    def verificar_alarma(self, dt):
        if self.alarma_activada and self.hora_alarma:
            ahora = datetime.now().time()
            if ahora.hour == self.hora_alarma.hour and ahora.minute == self.hora_alarma.minute:
                self.reproducir_alarma()
                self.alarma_activada = False  # Se desactiva después de sonar

    def reproducir_alarma(self):
        if self.sonido:
            self.sonido.play()
            print("🔔 ¡Alarma sonando!")
        else:
            print("❌ No se pudo cargar el sonido de alarma.")

def actualizar_reloj_visual(self, dt):
    hora = datetime.now().strftime("%H:%M:%S")
    if 'reloj_label' in self.ids:
        self.ids.reloj_label.text = hora
