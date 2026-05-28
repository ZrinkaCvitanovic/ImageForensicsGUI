# ImageForensicsGUI
This tool was created as a result of research I have done for my final thesis at 
[Faculty of Electrical Engineering and Computing](https://www.fer.unizg.hr/en), University of Zagreb. The thesis title is "Forenzički alat za prepoznavanje i uklanjanje izmjena na digitalnim slikama" (Croatian for "Forensic tool for detection of tampering and restoring tampered digital images"). The thesis is not yet public.

The tool has three main components:
1. detecting image manipulation
    - Error Level Analysis (ELA)
    - changing color scheme to HSV and luminence gradient
    - Edge detection using Canny edge detector
2. restoring images
    - Telea inpainting
    - PatchMatch
    - image enhancement: removing noise, increasing contrast, sharpening and resizing
3. comparing results
    - the graphic interface allows uploading up to 4 images and extracts all relevant data from images (used algorithm and parameters)

The tools can be used both thorugh graphic interface or using command line. The user interface has suggestions for parameter values which are shown when hovering over the entry field. 

DISCLAIMER: I **do not** take credit for writing implementations of the used algorithms. Most of the them were built on other implentations whose authors are referenced at the beginning of each file. However, most of them had to be updated for later version of Python.

## Setup and install
This project was written in Python and the version used is 3.12. Therefore, it is recommended to use the same version in yor setup. Current version is supported only by Linux.

Before starting, it is a good idea to create a virtual environmemt to prevent dependency crashes. For furhter instrucions, check the steps in **Virtual environment setup** section.  

After activating the virtual environment, stay in the root of your project.
If using the tool for the first time, simply install all necessary dependencies with command:  

    pip3 install -r requirements.txt

Now, if you wish to use the graphical interface, start it by executing command:  

    python3 gui.py

Otherwise, navigate to the desired folder and use the tool from command line. 

## Virtual environment setup:
Navigate to root of the project.

Create venv (only the first time):

    pip3 -m venv [name of the venv directory]

Typically, the folder is called `.venv`. The folder must not exist before you execute the command.

Whenever you use the tool, you need to activate the virtual environment. Start from root of your project and enter in command line:

    source [venv directory]/bin/activate

When finished, deactivate the virtual environment. Navigate to root of you project and enter in command line:

    deactivate

If you wish to delete the virtual environment, simply delete the folder where you created it. Ensure you have deactivated the virtual environment  before this action:

    rm -r [venv directory]
