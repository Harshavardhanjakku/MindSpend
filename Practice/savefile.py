import tkinter as tk
from tkinter import filedialog
import shutil

window= tk.Tk()
def SaveFile():
    filepath = filedialog.asksaveasfilename(
        defaultextension='.json',
        filetypes=[("JSON file", "*.json"), ("All files", "*.*")]
    )
    if filepath:
        shutil.copy("myexpenses.json", filepath)
downloadbutton=tk.Button(text="save",command=SaveFile)
downloadbutton.pack()

window.mainloop()