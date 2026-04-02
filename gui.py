import tkinter as tk
from tkinter import ttk
from proxy import *

root = tk.Tk()
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tabControl.pack(expand = 1, fill ="both")

def ela(event):
    lbl_ela_msg["text"] = ""
    in_image = ent_ela_in.get()
    try:
        quality = int(ent_ela_q.get())
        if quality < 0 or quality > 100:
            lbl_ela_msg["text"] ="Quality must be an integer between 0 and 100!"
        else: 
            lbl_ela_msg["text"] ="Success!"
    except:
        lbl_ela_msg["text"] ="Quality must be an integer!"
    finally:
        ent_ela_in.delete(0, tk.END)
        ent_ela_q.delete(0, tk.END)
        proxy_ela(ent_ela_in.get(), ent_ela_q.get())
    
    

tabControl.add(tab1, text ='Welcome page')
#TODO: add text explanations for all used algorithms


tabControl.add(tab2, text ='Detect image manipulation')
tk.Label(tab2, text ="Error Level Analysis").grid(column = 0, row = 0, sticky="w")
tk.Label(tab2, text="Input image", width=50).grid(row=1, column=0, sticky="w")
tk.Label(tab2, text="Desired quality", width=50).grid(row=2, column=0, sticky="w")
ent_ela_in = tk.Entry(tab2, width=100)
ent_ela_in.grid(row=1, column=1, sticky="w")
ent_ela_q = tk.Entry(tab2, width=5)
ent_ela_q.grid(row=2, column=1, sticky="w")
btn_ela = tk.Button(tab2, text='Start')
btn_ela.bind('<Button>', ela)
btn_ela.grid(row=3, column=1, sticky="w")
lbl_ela_msg = tk.Label(tab2, text="")
lbl_ela_msg.grid(row=4, column=1)



tabControl.add(tab3, text ='Restore images')

# Widgets are added here

root.mainloop()