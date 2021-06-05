import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from ttkthemes import ThemedTk
from screeninfo import get_monitors
from tkinter.filedialog import askopenfilename
from code_parser.code_parser import Parser
from drawer.drawer import Drawer


# You can see SVG preview in PyQt window (just uncomment proper lines)

# Main window class for user interface
class GUI:
    def __init__(self) -> None:
        """
        Initial function with initial parameters and others attributes.

        """
        self.__SCREEN_HEIGHT = get_monitors()[0].height
        self.__SCREEN_WIDTH = get_monitors()[0].width
        self.graph = None
        self.__SIZE = f"800x800+{int(self.__SCREEN_WIDTH / 2 - 400)}+{int(self.__SCREEN_HEIGHT / 2 - 400)}"
        self.file_path = str()
        self.window = ThemedTk(theme="breeze")
        self.label_path = ttk.Label(text="Path to file")
        self.label_path.pack(side=tk.TOP, pady=20)
        self.select_file_btn = ttk.Button(self.window, text='Select file', command=self.select_file)
        self.select_file_btn.pack(side=tk.TOP, pady=20)
        self.generate_btn = ttk.Button(self.window, text='Generate', command=self.generate)
        self.generate_btn.pack(side=tk.TOP, pady=20)
        self.save_btn = ttk.Button(self.window, text='Save as PDF', command=self.save)
        self.save_btn.pack(side=tk.BOTTOM, pady=20)
        # self.show_svg = ttk.Button(self.window, text='Show SVG', command=self.show_svg)
        # self.show_svg.pack(side=tk.BOTTOM, pady=20)
        self.image_as_label = tk.Label(self.window)
        self.image_as_label.pack(side=tk.TOP, pady=20)
        self.image_as_label.configure(text='Your tree')
        self.window.iconbitmap('const/main_icon.ico')
        self.window.title('Assembler tree drawer')
        self.window.geometry(self.__SIZE)
        self.window.mainloop()

    def select_file(self) -> None:
        """
        Function for 'Select file' button which show filedialog with *.asm filter
        After selection change the label from default text to selected file's path

        :return: None
        """
        filetypes = (
            ('Assembler files', '*.asm'),
            ('All files', '*.*')
        )

        filename = tk.filedialog.askopenfilename(
            title='Select a file',
            initialdir='/',
            filetypes=filetypes)

        self.file_path = filename
        self.label_path['text'] = self.file_path

    # TODO: Extract another method to replace label-image
    def generate(self) -> None:
        """
        Function for 'Generate' button which generate graph in dot language and replace label
        with proper image with graph.

        :return: None
        """
        prs = Parser(self.file_path)
        labels_dict = prs.find_labels()
        labels_with_code_dict = prs.find_code_under_labels(labels_dict)
        list_of_mnemo_obj = prs.find_mnemonics(labels_with_code_dict)
        drw = Drawer()
        self.graph = drw.create_nodes_with_edges(list_of_mnemo_obj, labels_with_code_dict)
        image = Image.open('output.gv.png')
        image = image.resize((400, 400), Image.ANTIALIAS)
        image_of_tree = ImageTk.PhotoImage(image)
        self.image_as_label.image = image_of_tree
        self.image_as_label.configure(image=image_of_tree)

    def save(self) -> None:
        """
        Function for 'Save as PDF' button which creates PDF file with graph in folder named 'generated_pdf'

        :return: None
        """
        self.graph.render('generated_pdf/Tree')


# TODO: In future add SVG preview using PyQt
# def show_svg(self):
#     app = QApplication([])
#     window = WidnowForSvg()
#     window.show()
#     app.exec()

# class WidnowForSvg(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(100, 100, 800, 800)
#         self.widgetSvg = QSvgWidget(parent=self)
#         self.svg_tree = 'output.gv.svg'
#         self.widgetSvg.load(self.svg_tree)


if __name__ == '__main__':
    pass
