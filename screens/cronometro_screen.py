from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

class CronometroScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.segundos = 0
        self.evento = None

    def actualizar(self, dt):
        self.segundos += 1
        minutos = self.segundos // 60
        segundos = self.segundos % 60
        self.ids.cronometro_label.text = f"{minutos:02}:{segundos:02}"

    def iniciar(self):
        if not self.evento:
            self.evento = Clock.schedule_interval(self.actualizar, 1)

    def detener(self):
        if self.evento:
            self.evento.cancel()
            self.evento = None

    def reiniciar(self):
        self.detener()
        self.segundos = 0
        self.ids.cronometro_label.text = "00:00"
