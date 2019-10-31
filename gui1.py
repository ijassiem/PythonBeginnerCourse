import tkinter as tk

class Form(tk.Frame):

    def __init__(self):
        super().__init__()
        self.entries = {}
        self.rows = 0

    def setup(self, *titles):
        for title in titles:
            self.add_row(title)

    def add_row(self, title):
        self.rows += 1
        i = self.rows
        label = tk.Label(text=title)
        label.grid(row=i, column=1)
        entry = tk.Entry()
        entry.grid(row=i, column=2)
        self.entries[title] = entry

    def button_command(self):
        for title, entry in self.entries.items():
            print(title, entry.get())

    def add_button(self, title):
        button = tk.Button(text=title, command=self.button_command)
        button.grid(row=self.rows+1, column=1, columnspan=2)

if __name__=='__main__':
    form = Form()
    form.setup('name','surname','age')
    form.add_button('print')
    form.mainloop()
    
#win = tk.Frame()

#entries = {}

#for i, title in enumerate('name surname age'.split()):
 #   label = tk.Label(text = title)
  #  label.grid(row=i, column=1)
   # entry = tk.Entry()
    #entry.grid(row=i, column=2)
    #entries[title] = entry

#def button_command():
 #   for title, entry in entries.items():
  #      print(title, entry.get())

#print_button = tk.Button(text='print', command=button_command)
#print_button.grid(row=i+1, column=1, columnspan=2)

#win.mainloop(0)
