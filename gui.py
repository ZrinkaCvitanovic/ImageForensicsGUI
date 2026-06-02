import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import subprocess
import tools
from functools import partial

from PIL import Image, ImageTk

root = tk.Tk()
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tabControl.pack(expand = 1, fill ="both")

global num_of_images_uploaded

def browse_file(entry_widget):
    """Generic file browser that inserts selected path into the provided entry widget"""
    filename = filedialog.askopenfilename(
        initialdir="/home",
        title="Select a File",
        filetypes=(
            ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff"),
            ("Text files", "*.txt"),
            ("all files", "*.*")
        )
    )
    if filename:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, filename)

def event_ela(event):
    in_image = ent_ela_in.get()
    try:
        quality = int(ent_ela_q.get())
        if quality < 0 or quality > 100:
            lbl_ela_msg["text"] ="Quality value must be an integer between 0 and 100!"
        else: 
            lbl_ela_msg["text"] ="Success!"
            subprocess.run(['python3', 'detection/ela/main.py', in_image, str(quality)])
            ent_ela_in.delete(0, tk.END)
            ent_ela_q.delete(0, tk.END)
    except ValueError:
        lbl_ela_msg["text"] ="Quality value must be an integer!"

def event_color(event):
    in_image = ent_color_in.get()
    method = opt_color_method.get()
    if method != "lum" and method != "hsv":
        lbl_color_msg["text"] ="Unsupported choice of method. Choose 'lum' or 'hsv!"
    else: 
        lbl_color_msg["text"] ="Success!"
        subprocess.run(['python3', 'detection/change-color-scheme/main.py', in_image, method])
        ent_color_in.delete(0, tk.END)

def event_edge(event):
    in_image = ent_edge_in.get()
    try:
        lower = int(ent_edge_lower.get())
        higher = int(ent_edge_higher.get())
        subprocess.run(['python3', 'detection/edges/main.py', in_image, str(lower), str(higher)])
        lbl_edge_msg["text"] ="Success!"
        ent_edge_in.delete(0, tk.END)
        ent_edge_lower.delete(0, tk.END)
        ent_edge_higher.delete(0, tk.END)
    except ValueError:
        lbl_edge_msg["text"] ="Lower and higher threshold values must be numbers!"
        

def event_telea(event):
    in_image = ent_telea_in.get()
    mask_image = ent_telea_mask.get()
    radius = ent_telea_radius.get()
    try:
        radius_int = int(radius)
        lbl_telea_msg["text"] ="Success!"
        subprocess.run(['python3', 'restoration/telea/main.py', '-r', radius, in_image, mask_image])
        ent_telea_in.delete(0, tk.END)
        ent_telea_mask.delete(0, tk.END)
        ent_telea_radius.delete(0, tk.END)
    except:
        lbl_telea_msg["text"] ="Radius value must be a number!"
    


def event_patch(event):
    in_image = ent_patch_in.get()
    mask_image = ent_patch_mask.get()
    color = opt_patch_maskc.get()
    if color != "white" and color != "black" and color != "blue" and color != "green" and color != "red":
        lbl_patch_msg["text"] = "Supported choices are white, black, blue, green or red."
    else:
        lbl_patch_msg["text"] ="Success!"
        subprocess.run(['python3', 'restoration/PatchMatch/main.py', in_image, mask_image, color])
        ent_patch_in.delete(0, tk.END)
        ent_patch_mask.delete(0, tk.END)

def event_resize(event):
    in_image = ent_resize_in.get()
    height_scale = ent_resize_height.get()
    width_scale = ent_resize_width.get()
    method = opt_resize_method.get()

    try:
        height = int(height_scale)
        width = int(width_scale)
        if method != "cubic" and method != "lanzos" and method != "linear":
            lbl_resize_msg["text"] = "Supported choices are cubic, lanzos and linear."
        else:
            lbl_resize_msg["text"] ="Success!"
            subprocess.run(['python3', 'restoration/enhancement/resize/resize.py', in_image, height_scale, width_scale, method])
            ent_resize_in.delete(0, tk.END)
            ent_resize_height.delete(0, tk.END)
            ent_resize_width.delete(0, tk.END)
    except:
        lbl_resize_msg["text"] = "Height and width scale values must be integers!"

