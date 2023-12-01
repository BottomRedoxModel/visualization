import os
from tkinter.filedialog import askopenfilename

def get_fname():
    fname = askopenfilename(
        initialdir=os.getcwd(),
        filetypes=(("netcdf file", "*.nc"), ("All Files", "*.*")),
        title="Choose a needed file.")
    return fname