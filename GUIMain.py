import tkinter as tk


class GUIMain:

    def __init__(self):
        self.root = tk.Tk()

    def setup_GUI(self):
        self.setup_sidebar()
        self.setup_main_area()

    def setup_sidebar(self):
        sidebar = tk.Frame(self.root, height=500, width=200, bg="#CCC")
        sidebar.pack(expand=False, fill="both", side="left", anchor="nw")

    def setup_main_area(self):
        main_area = tk.Frame(self.root, height=500, width=500, relief="sunken", border=2)
        main_area.pack(expand=False, fill="both", side="right")

    def update_main_area(self, screen):
        pass


if '__name__' == '__main__':
    gui = GUIMain()
    gui.root.mainloop()