def event_noise(event):
    in_image = ent_noise_in.get()
    method = opt_noise_method.get()
    if method != "gaussian" and method != "median":
        lbl_noise_msg["text"] = "Supported choices are gaussian and median"
    else:
        lbl_noise_msg["text"] ="Success!"
        subprocess.run(['python3', 'restoration/enhancement/noise/denoising.py', in_image, method])
        ent_noise_in.delete(0, tk.END)

def event_sharp(event):
    in_image = ent_sharp_in.get()
    method = opt_sharp_method.get()
    if method != "kernel" and method != "laplacian":
        lbl_sharp_msg["text"] = "Supported choices are kernel or laplacian"
    else:
        subprocess.run(['python3', 'restoration/enhancement/sharpen/sharpen.py', in_image, method])            
        lbl_sharp_msg["text"] ="Success!"
        ent_sharp_in.delete(0, tk.END)

def event_contrast(event):
    in_image = ent_contrast_in.get()
    subprocess.run(['python3', 'restoration/enhancement/sharpen/histogram.py', in_image])          
    lbl_contrast_msg["text"] ="Success!"
    ent_contrast_in.delete(0, tk.END)

 
def imageUploader():
    global num_of_images_uploaded
    fileTypes = [("All files", "*.*")]
    file_list = tk.filedialog.askopenfilenames(filetypes=fileTypes)
    file_list = list(file_list)
    labels_img = [upload_lbl_1, upload_lbl_2, upload_lbl_3, upload_lbl_4]
    labels_mtdt = [upload_mtdt_1, upload_mtdt_2, upload_mtdt_3, upload_mtdt_4]

    for path in file_list:
        if path:
            img = Image.open(path)
            img = img.resize((750, 750))
            pic = ImageTk.PhotoImage(img)
            labels_img[num_of_images_uploaded].config(image=pic)
            labels_img[num_of_images_uploaded].image = pic
            metadata = tools.parseParameters(path.split("/")[-1])
            metadata_string = ""
            for key in metadata.keys():
                    metadata_string += f"{key}: {metadata.get(key)}  \n"
            labels_mtdt[num_of_images_uploaded]["text"] = metadata_string
            num_of_images_uploaded = (num_of_images_uploaded + 1) % 4

def removeImage(event):
    global num_of_images_uploaded
    num_of_images_uploaded -= 1

def displayHelp(method):
    match method:
        case "ELA":
            if len(lbl_ela_help["text"]) == 0:
                lbl_ela_help["text"] = "Recommended values for quality are between 40 and 80.\nFor high resolution images, choose lower values and vice versa." 
            else:
                lbl_ela_help["text"] = ""
        case "color":
            print(lbl_color_help["text"])
            if len(lbl_color_help["text"]) == 0:
                lbl_color_help["text"] = "Always use both methods because each can cause false positives."
            else:
                lbl_color_help["text"] = ""
        case "edges":
            if len(lbl_edge_help["text"]) == 0:
                lbl_edge_help["text"] = """
                Recommended values for lower threshold are between 40 and 100 for natural images.\nFor darker pictures, the threshold can be higher.\n
                Higher threshold should be about twice as large as the lower. \nIf many edges are undetected, lower it, but always make it larger than the lower threshold."""
            else:
                lbl_edge_help["text"] = ""
        case "telea":
            if len(lbl_telea_help["text"]) == 0:
                lbl_telea_help["text"] = "Default value for radius is 5. For less narrow masks, choose a smaller radius."
            else:
                lbl_telea_help["text"] = ""
        case "resize":
            if len(lbl_resize_help["text"]) == 0:
                lbl_resize_help["text"] = """
            Linear interpolation - fastest, works fine for pictures without too much details
            Lanzos - smoother, but for a large amount of images can be slow.
            Cubic - a compromise between the two
            """
            else:
                lbl_resize_help["text"] = ""
        case "noise":
            if len(lbl_noise_help["text"]) == 0:
                lbl_noise_help["text"] = "Use 'gaussian' for Gaussian noise and 'median' for random or 'salt and pepper' noise."

            else:
                lbl_noise_help["text"] = ""
        case "sharp":
             if len(lbl_sharp_msg["text"]) == 0:
                lbl_sharp_msg["text"] = "Use 'kernel' for detailed images and 'laplacian' for noisy images."
             else:
                 lbl_sharp_msg["text"] = ""



