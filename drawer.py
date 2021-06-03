from graphviz import Graph

from code_parser import Parser


class Drawer:
    def configure_graph(self) -> Graph:
        graph = Graph("G", filename='output.gv', engine='dot')
        graph.attr('node', shape='box', fixed_size='true')
        return graph

    def create_nodes_with_edges(self, list_of_mnemo_obj) -> None:
        graph = self.configure_graph()
        for element in list_of_mnemo_obj:
            graph.node(element.root)
            graph.node(element.target_label)
        for element in list_of_mnemo_obj:
            graph.edge(element.root, element.target_label, label=element.name, dir='forward')
        graph.view()


if __name__ == '__main__':
    prs = Parser('test_file.asm')
    labels_dict = prs.find_labels()
    labels_with_code_dict = prs.find_code_under_labels(labels_dict)
    list_of_mnemo_obj = prs.find_mnemonics(labels_with_code_dict)
    drw = Drawer()
    drw.create_nodes_with_edges(list_of_mnemo_obj)
