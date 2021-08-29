import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

 = ["", "", ""]
data_source_current = 0

def get_figure():
    file_path = askopenfilename()
    data_source[data_source_current] = pd.read_csv(file_path).pivot('group', 'place', 'count')
    fig = plt.Figure(figsize=(5,5), dpi=100)
    graph = fig.add_subplot(111)
    graph.plot(data_source[data_source_current], kind='line')
    

window = tk.Tk()
window.title("Data Viewer")

get_figure_button = ttk.Button(window, text="Select Data Source", command=get_figure)
get_figure_button.pack()



window.mainloop()