tabControl.add(tab1, text ='Detect image manipulation')

lbl_ela_title = tk.Label(tab1, text ="Error Level Analysis")
lbl_ela_title.config(font=("TkDefaultFont", 10, "bold"))
lbl_ela_title.grid( row=0, column=0, sticky="w")
tk.Label(tab1, text="Input image", width=50).grid(row=1, column=0, sticky="w")
tk.Button(tab1, text="Browse Files",command=partial(browse_file, None)).grid(row=1, column=2, sticky="w")
tk.Label(tab1, text="Desired quality", width=50).grid(row=2, column=0, sticky="w")
ent_ela_in = tk.Entry(tab1, width=100)
ent_ela_in.grid(row=1, column=1, sticky="w")
tk.Button(tab1, text="Browse Files",command=partial(browse_file, ent_ela_in)).grid(row=1, column=2, sticky="w")
ent_ela_q = tk.Entry(tab1, width=5)
ent_ela_q.grid(row=2, column=1, sticky="w")
btn_ela_help = tk.Button(tab1, text="Help", command=lambda: displayHelp("ELA")).grid(row=1, column=3, sticky="w")
lbl_ela_help = tk.Label(tab1, text="")
lbl_ela_help.grid(row=5, column=1)
btn_ela = tk.Button(tab1, text='Start')
btn_ela.bind('<Button>', event_ela)
btn_ela.grid(row=3, column=1, sticky="w")
lbl_ela_msg = tk.Label(tab1, text="")
lbl_ela_msg.grid(row=4, column=1)

lbl_color_title = tk.Label(tab1, text ="Change Color Scheme")
lbl_color_title.config(font=("TkDefaultFont", 10, "bold"))
lbl_color_title.grid(row=10, column=0, sticky="w")
tk.Label(tab1, text="Input image", width=50).grid(row=11, column=0, sticky="w")
tk.Label(tab1, text="Desired method", width=50).grid(row=12, column=0, sticky="w")
ent_color_in = tk.Entry(tab1, width=100)
ent_color_in.grid(row=11, column=1, sticky="w")
tk.Button(tab1, text="Browse Files",command=partial(browse_file, ent_color_in)).grid(row=11, column=2, sticky="w")
opt_color_method = tk.StringVar(value="hsv")
opt_color_dropdown = tk.OptionMenu(tab1, opt_color_method, "hsv", "lum")
opt_color_dropdown.grid(row=12, column=1, sticky="w")
btn_color = tk.Button(tab1, text='Start')
btn_color.bind('<Button>', event_color)
btn_color.grid(row=13, column=1, sticky="w")
lbl_color_msg = tk.Label(tab1, text="")
lbl_color_msg.grid(row=14, column=1)
btn_color_help = tk.Button(tab1, text="Help", command=lambda: displayHelp("color")).grid(row=11, column=3, sticky="w")
lbl_color_help = tk.Label(tab1, text="")
lbl_color_help.grid(row=15, column=1)

