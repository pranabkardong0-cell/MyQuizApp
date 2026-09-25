from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class QuizApp(App):

    def build(self):
        self.score = 0

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        title = Label(
            text="MY QUIZ APP",
            font_size=30
        )

        question = Label(
            text="India ki capital kya hai?",
            font_size=22
        )

        button1 = Button(text="Mumbai")
        button2 = Button(text="Delhi")
        button3 = Button(text="Kolkata")

        button1.bind(on_press=self.wrong)
        button2.bind(on_press=self.correct)
        button3.bind(on_press=self.wrong)

        layout.add_widget(title)
        layout.add_widget(question)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)

        return layout

    def correct(self, instance):
        instance.text = "✅ Correct!"

    def wrong(self, instance):
        instance.text = "❌ Wrong!"


QuizApp().run()