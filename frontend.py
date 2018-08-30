from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Menu(Widget):

    def MenuLayout(self, *args):
        numOfChildren = len(self.children)
        height = self.height
        heightPerChild = height / numOfChildren

        position = 1
        for child in self.children:
            child.x = self.x
            child.width = self.width
            
            child.height = heightPerChild
            position = position + 1
    def on_size(self, *args):
        self.MenuLayout()

    def on_pos(self, *args):
        self.MenuLayout()


class GUI(Widget):
    pass


class GradDatabase(App):
    def build(self):
        interface = GUI()
        return interface

GradDatabase().run()
