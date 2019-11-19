from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.recycleview import RecycleView

#from kivy.uix.widget import Butt

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
    #icon='/mnt/369071E49071AB4F/MyLab/Space/project_box/training/calculator_in_kivy/icon-picture-1.ico'

if __name__=='__main__':
    calculatorApp().run()