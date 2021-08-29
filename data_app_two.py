import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        
        self.frames = { }
        for page in (DataAppHome, DataSourceOne, DataSourceTwo, DataSourceThree):
            frame = page(container, self)
            self.frames = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(DataAppHome)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class DataAppHome(tk.Frame):
    def __init__(self, parent, controller):    
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home")
        label.pack()
        
        source_one_button = ttk.Button(self, text="Data Source One", command=lambda: controller.show_frame(DataSourceOne))
        source_one_button.pack()
        
        source_two_button = ttk.Button(self, text="Data Source Two", command=lambda: controller.show_frame(DataSourceTwo))
        source_two_button.pack()
        
        source_three_button = ttk.Button(self, text="Data Source Three", command=lambda: controller.show_frame(DataSourceThree))
        source_three_button.pack()

class DataSourceOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Data Source One")
        label.pack()
        
        get_file_button = ttk.Button(self, text="Select Data Source", command=get_file)
        get_file_button.pack()
        
        home_button = ttk.Button(self, text="Return to Home", command=lambda: controller.show_frame())
        home_button.pack()
        
class DataSourceTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Data Source One")
        label.pack()
        
        get_file_button = ttk.Button(self, text="Select Data Source", command=get_file)
        get_file_button.pack()
        
        home_button = ttk.Button(self, text="Return to Home", command=lambda: controller.show_frame())
        home_button.pack()
        
class DataSourceThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Data Source One")
        label.pack()
        
        get_file_button = ttk.Button(self, text="Select Data Source", command=get_file)
        get_file_button.pack()
        
        home_button = ttk.Button(self, text="Return to Home", command=lambda: controller.show_frame())
        home_button.pack()

def get_file():
            file_path = askopenfilename()
            data_source[data_source_current] = pd.read_csv(file_path).pivot('group', 'place', 'count')
            print(data_source[data_source_current])

DataApp.mainloop()