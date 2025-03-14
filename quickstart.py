import tkinter as tk
import tui

def main(root):
    root.title('Banana Interest Survery')

    tk.Label(
        root,
        text='Please take the survey',
        font=('Arial 16 bold'),
        background='brown',
        foreground='#ff0').grid(columnspan=2)

    tk.Label(root, text='What is your name?').grid(row=1, column=0)
    name_inp = tk.Entry(root)
    name_inp.grid(row=1, column=1)

    eater_inp = tk.Checkbutton(root, text='Check this box if you eat bananas')
    eater_inp.grid(columnspan=2, sticky='we')

    tk.Label(root, text='How many bananas do you eat per day?').grid(row=3, sticky='w')
    num_inp = tk.Spinbox(root, from_=0, to=1000, increment=1)
    num_inp.grid(row=3, column=1, sticky='we')

    tk.Label(root, text='What is the best color for a banana?').grid(columnspan=2, sticky='w', pady=10)
    color_inp = tk.Listbox(root, height=1)
    color_inp.insert(tk.END, 'Any', 'Green', 'Green-Yellow', 'Yellow', 'Brown Spotted', 'Black')
    color_inp.grid(columnspan=2, sticky='we', padx=25)

    tk.Label(root, text='Do you eat plantains?').grid(stick='w')
    plantain_frame = tk.Frame(root)
    plantain_frame.grid(columnspan=2, sticky='w')
    plantain_yes_inp = tk.Radiobutton(plantain_frame, text='Yes')
    plantain_yes_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
    plantain_no_inp = tk.Radiobutton(plantain_frame, text='Ewww, no!')
    plantain_no_inp.pack(side='right', fill='x', ipadx=10, ipady=5)

    tk.Label(root, text='Write a haiku about bananas').grid(sticky='w')
    banana_haiku_inp = tk.Text(root, height=3).grid(columnspan=2, sticky='nsew')

    submit_btn = tk.Button(root, text='Submit survey')
    submit_btn.grid(row=99)

    output_line = tk.Label(root, text='', anchor='w', justify='left')
    output_line.grid(columnspan=2, sticky='nsew')


if __name__ == '__main__':
    tui.run(main)
