from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from datetime import datetime

class RelojScreen(Screen):
    hora_actual = "Cargando..."

    def on_enter(self):
        Clock.schedule_interval(self.actualizar_hora, 1)

    def on_leave(self):
        Clock.unschedule(self.actualizar_hora)

    def actualizar_hora(self, *args):
        self.ids.hora_label.text = datetime.now().strftime("%H:%M:%S")
