import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from screeninfo import get_monitors
from tkinter.filedialog import askopenfilename


class GUI:
    def __init__(self):
        self.__SCREEN_HEIGHT = get_monitors()[0].height
        self.__SCREEN_WIDTH = get_monitors()[0].width
        self.__SIZE = f"800x800+{int(self.__SCREEN_WIDTH / 2 - 400)}+{int(self.__SCREEN_HEIGHT / 2 - 400)}"
        self.file_path = str()

        self.window = ThemedTk(theme="breeze")
        self.label_path = ttk.Label(text="TEST")
        self.label_path.pack(side=tk.TOP, pady=20)
        self.select_file_btn = ttk.Button(self.window, text='Select file', command=self.select_file)
        self.select_file_btn.pack(side=tk.TOP, pady=20)
        self.generate_btn = ttk.Button(self.window, text='Generate', command=self.generate)
        self.generate_btn.pack(side=tk.TOP, pady=20)
        self.save_btn = ttk.Button(self.window, text='Save as PDF', command=self.generate)
        self.save_btn.pack(side=tk.BOTTOM, pady=20)
        self.window.iconbitmap('const/main_icon.ico')
        self.window.title('Assembler tree drawer')
        self.window.geometry(self.__SIZE)
        self.window.mainloop()

    def select_file(self):
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

    def generate(self):
        print('Generating...')

    def save(self):
        print('Saving PDF...')


if __name__ == '__main__':
    main_gui = GUI()
