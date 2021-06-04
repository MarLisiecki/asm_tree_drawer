from graphviz import Graph

from code_parser.code_parser import Parser


class Drawer:
    def configure_graph(self) -> Graph:
        graph = Graph('structs', filename='../output.gv', engine='dot')
        graph.attr('node', shape='box', fixed_size='true')
        return graph

    def create_nodes_with_edges(self, list_of_mnemo_obj: list, labels_with_code_dict: dict) -> None:
        """

        :param list_of_mnemo_obj: Objects
        :param labels_with_code_dict:
        :return:
        """
        graph = self.configure_graph()
        for element in list_of_mnemo_obj:
            graph.node(shape='record', name=element.root,
                       label="{" + element.root + "|" + labels_with_code_dict[element.root].replace('\n', '\\l') + "}")
            try:
                graph.node(shape='record', name=element.target_label,
                           label="{" + element.target_label + "|" + labels_with_code_dict[element.target_label].replace(
                               '\n',
                               '\\l') + "}")
            except KeyError:
                pass
        for element in list_of_mnemo_obj:
            graph.edge(element.root, element.target_label, label=element.name, labeltooltip=element.jump_type, dir='forward')
        graph.render(format = 'png')
        graph.view()



if __name__ == '__main__':
    prs = Parser('../test_file.asm')
    labels_dict = prs.find_labels()
    labels_with_code_dict = prs.find_code_under_labels(labels_dict)
    list_of_mnemo_obj = prs.find_mnemonics(labels_with_code_dict)
    drw = Drawer()
    drw.create_nodes_with_edges(list_of_mnemo_obj, labels_with_code_dict)
    pass
