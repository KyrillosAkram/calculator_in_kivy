from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.recycleview import RecycleView

class lay(BoxLayout):
    theinput=ObjectProperty()

    def calculate(self,calculation):
        try:
            print(calculation)
            return eval(calculation)

        except:
            return 'Error'


class calculatorApp(App):
    title="Calculator"

if __name__=='__main__':
    calculatorApp().run()