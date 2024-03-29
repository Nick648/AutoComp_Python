import customtkinter as ctk
from CTkMessagebox import CTkMessagebox  # icons = ["check", "cancel", "info", "warning", "question"]
from Encoder import Encoder
import tkinter

# Sets the appearance of the window; Supported modes : Light, Dark, System
ctk.set_appearance_mode("System")

# Sets the color of the widgets in the window; Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("green")


def Edit_Was_Made(event: tkinter.Event, entry_text: ctk.CTkTextbox, entry_code: ctk.CTkTextbox, encoder: Encoder):
    print(event, type(event))
    print('->', entry_text.get('1.0', 'end-1c'))
    print('->', entry_text.get('1.0', 'end-1c'))
    user_text = (entry_text.get('1.0', 'end-1c') + event.char).strip()
    encode_mes = encoder.encode_message(message=user_text)
    decode_mes = encoder.decode_message(message=encode_mes)
    entry_code.configure(state='normal')
    entry_code.delete(index1='1.0', index2='end')
    entry_code.insert(index='1.0', text=encode_mes)
    entry_code.configure(state='disabled')
    # print(f"{user_text=}\n{encode_mes=}\n{decode_mes=}")


class FloatSpinbox(ctk.CTkFrame):
    def __init__(self, *args, width: int = 100, height: int = 32, step_size: [int, float] = 1, command=None,
                 type_val: str = 'float', app_encoder: Encoder, **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command
        self.type_val = type_val
        self.app_encoder = app_encoder

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = ctk.CTkButton(self, text="-", width=height - 6, height=height - 6, fg_color='darkorange',
                                             command=self.subtract_button_callback, font=('Arial', 15, 'bold'))
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = ctk.CTkEntry(self, width=width - (2 * height), height=height - 6, font=('Times', 16, 'italic'),
                                  border_width=0, justify='center')
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="nsew")

        self.add_button = ctk.CTkButton(self, text="+", width=height - 6, height=height - 6, font=('Arial', 15),
                                        command=self.add_button_callback, fg_color='darkorange')
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "3")
        self.entry.configure(state="disabled")

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) + self.step_size
            if self.type_val == 'int':
                value = int(self.entry.get()) + self.step_size
            self.entry.configure(state="normal")
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
            self.entry.configure(state="disabled")
            self.app_encoder.set_code_len(code_len=value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) - self.step_size
            if self.type_val == 'int':
                value = int(self.entry.get()) - self.step_size
            if value > 0:
                self.entry.configure(state="normal")
                self.entry.delete(0, "end")
                self.entry.insert(0, value)
                self.entry.configure(state="disabled")
                self.app_encoder.set_code_len(code_len=value)
        except ValueError:
            return

    def get(self) -> [float, int, None]:
        try:
            if self.type_val == 'int':
                return int(self.entry.get())
            return float(self.entry.get())
        except ValueError:
            return None

    def set(self, value: [float, int]):
        self.entry.configure(state="normal")
        self.entry.delete(0, "end")
        self.entry.insert(0, str(float(value)))
        if self.type_val == 'int':
            self.entry.insert(0, str(int(value)))
        self.entry.configure(state="disabled")
        self.app_encoder.set_code_len(code_len=value)


