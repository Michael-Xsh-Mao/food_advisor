import tkinter as tk
from Controller import Controller


class GUIMain:

    def __init__(self, controller):
        self.root = tk.Tk()
        self.controller = controller
        self.gui_info = []
        self.listboxes = {}

    def setup_GUI(self):
        self.root.title("Brocado")
        self.setup_sidebar()
        self.setup_personal_info_screen()
        self.setup_food_management()
        self.setup_warnings_screen()

    def setup_sidebar(self):
        sidebar = tk.Frame(self.root, height=500, width=300, bg="#CCC")
        sidebar.pack(expand=False, fill="both", side="left", anchor="nw")

        # Personal Info
        info_label = tk.Label(sidebar, text='Personal Info',
                              bg="#CCC", font=('bold', 14), pady=5, padx=5)
        info_label.grid(row=0, column=0, sticky="w")

        name_label = tk.Label(sidebar, text='   - Name: Tomato', bg="#CCC")
        name_label.grid(row=1, column=0, sticky="w")
        self.gui_info.append(name_label)

        energy_needs_label = tk.Label(sidebar, text='   - Daily Requirements', bg="#CCC")
        energy_needs_label.grid(row=2, column=0, sticky="w")

        protein_needs_label = tk.Label(sidebar, text='     - Protein: 5g', bg="#CCC")
        protein_needs_label.grid(row=3, column=0, sticky="w")
        self.gui_info.append(protein_needs_label)

        calorie_needs_label = tk.Label(sidebar, text='     - Calories: 2000', bg="#CCC")
        calorie_needs_label.grid(row=4, column=0, sticky="w")
        self.gui_info.append(calorie_needs_label)

        fat_needs_label = tk.Label(sidebar, text='     - Fat: 5g', bg="#CCC")
        fat_needs_label.grid(row=5, column=0, sticky="w")
        self.gui_info.append(fat_needs_label)

        # Today's Consumption
        info_label = tk.Label(sidebar, text='Consumed Today',
                              bg="#CCC", font=('bold', 14), pady=5, padx=5)
        info_label.grid(row=6, column=0, sticky="w")

        protein_consumed_label = tk.Label(sidebar, text='   - Protein: 70g', bg="#CCC")
        protein_consumed_label.grid(row=7, column=0, sticky="w")
        self.gui_info.append(protein_consumed_label)

        calorie_consumed_label = tk.Label(sidebar, text='   - Calories: 20000', bg="#CCC")
        calorie_consumed_label.grid(row=8, column=0, sticky="w")
        self.gui_info.append(calorie_consumed_label)

        fat_consumed_label = tk.Label(sidebar, text='   - Fat: 5g', bg="#CCC")
        fat_consumed_label.grid(row=9, column=0, sticky="w")
        self.gui_info.append(fat_consumed_label)

        # Inventory Status
        inventory_status_label = tk.Label(sidebar, text='Inventory Status',
                                          bg="#CCC", font=('bold', 14), pady=5, padx=5)
        inventory_status_label.grid(row=10, column=0, sticky="w")

        food_quantity_label = tk.Label(sidebar, text='   - You have no food!', bg="#CCC")
        food_quantity_label.grid(row=11, column=0, sticky="w")
        self.gui_info.append(food_quantity_label)

        expiration_label = tk.Label(sidebar, text='   - Nothing Expiring!', bg="#CCC")
        expiration_label.grid(row=12, column=0, sticky="w")
        self.gui_info.append(expiration_label)

        more_info_label = tk.Label(sidebar, text='        more info in details tab', bg="#CCC", font=('italic', 8))
        more_info_label.grid(row=13, column=0, sticky="w")

        self.update_gui_info()

    def update_gui_info(self):
        # update sidebar
        personal_info = self.controller.personal_needs()
        self.gui_info[0]['text'] = "   - Name: " + personal_info[0]
        self.gui_info[1]['text'] = "     - Protein: " + str(personal_info[1]) + "g"
        self.gui_info[2]['text'] = "     - Calories: " + str(personal_info[2]) + "kcal"
        self.gui_info[3]['text'] = "     - Fat: " + str(personal_info[3]) + "g"

        personal_info = self.controller.nutrient_info()
        self.gui_info[4]['text'] = "   - Protein: " + str(personal_info[1]) + "g"
        self.gui_info[5]['text'] = "   - Calories: " + str(personal_info[0]) + "kcal"
        self.gui_info[6]['text'] = "   - Fat: " + str(personal_info[2]) + "g"

        personal_info = self.controller.inventory_status()
        self.gui_info[7]['text'] = "   - " + personal_info[0]
        self.gui_info[8]['text'] = "   - " + personal_info[1]

        # update Warnings
        if 'warning' in self.listboxes:
            self.listboxes['warning'].delete(0, tk.END)
            for line in self.controller.get_all_warnings():
                self.listboxes['warning'].insert(tk.END, line)


    def setup_personal_info_screen(self):
        personal_info_screen = tk.Frame(self.root, height=500, width=500, relief="sunken", border=2)
        personal_info_screen.pack(expand=False, fill="both", side="right")

        title_label = tk.Label(personal_info_screen, text='Personal Details', font=("bold", 14))
        title_label.grid(row=0, column=0, sticky="w")

        name_label = tk.Label(personal_info_screen, text='Name: ')
        name_label.grid(row=1, column=0, sticky="w")

        name_entry = tk.Entry(personal_info_screen, bd=2)
        name_entry.grid(row=1, column=1, sticky="w")

        weight_label = tk.Label(personal_info_screen, text='Weight (kg): ')
        weight_label.grid(row=2, column=0, sticky="w")

        weight_entry = tk.Entry(personal_info_screen, bd=2)
        weight_entry.grid(row=2, column=1, sticky="w")

        age_label = tk.Label(personal_info_screen, text='Age: ')
        age_label.grid(row=3, column=0, sticky="w")

        age_entry = tk.Entry(personal_info_screen, bd=2)
        age_entry.grid(row=3, column=1, sticky="w")

        height_label = tk.Label(personal_info_screen, text='Height (cm): ')
        height_label.grid(row=4, column=0, sticky="w")

        height_entry = tk.Entry(personal_info_screen, bd=2)
        height_entry.grid(row=4, column=1, sticky="w")

        sex_label = tk.Label(personal_info_screen, text='Sex: ')
        sex_label.grid(row=5, column=0, sticky="w")

        sex_var = tk.IntVar()
        sex_male_rb = tk.Radiobutton(personal_info_screen, variable=sex_var, text="Male", value=1)
        sex_male_rb.grid(row=5, column=1, sticky="w")
        sex_female_rb = tk.Radiobutton(personal_info_screen, variable=sex_var, text="Female", value=2)
        sex_female_rb.grid(row=6, column=1, sticky="w")

        active_label = tk.Label(personal_info_screen, text='Activity Level (1 lowest, 5 highest): ')
        active_label.grid(row=7, column=0, sticky="w")

        active_var = tk.IntVar()
        active1_rb = tk.Radiobutton(personal_info_screen, variable=active_var, text="1", value=1)
        active1_rb.grid(row=7, column=1, sticky="w")
        active2_rb = tk.Radiobutton(personal_info_screen, variable=active_var, text="2", value=2)
        active2_rb.grid(row=8, column=1, sticky="w")
        active3_rb = tk.Radiobutton(personal_info_screen, variable=active_var, text="3", value=3)
        active3_rb.grid(row=9, column=1, sticky="w")
        active4_rb = tk.Radiobutton(personal_info_screen, variable=active_var, text="4", value=4)
        active4_rb.grid(row=10, column=1, sticky="w")
        active5_rb = tk.Radiobutton(personal_info_screen, variable=active_var, text="5", value=5)
        active5_rb.grid(row=11, column=1, sticky="w")

        screen_elements = [name_entry, sex_var, age_entry, weight_entry, height_entry, active_var]

        update_button = tk.Button(personal_info_screen, text="Update Info",
                                  command=lambda: self.update_info(screen_elements))
        update_button.grid(row=12, column=1)

    def setup_food_management(self):
        food_management_screen = tk.Frame(self.root, height=500, width=500, relief="sunken", border=2)
        food_management_screen.pack(expand=False, fill="both", side="right")

        title_label = tk.Label(food_management_screen, text='Food Management', font=("bold", 14))
        title_label.grid(row=0, column=0, sticky="w")

        name_label = tk.Label(food_management_screen, text='Name of Food: ')
        name_label.grid(row=1, column=0, sticky="w")

        name_entry = tk.Entry(food_management_screen, bd=2)
        name_entry.grid(row=1, column=1, sticky="w")

        quantity_label = tk.Label(food_management_screen, text='Quantity (g): ')
        quantity_label.grid(row=2, column=0, sticky="w")

        quantity_entry = tk.Entry(food_management_screen, bd=2)
        quantity_entry.grid(row=2, column=1, sticky="w")

        expiration_label = tk.Label(food_management_screen, text='Expiration Date (for adding food): ')
        expiration_label.grid(row=3, column=0, sticky="w")

        date_label = tk.Label(food_management_screen, text='yyyy-mm-dd')
        date_label.grid(row=4, column=0, sticky="w")

        date_entry = tk.Entry(food_management_screen, bd=2)
        date_entry.grid(row=4, column=1, sticky="w")

        screen_elements = [name_entry, quantity_entry, date_entry]

        add_button = tk.Button(food_management_screen, text="Add Food",
                               command=lambda: self.add_food(screen_elements))
        add_button.grid(row=5, column=1)

        eaten_button = tk.Button(food_management_screen, text="Eaten Food",
                                 command=lambda: self.ate_food(screen_elements[:2]))
        eaten_button.grid(row=6, column=1)

        remove_button = tk.Button(food_management_screen, text="Remove Food",
                                  command=lambda: self.remove_food(screen_elements[:2]))
        remove_button.grid(row=7, column=1)

    def setup_warnings_screen(self):
        warnings_screen = tk.Frame(self.root, height=500, width=500, relief="sunken", border=2)
        warnings_screen.pack(expand=False, fill="both", side="right")

        scrollbar = tk.Scrollbar(warnings_screen)
        scrollbar.pack(side="right", fill="y")

        warning_list = tk.Listbox(warnings_screen, yscrollcommand=scrollbar.set, width=50)
        self.listboxes["warning"] = warning_list

        for line in self.controller.get_all_warnings():
            warning_list.insert(tk.END, line)

        warning_list.pack(side="left", fill="both")
        scrollbar.config(command=warning_list.yview)

    def add_food(self, screen_elements):
        screen_elements = extract_screen_elements_info(screen_elements)
        self.controller.add_food(screen_elements[0],
                                 float(screen_elements[1]),
                                 screen_elements[2])
        self.update_gui_info()

    def ate_food(self, screen_elements):
        screen_elements = extract_screen_elements_info(screen_elements)
        self.controller.eat_food(screen_elements[0], float(screen_elements[1]))
        self.update_gui_info()

    def remove_food(self, screen_elements):
        screen_elements = extract_screen_elements_info(screen_elements)
        self.controller.trash_food(screen_elements[0], float(screen_elements[1]))
        self.update_gui_info()

    def update_info(self, screen_elements):
        screen_elements = extract_screen_elements_info(screen_elements)
        screen_elements[1] = "male" if screen_elements[1] == 1 else "female"
        for i in range(2,5):
            screen_elements[i] = float(screen_elements[i])
        self.controller.enter_personal_info(screen_elements)

        self.update_gui_info()


def extract_screen_elements_info(screen_elements):
    converted_elements = []
    for i, element in enumerate(screen_elements):
        converted_elements.append(element.get())

    return converted_elements


if __name__ == '__main__':
    control = Controller()
    gui = GUIMain(control)
    gui.setup_GUI()
    gui.root.mainloop()
