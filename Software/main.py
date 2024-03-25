from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget

class MeuLayout(Widget):
    

    def exibir_opcao_selecionada(self, instance):
        # Exibindo a opção selecionada quando o botão é clicado
        opcao_selecionada = self.spinnerOrigin.text
        print("Opção selecionada:", opcao_selecionada)

class GreedySearch(App):
    def build(self):
        return MeuLayout()

if __name__ == '__main__':
    GreedySearch().run()