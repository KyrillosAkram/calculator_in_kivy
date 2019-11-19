from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from playsound import playsound
from kivy.properties import ObjectProperty
from kivy.uix.recycleview import RecycleView

#from kivy.uix.widget import Butt

class lay(BoxLayout):
    ''',RecycleViewdef __init__(**kwarg):
        super(lay,self).__init__(**kwarg)
        self.data=[{'text':str(x)} for x in range(30)]'''
    theinput=ObjectProperty()

    def calculate(self,calculation):
        try:
            print(calculation)
            return eval(calculation)

        except:
            return 'Error'

#    def woof(self):
#        playsound("Dog-Woof-SoundBible.com-457935112.mp3")
#        print("woof !!\n")


class calculatorApp(App):
    title="Calculator"
    icon="icon-picture-1.jpg"

if __name__=='__main__':
    calculatorApp().run()