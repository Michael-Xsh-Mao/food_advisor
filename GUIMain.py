import tkinter as tk


class GUIMain:

    def __init__(self):
        self.root = tk.Tk()

    def setup_GUI(self):
        self.setup_sidebar()
        self.setup_main_area()

    def setup_sidebar(self):
        sidebar = tk.Frame(self.root, height=500, width=300, bg="#CCC")
        sidebar.pack(expand=False, fill="both", side="left", anchor="nw")

        info_label = tk.Label(sidebar, text='Personal Info',
                              bg="#CCC", font=('bold', 14), pady=5, padx=5)
        info_label.grid(row=0, column=0)

        name_label = tk.Label(sidebar, text='- Name: Tomato', bg="#CCC")
        name_label.grid(row=1, column=0, sticky="w")

        protein_needs_label = tk.Label(sidebar, text='- Protein Needs: 5g', bg="#CCC")
        protein_needs_label.grid(row=2, column=0)


    def setup_main_area(self):
        main_area = tk.Frame(self.root, height=500, width=500, relief="sunken", border=2)
        main_area.pack(expand=False, fill="both", side="right")

    def update_main_area(self, screen):
        pass


if __name__ == '__main__':
    gui = GUIMain()
    gui.setup_GUI()
    gui.root.mainloop()
