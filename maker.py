
from tkinter import *
from tkinter import filedialog


class win:
    def __init__(self, win: Tk):
        self.windows = win
        self.windows.title('RTO')
        self.windows.config(background='lightblue')
        self.windows.geometry("1080x1920")
        self.back_image_path = 'back.jpg'
        self.front_image_path = 'font.jpg'
        self.doc_image_path = './out'

    def create_label(self, text, row, column, px=20, py=20,) -> Label:
        l1 = Label(self.windows, text=f'{text}'.upper(
        ), font="bold", bg="lightblue")
        l1.grid(padx=(px, 0), pady=(py, 0))
        l1.grid(row=row, column=column)
        return l1

    def create_dropdown(self, array: list, r, c):
        string = StringVar()
        dropdown = OptionMenu(self.windows, string, *array)
        dropdown.grid(row=r, column=c)
        dropdown.grid(padx=(20, 0), pady=(20, 0))
        return string, dropdown

    def create_input(self,  row, column, px=20, py=20,) -> Entry:
        inputs = Entry(self.windows)
        inputs.grid(padx=(px, 0), pady=(py, 0))
        inputs.grid(row=row, column=column)
        return inputs

    def browseFiles_front(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("Text files",
                                                          "*.jpg*"),
                                                         ("all files",
                                                          "*.*")))

        # Change label contents
        self.front_image_path = filename

    def browseFiles_back(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("Text files",
                                                          "*.jpg*"),
                                                         ("all files",
                                                          "*.*")))

        # Change label contents
        self.back_image_path = filename

    def browseFiles_doc(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(
                                                         ("Text files",
                                                          "*.jpg*"),
                                                         ("all files",
                                                          "*.*")))

        # Change label contents
        self.doc_image_path = filename

    def outer_floder(self):
        file = filedialog.askdirectory()
        self.out = file

    def run(self):
        self.windows.mainloop()
