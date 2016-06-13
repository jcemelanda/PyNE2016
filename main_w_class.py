from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        layout = BoxLayout()
        label = Label(text='PyNE 2016')
        button = Button(text='Yay!')
        layout.add_widget(label)
        layout.add_widget(button)

        return layout


if __name__ == '__main__':
    MyApp().run()
