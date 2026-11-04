from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class QRUEApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        layout.add_widget(Label(text='QRUE SOLVER - Egyptian Hacker\nجاري تشغيل النظام...', font_size=18))
        return layout

if __name__ == '__main__':
    QRUEApp().run()