lbl_edge_title = tk.Label(tab1, text ="Edge detection")
lbl_edge_title.config(font=("TkDefaultFont", 10, "bold"))
lbl_edge_title.grid(column=0, row=20, sticky="w")
tk.Label(tab1, text="Input image", width=50).grid(row=21, column=0, sticky="w")
tk.Label(tab1, text="Lower threshold", width=50).grid(row=22, column=0, sticky="w")
tk.Label(tab1, text="Higher threshold", width=50).grid(row=23, column=0, sticky="w")
ent_edge_in = tk.Entry(tab1, width=100)
ent_edge_in.grid(row=21, column=1, sticky="w")
tk.Button(tab1, text="Browse Files",command=partial(browse_file, ent_edge_in)).grid(row=21, column=2, sticky="w")
ent_edge_lower = tk.Entry(tab1, width=5)
ent_edge_lower.grid(row=22, column=1, sticky="w")
btn_edge_help = tk.Button(tab1, text="Help", command=lambda: displayHelp("edges")).grid(row=21, column=3, sticky="w")
lbl_edge_help = tk.Label(tab1, text="")
lbl_edge_help.grid(row=28, column=1)
ent_edge_higher = tk.Entry(tab1, width=5)
ent_edge_higher.grid(row=23, column=1, sticky="w")
btn_edge = tk.Button(tab1, text='Start')
btn_edge.bind('<Button>', event_edge)
btn_edge.grid(row=26, column=1, sticky="w")
lbl_edge_msg = tk.Label(tab1, text="")
lbl_edge_msg.grid(row=27, column=1)


tabControl.add(tab2, text ='Restore images')

lbl_telea_title = tk.Label(tab2, text ="Telea inpainting")
lbl_telea_title.config(font=("TkDefaultFont", 10, "bold"))
lbl_telea_title.grid(row=0, column=0, sticky="w")
tk.Label(tab2, text="Input image", width=50).grid(row=1, column=0, sticky="w")
tk.Label(tab2, text="Mask image", width=50).grid(row=2, column=0, sticky="w")
tk.Label(tab2, text="Neighbourhood radius", width=50).grid(row=3, column=0, sticky="w")
ent_telea_in = tk.Entry(tab2, width=100)
ent_telea_in.grid(row=1, column=1, sticky="w")
tk.Button(tab2, text="Browse Files",command=partial(browse_file, ent_telea_in)).grid(row=1, column=2, sticky="w")
ent_telea_mask = tk.Entry(tab2, width=100)
ent_telea_mask.grid(row=2, column=1, sticky="w")
tk.Button(tab2, text="Browse Files",command=partial(browse_file, ent_telea_mask)).grid(row=2, column=2, sticky="w")
ent_telea_radius = tk.Entry(tab2, width=5)
ent_telea_radius.grid(row=3, column=1, sticky="w")
ent_telea_radius.insert(0, 5)
btn_telea_help = tk.Button(tab2, text="Help", command=lambda: displayHelp("telea")).grid(row=1, column=3, sticky="w")
lbl_telea_help = tk.Label(tab2, text="")
lbl_telea_help.grid(row=6, column=1)
btn_telea = tk.Button(tab2, text='Start')
btn_telea.bind('<Button>', event_telea)
btn_telea.grid(row=4, column=1, sticky="w")
lbl_telea_msg = tk.Label(tab2, text="")
lbl_telea_msg.grid(row=5, column=1)

lbl_patch_title = tk.Label(tab2, text ="PatchMatch inpainting")
lbl_patch_title.config(font=("TkDefaultFont", 10, "bold"))
lbl_patch_title.grid(row=7, column=0, sticky="w")
tk.Label(tab2, text="Input image", width=50).grid(row=8, column=0, sticky="w")
tk.Label(tab2, text="Mask image", width=50).grid(row=9, column=0, sticky="w")
tk.Label(tab2, text="Mask color", width=50).grid(row=10, column=0, sticky="w")
ent_patch_in = tk.Entry(tab2, width=100)
ent_patch_in.grid(row=8, column=1, sticky="w")
tk.Button(tab2, text="Browse Files",command=partial(browse_file, ent_patch_in)).grid(row=9, column=2, sticky="w")
ent_patch_mask = tk.Entry(tab2, width=100)
ent_patch_mask.grid(row=9, column=1, sticky="w")
tk.Button(tab2, text="Browse Files",command=partial(browse_file, ent_patch_mask)).grid(row=9, column=2, sticky="w")
opt_patch_maskc = tk.StringVar(value="white")
opt_patch_dropdown = tk.OptionMenu(tab2, opt_patch_maskc, "white", "black", "red", "green", "blue")
opt_patch_dropdown.grid(row=10, column=1, sticky="w")
btn_patch = tk.Button(tab2, text='Start')
btn_patch.bind('<Button>', event_patch)
btn_patch.grid(row=11, column=1, sticky="w")
lbl_patch_msg = tk.Label(tab2, text="")
lbl_patch_msg.grid(row=12, column=1)

