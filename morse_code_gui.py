from tkinter import *
from morse_functions import MorseFunctions

root = Tk()

available_text = 'abcdefghijklmnopqrstuvwyxz1234567890&\'@():,+!.-+"?/'
morse_list = [_ for _ in available_text]

class MorseGUI:
    def __init__(self):
        self.morse_functions = MorseFunctions()

    def run_program(self):
        root.title("Morse Code Encoder")
        self._entry_points()
        self._buttons()
        self._note_message()

    def _entry_points(self):
        self.entry_value = Entry(root, width=120, bd=4)
        self.results = Entry(root, state="disabled", width=120, bd=4)

        self.entry_value.grid(row=0, column=0, padx=10, pady=5, ipady=2)
        self.results.grid(row=1, column=0, padx=10, pady=10, ipady=5)

    def _buttons(self):
        self.encode_letter = Button(root, text="Encode/Decode", command=self.encode_or_decode, padx=20, pady=15)

        self.encode_letter.grid(row=2, column=0)

    def _note_message(self):
        self.note = Message(root, pady=5, text="Note: '#' will appear if the character cannot be translated.", width=200)

        self.note.grid(row=3, column=0)

    def encode_function(self):
        self.results.delete(0, END)
        result = self.entry_value.get()
        self.results.insert(0, self.morse_functions.encode_morse(result))

    def decode_function(self):
        result = self.entry_value.get()
        self.results.delete(0, END)
        self.results.insert(0, self.morse_functions.decode_morse(result))

    def encode_or_decode(self):
        x = self.entry_value.get()
        split_entry = [_ for _ in x]
        if "." in x and "-" in split_entry:
            self.results.config(state=NORMAL)
            self.decode_function()
            self.results.config(state="readonly")
        else:
            self.results.config(state=NORMAL)
            self.encode_function()
            self.results.config(state="readonly")

if __name__ == '__main__':
    run = MorseGUI()
    run.run_program()
    root.mainloop()