class App(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.win_width, self.win_height = self.winfo_screenwidth(), self.winfo_screenheight()

        self.title("Encoder")
        self.iconbitmap(r"data\cipher.ico")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.resizable(width=False, height=False)
        self.set_geometry()
        self.encoder = Encoder(num_sys=28)
        self.add_settings()

    def set_geometry(self, app_width: int = 500, app_height: int = 320) -> None:
        offset_width, offset_height = self.win_width // 2 - app_width // 2, self.win_height // 2 - app_height // 2
        self.geometry(f"{app_width}x{app_height}+{offset_width}+{offset_height}")
        self.update()

    def add_settings(self):
        for r in range(3):
            self.rowconfigure(index=r, weight=1)
        self.rowconfigure(index=3, weight=0)
        self.rowconfigure(index=4, weight=4)
        for c in range(5):
            if c == 2:
                self.columnconfigure(index=c, weight=1)
            self.columnconfigure(index=c, weight=4)

        self.lbl_num_sys = ctk.CTkLabel(master=self, text='Number system: 28', font=('Times', 15, 'bold'))
        self.lbl_num_sys.grid(row=0, column=0, columnspan=2, padx=10, pady=2, sticky='n')
        self.slider_var = ctk.IntVar(master=self, value=28)
        slider_num_sys = ctk.CTkSlider(master=self, orientation="horizontal", from_=20, to=35, number_of_steps=15,
                                       progress_color="green", width=120, height=20, command=self.slider_event,
                                       variable=self.slider_var,
                                       button_color='blue', button_hover_color='darkgreen', border_width=3)
        slider_num_sys.grid(row=1, column=0, columnspan=2, padx=10, pady=2, sticky='n')

        lbl_code_len = ctk.CTkLabel(master=self, text='Code character length', font=('Times', 15, 'bold'))
        lbl_code_len.grid(row=0, column=3, columnspan=2, padx=10, pady=2, sticky='n')
        self.spinbox_1 = FloatSpinbox(master=self, width=130, height=30, step_size=1, type_val='int',
                                      app_encoder=self.encoder)
        self.spinbox_1.grid(row=1, column=3, columnspan=2, padx=10, sticky='n')

        lbl_ignore_spaces = ctk.CTkLabel(master=self, text='Ignore spaces', font=('Times', 15, 'bold'))
        lbl_ignore_spaces.grid(row=2, column=0, padx=10, pady=2, sticky='n')
        self.switch_var_i_s = ctk.BooleanVar(value=False)
        switch_ignore_spaces = ctk.CTkSwitch(master=self, text="", command=self.switch_event_space,
                                             variable=self.switch_var_i_s, onvalue=True, offvalue=False)
        switch_ignore_spaces.grid(row=2, column=1, padx=10, pady=2, sticky='nw')

        lbl_reverse_encoding = ctk.CTkLabel(master=self, text='Reverse encoding', font=('Times', 14, 'bold'))
        lbl_reverse_encoding.grid(row=2, column=3, padx=10, pady=(5, 0), sticky='n')
        self.switch_var_r_e = ctk.BooleanVar(value=False)
        switch_reverse_encoding = ctk.CTkSwitch(master=self, text="", command=self.switch_event_reverse,
                                                variable=self.switch_var_r_e, onvalue=True, offvalue=False)
        switch_reverse_encoding.grid(row=2, column=4, padx=10, pady=(5, 0), sticky='nw')

        self.lbl_text = ctk.CTkLabel(master=self, text='Text', font=('Times', 12, 'italic'))
        self.lbl_text.grid(row=3, column=0, columnspan=2, padx=20, sticky='nw')

        self.entry_text = ctk.CTkTextbox(self, font=('Times', 14), border_width=1, wrap='word')
        self.entry_text.grid(row=4, column=0, columnspan=2, padx=10, sticky='nsew')
        self.entry_text.bind("<Key>", lambda e: Edit_Was_Made(e, self.entry_text, self.entry_code, self.encoder))

        btn_switch = ctk.CTkButton(self, text="<->", width=25, font=('Times', 11, 'italic'), fg_color='gray')
        btn_switch.grid(row=4, column=2, sticky='n')

        self.lbl_code = ctk.CTkLabel(master=self, text='Code', font=('Times', 12, 'italic'))
        self.lbl_code.grid(row=3, column=3, columnspan=2, padx=20, sticky='nw')

        self.entry_code = ctk.CTkTextbox(self, font=('Times', 14), border_width=1, wrap='word', state='disabled')
        self.entry_code.grid(row=4, column=3, columnspan=2, padx=10, pady=2, sticky='nsew')

    def slider_event(self, val: float):
        self.lbl_num_sys.configure(text=f"Number system: {self.slider_var.get()}")
        self.encoder.set_num_sys(num_sys=self.slider_var.get())

    def switch_event_space(self):
        self.encoder.set_ignore_spaces(ignore_spaces=self.switch_var_i_s.get())

    def switch_event_reverse(self):
        self.encoder.set_reverse_encoding(reverse_encoding=self.switch_var_r_e.get())

    def clear_window(self) -> None:
        try:
            for widget in self.winfo_children():
                widget.destroy()
            self.update()
        except Exception as ex:
            msg_error = f"{type(ex).__name__} -> {ex} -> clear_window()"
            CTkMessagebox(title="Error", message=msg_error, icon="cancel")

    def on_closing(self) -> None:
        msg = CTkMessagebox(title="Exit?", message="Do you want to close the program?",
                            icon="question", option_1="Yes", option_2="No")
        response = msg.get()
        if response == "Yes":
            try:
                self.destroy()
            except Exception as ex:
                msg_error = f"{type(ex).__name__} -> {ex} -> on_closing()"
                CTkMessagebox(title="Error", message=msg_error, icon="cancel")
            finally:
                exit()

    def display(self) -> None:
        self.update()
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.display()
