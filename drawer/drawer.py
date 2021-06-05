from graphviz import Graph


# Class for creating graph
class Drawer:
    def configure_graph(self) -> Graph:
        """
        Fucntion which configure graph with initial parameters.

        :return: Graph object
        """
        graph = Graph('structs', filename='output.gv', engine='dot')
        graph.attr('node', shape='box', fixed_size='true')
        return graph

    def create_nodes_with_edges(self, list_of_mnemo_obj: list, labels_with_code_dict: dict) -> Graph:
        """
        Function which creates nodes and edges for graph

        :param list_of_mnemo_obj: List of mnemonics objects (contains links between labels)
        :param labels_with_code_dict: Dictionary which contains labels (key) with labels's code (value)
        :return: Graph: Final graph with proper edges and nodes
        """
        graph = self.configure_graph()

        # Create nodes

        for element in list_of_mnemo_obj:

            # Normalize code for proper display in node

            graph.node(shape='record', name=element.root,
                       label="{" + element.root + "|" + labels_with_code_dict[element.root].replace('\n', '\\l') + "}")
            try:
                graph.node(shape='record', name=element.target_label,
                           label="{" + element.target_label + "|" + labels_with_code_dict[element.target_label].replace(
                               '\n', '\\l') + "}")
            except KeyError:
                pass

        # Set links between nodes

        for element in list_of_mnemo_obj:
            graph.edge(element.root, element.target_label, label=element.name, labeltooltip=element.jump_type,
                       dir='forward')
        graph.render(format='png')
        return graph


if __name__ == '__main__':
    pass
