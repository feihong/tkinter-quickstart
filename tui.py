import sys
from pathlib import Path
import functools
import tempfile
import threading
import importlib
import tkinter
import watchfiles

root = None
geometry_file = Path(tempfile.gettempdir()) / 'tui_geometry'

def run(main):
    global root
    root = tkinter.Tk()

    if geometry_file.exists():
        root.geometry(geometry_file.read_text())

    root.protocol('WM_DELETE_WINDOW', on_exit)

    def on_key(evt):
        if evt.keysym == 'Escape':
            on_exit()

    root.bind('<KeyRelease>', on_key)

    main(root)
    root.after_idle(root.focus_force)
    root.mainloop()

def on_exit():
    geometry_file.write_text(root.geometry())
    root.quit()

def watch_file(py_file, module):
    for _changes in watchfiles.watch(py_file):
        root.after_idle(reload, module)

def reload(module):
    for widget in root.winfo_children():
        widget.destroy()
    importlib.reload(module)
    module.main(root)

if __name__ == '__main__':
    py_file = Path(sys.argv[1])
    module = importlib.import_module(py_file.stem)

    watch_thread = threading.Thread(target=watch_file, args=(py_file, module))
    watch_thread.daemon = True
    watch_thread.start()

    run(module.main)