lbl_resize_title = tk.Label(tab2, text ="Image resizing")
lbl_resize_title.config(font=("TkDefaultFont", 10, "bold"))
lbl_resize_title.grid(row=13, column=0, sticky="w")
tk.Label(tab2, text="Input image", width=50).grid(row=14, column=0, sticky="w")
tk.Label(tab2, text="Height scale", width=50).grid(row=15, column=0, sticky="w")
tk.Label(tab2, text="Width scale", width=50).grid(row=16, column=0, sticky="w")
tk.Label(tab2, text="Method", width=50).grid(row=17, column=0, sticky="w")
ent_resize_in = tk.Entry(tab2, width=100)
ent_resize_in.grid(row=14, column=1, sticky="w")
tk.Button(tab2, text="Browse Files",command=partial(browse_file, ent_resize_in)).grid(row=14, column=2, sticky="w")
ent_resize_height = tk.Entry(tab2, width=5)
ent_resize_height.grid(row=15, column=1, sticky="w")
ent_resize_width = tk.Entry(tab2, width=5)
ent_resize_width.grid(row=16, column=1, sticky="w")
btn_resize_help = tk.Button(tab2, text="Help", command=lambda: displayHelp("resize")).grid(row=14, column=3, sticky="w")
lbl_resize_help = tk.Label(tab2, text="")
lbl_resize_help.grid(row=20, column=1)
opt_resize_method = tk.StringVar(value="cubic")
opt_resize_dropdown = tk.OptionMenu(tab2, opt_resize_method, "cubic", "lanzos", "linear")
opt_resize_dropdown.grid(row=17, column=1, sticky="w")
btn_resize = tk.Button(tab2, text='Start')
btn_resize.bind('<Button>', event_resize)
btn_resize.grid(row=18, column=1, sticky="w")
lbl_resize_msg = tk.Label(tab2, text="")
lbl_resize_msg.grid(row=19, column=1)

lbl_noise_title = tk.Label(tab2, text ="Removing noise from images")
lbl_noise_title.config(font=("TkDefaultFont", 10, "bold"))
lbl_noise_title.grid(row=21, column=0, sticky="w")
tk.Label(tab2, text="Input image", width=50).grid(row=22, column=0, sticky="w")
tk.Label(tab2, text="Method", width=50).grid(row=23, column=0, sticky="w")
ent_noise_in = tk.Entry(tab2, width=100)
ent_noise_in.grid(row=22, column=1, sticky="w")
tk.Button(tab2, text="Browse Files",command=partial(browse_file, ent_noise_in)).grid(row=22, column=2, sticky="w")
opt_noise_method = tk.StringVar(value="gaussian")
opt_noise_dropdown = tk.OptionMenu(tab2, opt_noise_method, "gaussian", "median")
btn_noise_help = tk.Button(tab2, text="Help", command=lambda: displayHelp("noise")).grid(row=22, column=3, sticky="w")
lbl_noise_help = tk.Label(tab2, text="")
lbl_noise_help.grid(row=26, column=1)
opt_noise_dropdown.grid(row=23, column=1, sticky="w")
btn_noise = tk.Button(tab2, text='Start')
btn_noise.bind('<Button>', event_noise)
btn_noise.grid(row=24, column=1, sticky="w")
lbl_noise_msg = tk.Label(tab2, text="")
lbl_noise_msg.grid(row=25, column=1)

