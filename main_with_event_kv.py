from kivy.app import App
from kivy.uix.button import Button


class MyButton(Button):
    def ai(self):
        self.text = 'Ai!'


class MyEventApp(App):
    pass

if __name__ == '__main__':
    MyEventApp().run()
