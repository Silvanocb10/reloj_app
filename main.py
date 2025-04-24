from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.reloj_screen import RelojScreen
from screens.cronometro_screen import CronometroScreen
from screens.alarma_screen import AlarmaScreen  # ← Importar aquí

class RelojApp(App):
    def build(self):
        Builder.load_file("reloj.kv") 
        
        sm = ScreenManager()
        sm.add_widget(RelojScreen(name='reloj'))
        sm.add_widget(CronometroScreen(name='cronometro'))
        sm.add_widget(AlarmaScreen(name='alarma'))  # ← Agregar aquí
        return sm

if __name__ == '__main__':
    RelojApp().run()
