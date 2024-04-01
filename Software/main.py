from kivy.app import App
from kivy.uix.widget import Widget
from logic import Logic
from graph import graph

class MeuLayout(Widget):

    def grafo(self):
        grafo = graph()
        grafo.gerar_grafo()

    def buscar(self):

        logic = Logic()
        logic.busca(self.ids.origem.text, self.ids.destino.text)



class GreedySearch(App):
    
    def build(self):
        return MeuLayout()

if __name__ == '__main__':
    GreedySearch().run()