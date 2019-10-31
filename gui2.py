import logging as log
log.basicConfig(level=log.DEBUG)
from gui1 import Form

class Form2(Form):
    def button_command(self):
        log.debug('button pressed')
        with open('form.txt', 'a') as f:
            for title, entry in self.entries.items():
                f.write('{} {}'.format(title, entry.get()))

    def add_button(self, title):
        button = tk.Button(text=title, command=self.button_command)
        button.grid(row=self.rows+1, columns=1, columnspan=2)

if __name__=='__main__':
    form = Form2()
    form.setup('host', 'user', 'db')
    form.add_button('Write')
    form.mainloop()
    log.debug(open('form.text').read())