lbl_contrast_title = tk.Label(tab2, text ="Increasing contrast to images")
lbl_contrast_title.config(font=("TkDefaultFont", 10, "bold"))
lbl_contrast_title.grid(row=26, column=0, sticky="w")
tk.Label(tab2, text="Input image", width=50).grid(row=27, column=0, sticky="w")
ent_contrast_in = tk.Entry(tab2, width=100)
ent_contrast_in.grid(row=27, column=1, sticky="w")
tk.Button(tab2, text="Browse Files",command=partial(browse_file, ent_contrast_in)).grid(row=27, column=2, sticky="w")
btn_contrast = tk.Button(tab2, text='Start')
btn_contrast.bind('<Button>', event_contrast)
btn_contrast.grid(row=28, column=1, sticky="w")
lbl_contrast_msg = tk.Label(tab2, text="")
lbl_contrast_msg.grid(row=29, column=1)

lbl_sharp_title = tk.Label(tab2, text ="Sharpening images")
lbl_sharp_title.config(font=("TkDefaultFont", 10, "bold"))
lbl_sharp_title.grid(row=30, column=0, sticky="w")
tk.Label(tab2, text="Input image", width=50).grid(row=31, column=0, sticky="w")
tk.Label(tab2, text="Method", width=50).grid(row=32, column=0, sticky="w")
ent_sharp_in = tk.Entry(tab2, width=100)
ent_sharp_in.grid(row=31, column=1, sticky="w")
tk.Button(tab2, text="Browse Files",command=partial(browse_file, ent_sharp_in)).grid(row=31, column=2, sticky="w")
opt_sharp_method = tk.StringVar(value="kernel")
opt_sharp_dropdown = tk.OptionMenu(tab2, opt_sharp_method, "kernel", "laplacian")
opt_sharp_dropdown.grid(row=32, column=1, sticky="w")
btn_sharp_help = tk.Button(tab2, text="Help", command=lambda: displayHelp("sharp")).grid(row=31, column=3, sticky="w")
lbl_sharp_help = tk.Label(tab2, text="")
lbl_sharp_help.grid(row=35, column=1)
btn_sharp = tk.Button(tab2, text='Start')
btn_sharp.bind('<Button>', event_sharp)
btn_sharp.grid(row=33, column=1, sticky="w")
lbl_sharp_msg = tk.Label(tab2, text="")
lbl_sharp_msg.grid(row=34, column=1)

num_of_images_uploaded = 0
tabControl.add(tab3, text ='Compare results')
upload_lbl = tk.Label(tab3, text="Upload up to 4 images for result comparison          ")
upload_lbl.config(font=("TkDefaultFont", 10, "bold"))
upload_lbl.grid(row=0, column=0, sticky="w")
upload_button = tk.Button(tab3, text="Upload Files", command=imageUploader)
upload_button.grid(column=1, row=0, sticky="e")
upload_lbl_1 = tk.Label(tab3, text="")
upload_lbl_1.grid(column=0, row=1, sticky="w")
upload_mtdt_1 = tk.Label(tab3, text="")
upload_mtdt_1.grid(column=1, row=1)
upload_lbl_2 = tk.Label(tab3, text="")
upload_lbl_2.grid(column=2, row=1, sticky="w")
upload_mtdt_2 = tk.Label(tab3, text="")
upload_mtdt_2.grid(column=3, row=1)
tk.Label(tab3, text="").grid(row=2, column=0)
upload_lbl_3 = tk.Label(tab3, text="")
upload_lbl_3.grid(column=0, row=3, sticky="w")
upload_mtdt_3 = tk.Label(tab3, text="")
upload_mtdt_3.grid(column=1, row=3)
upload_lbl_4 = tk.Label(tab3, text="")
upload_lbl_4.grid(column=2, row=3, sticky="w")
upload_mtdt_4 = tk.Label(tab3, text="")
upload_mtdt_4.grid(column=3, row=3)



root.mainloop()