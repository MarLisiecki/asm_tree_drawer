
from graphviz import Graph

from code_parser import Parser


class Drawer:
    def configure_graph(self) -> Graph:
        graph = Graph("ER", filename='output.gv', engine='neato')
        graph.attr('node', shape='box')
        return graph

    def create_nodes(self, labels_dict) -> None:
        graph = self.configure_graph()
        for label in labels_dict.keys():
            graph.node(label)
        graph.view()


if __name__ == '__main__':
    prs = Parser('test_file.asm')
    labels = prs.find_labels()
    drw = Drawer()
    drw.create_nodes(labels)
