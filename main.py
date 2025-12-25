from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Hello GitHub Actions!")

if _name_ == "_main_":
    MyApp().run()
