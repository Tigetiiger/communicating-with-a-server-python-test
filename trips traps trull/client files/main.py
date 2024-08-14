import customtkinter
from PIL import Image

last_objekt = None
control_map = [[None, None, None],[None, None, None],[None, None, None]]
red_map = [[None, None, None],[None, None, None],[None, None, None]]
blue_map = [[None, None, None],[None, None, None],[None, None, None]]

def bitmap_locate_win(map):
    if locate_win_row(map) or locate_win_column(map) or locate_win_diagonal(map):
        return True

def locate_win_row(map):
    for i in map:
        try:
            if sum(i) == 3:
                return True
        except:
            ...
    return False

def locate_win_column(map):
    for i in range(3):
        try:
            if sum([map[0][i], map[1][i], map[2][i]]) == 3:
                return True
        except:
            ...
    return False

def locate_win_diagonal(map):
    try:
        if sum([map[0][0], map[1][1], map[2][2]]) == 3:
            return True
    except:
        ...
    try:
        if sum([map[0][2], map[1][1], map[2][0]]) == 3:
            return True
    except:
        ...
    return False
def location_taken(button_pos: tuple):
    global control_map
    if not control_map[button_pos[0]][button_pos[1]] == None:
        return True
    else:
        control_map[button_pos[0]][button_pos[1]] = 1
        print(control_map)
        return False

class main(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("LOL")
        self.geometry(f"{501}x{501}")
        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)
        for i in range(0, 3):
            for j in range(0, 3):
                self.make_button(j,i)
        self.mainloop()

    def game_end(self, winner):
        self.win_label = customtkinter.CTkLabel(self, text=f"winner is {winner}",)
        self.win_label.grid(row=0, rowspan=3, column=0, columnspan=3, sticky="nsew")
    def move(self, element, button_pos: tuple):
        global last_objekt
        global red_map, blue_map
        if location_taken(button_pos):
            return
        if last_objekt in [None, "blue"]:
            element.configure(state=customtkinter.DISABLED, image=customtkinter.CTkImage(Image.open("sprites/red.png"), size=(100,100)), text="")
            last_objekt = "red"
            red_map[button_pos[1]][button_pos[0]] = 1
            if bitmap_locate_win(red_map):
                self.game_end("red")
        else:
            element.configure(state=customtkinter.DISABLED, image=customtkinter.CTkImage(Image.open("sprites/blue.png"), size=(100, 100)), text="")
            last_objekt = "blue"
            blue_map[button_pos[1]][button_pos[0]] = 1
            if bitmap_locate_win(blue_map):
                self.game_end("blue")

    def make_button(self, x, y):
        self.button = customtkinter.CTkButton(self, text="test", width=157, height=157)
        self.button.grid(row=y, column=x, pady=5, padx=5, sticky="nsew")
        def on_press(button = self.button):
            return self.move(button, (y,x))

        self.button.configure(command=on_press)


if __name__ == '__main__':
    main()