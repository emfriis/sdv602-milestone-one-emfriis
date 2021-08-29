import matplotlib
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
matplotlib.use('TkAgg')

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    plt.close('all')

def main():
    '''
    
    '''
    data_source = [pd.DataFrame(), pd.DataFrame(), pd.DataFrame()]
    data_source_current = 0
    sg.theme('Dark Blue 3')
    layout = [
        [ # --- gui row one
            sg.Button('Select Data Source')
        ], [ # --- gui row two
            sg.Canvas(key='-CANVAS-')
        ], [ # --- gui row three
            sg.Text('Summary Information')
        ], [ # --- gui row four
            sg.Text('Chat Placeholder')
        ], [ # --- gui row five
            sg.Button('Data Source One'),
            sg.Button('Data Source Two'), 
            sg.Button('Data Source Three')
        ]
    ]
    window = sg.Window("Data View", layout)
    figure_agg = None
    
    while True:
        event, value = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'Select Data Source':
            #fig = plt.clf()
            file_path = sg.PopupGetFile('Please select a data source')
            if file_path:
                if figure_agg:
                    delete_figure_agg(figure_agg)
                data_source[data_source_current] = pd.read_csv(file_path).pivot('place', 'group', 'count')
                data_plot = data_source[data_source_current].plot(kind='line')
                fig = plt.gcf()
                figure_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
                print(data_source[data_source_current])
        if event == 'Data Source One':
            #fig = plt.clf()
            if figure_agg:
                delete_figure_agg(figure_agg)
            data_source_current = 0
            if not data_source[0].empty:
                data_source[0] = pd.read_csv(file_path).pivot('place', 'group', 'count')
                data_plot = data_source[0].plot(kind='line')
                fig = plt.gcf()
                figure_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
                print(data_source[data_source_current])
        if event == 'Data Source Two':
            #fig = plt.clf()
            if figure_agg:
                delete_figure_agg(figure_agg)
            data_source_current = 1
            if not data_source[1].empty:
                data_source[1] = pd.read_csv(file_path).pivot('place', 'group', 'count')
                data_plot = data_source[1].plot(kind='line')
                fig = plt.gcf()
                figure_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
                print(data_source[data_source_current])
        if event == 'Data Source Three':
            #fig = plt.clf()
            if figure_agg:
                delete_figure_agg(figure_agg)
            data_source_current = 2
            if not data_source[2].empty:
                data_source[2] = pd.read_csv(file_path).pivot('place', 'group', 'count')
                data_plot = data_source[2].plot(kind='line')
                fig = plt.gcf()
                figure_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
                print(data_source[data_source_current])

if __name__ == "__main__":
    main()