from kivy.app import App
from kivy.uix.widget import Widget
from logic import Logic
from graph import graph

class MeuLayout(Widget):

    texto_resp = ''
    lista_visited = []

    def grafo(self):
        grafo = graph()
        grafo.gerar_grafo(self.lista_visited)

    def buscar(self):

        logic = Logic()
        logic.busca(self.ids.origem.text, self.ids.destino.text)
        self.ids.label_resp.text = logic.texto
        self.ids.label_resp.texture_update()
        self.lista_visited = logic.visited
        print(self.lista_visited)

class GreedySearch(App):
    
    def build(self):
        return MeuLayout()

if __name__ == '__main__':
    GreedySearch().run()