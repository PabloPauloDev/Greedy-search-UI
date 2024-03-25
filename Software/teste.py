from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MeuLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MeuLayout, self).__init__(**kwargs)
        
        # Exemplo de BoxLayout horizontal
        box_layout_horizontal = BoxLayout(orientation='horizontal')
        box_layout_horizontal.add_widget(Button(text='Botão 1'))
        box_layout_horizontal.add_widget(Button(text='Botão 2'))
        
        # Exemplo de GridLayout
        grid_layout = GridLayout(cols=2)
        grid_layout.add_widget(Label(text='Nome:'))
        grid_layout.add_widget(TextInput())
        grid_layout.add_widget(Label(text='Idade:'))
        grid_layout.add_widget(TextInput())
        
        # Exemplo de FloatLayout
        float_layout = FloatLayout()
        float_layout.add_widget(Button(text='Botão 3', pos_hint={'x':0.1, 'y':0.1}))
        
        # Adicionando layouts ao layout principal (BoxLayout vertical)
        self.add_widget(box_layout_horizontal)
        self.add_widget(grid_layout)
        self.add_widget(float_layout)

class MinhaApp(App):
    def build(self):
        return MeuLayout()

if __name__ == '__main__':
    MinhaApp().run()
