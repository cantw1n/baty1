from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.counter = 0
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Счетчик: 0")
        button = Button(text="Нажми меня")
        button.bind(on_press=self.on_button_press)
        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout

    def on_button_press(self, instance):
        self.counter += 1
        self.label.text = f"Счетчик: {self.counter}"

if __name__ == "__main__":
    MyApp().run()
