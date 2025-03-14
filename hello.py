import random
import tkinter as tk

import tui

def hanzi():
    return chr(random.randint(0x4e00, 0x9fff))

def main(root):
    root.title('Hello World')

    tk.Label(root, text='你好世界！', font='Arial 48 bold').grid()

    def on_click():
        output.configure(text=''.join(hanzi() for _ in range(8)))

    btn = tk.Button(root, text='生成', command=on_click)
    btn.grid()

    output = tk.Label(root, text='', font='Arial 32')
    output.grid()

if __name__ == '__main__':
    tui.run(main)
