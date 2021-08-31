import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

def draw_figure(canvas, figure):
    '''
    This function draws a matplotlib figure to a pysimplegui canvas.
    
    Args:
        canvas: the canvas to draw the figure to
        figure: the figure to draw
    
    Returns:
        figure_canvas_agg: a renderable matplotlib figure
    '''
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def delete_figure_agg(figure_agg):
    '''
    This function deletes the current renderable matplotlib figure as stored in a global variable.
    '''
    figure_agg.get_tk_widget().forget()
    plt.close('all')

def login():
    '''
    This function returns a pysimplegui layout to generate a placeholder login window.
    '''
    layout = [
        [
            sg.Text("Username")
        ], [
            sg.Input()
        ], [
            sg.Text("Password")
        ], [
            sg.Input()
        ], [
            sg.Button("Login"), sg.Button("Register")
        ]
    ]
    return sg.Window("Login", layout, finalize=True)

def registration():
    '''
    This function returns a pysimplegui layout to generate a placeholder registration window.
    '''
    layout = [
        [
            sg.Text("Email")
        ], [
            sg.Input()
        ], [
            sg.Text("Username")
        ], [
            sg.Input()
        ], [
            sg.Text("Password")
        ], [
            sg.Input()
        ], [
            sg.Button("Register")
        ]
    ]
    return sg.Window("Registration", layout, modal=True, finalize=True)

def home():
    '''
    This function returns a pysimplegui layout for a simple navigation home window
    '''
    layout = [
        [ # --- gui row one
            sg.Button('Data Source One'), 
            sg.Button('Data Source Two'), 
            sg.Button('Data Source Three')
        ]
    ]
    return sg.Window("Home", layout, finalize=True)

class DataSourceOne():
    '''
    This class is used to build the first data source window. 
    It contains an attribute "data_frame", used to remember the last selected data frame.
    It also contains a function that returns a layout for a data view window.
    '''
    data_frame = pd.DataFrame()
    
    def get_layout(self):
        '''
        This function returns a layout for a data view window.
        '''
        layout = [
            [ # --- gui row one
                sg.Button('Select Data Source')
            ], [ # --- gui row two
                sg.Text("", key="-TITLE-")
            ], [ # --- gui row three
                sg.Canvas(key='-CANVAS-')
            ], [ # --- gui row four
                sg.Text('Summary Information')
            ], [ # --- gui row five
                sg.Text('Chat Placeholder')
            ], [ # --- gui row six
                sg.Button('Data Source Two'), 
                sg.Button('Data Source Three')
            ]
        ]
        return layout

class DataSourceTwo():
    '''
    This class is used to build the second data source window. 
    It contains an attribute "data_frame", used to remember the last selected data frame.
    It also contains a function that returns a layout for a data view window.
    '''
    data_frame = pd.DataFrame()
    
    def get_layout(self):
        '''
        This function returns a layout for a data view window.
        '''
        layout = [
            [ # --- gui row one
                sg.Button('Select Data Source')
            ], [ # --- gui row two
                sg.Text("", key="-TITLE-")
            ], [ # --- gui row three
                sg.Canvas(key='-CANVAS-')
            ], [ # --- gui row four
                sg.Text('Summary Information')
            ], [ # --- gui row five
                sg.Text('Chat Placeholder')
            ], [ # --- gui row six
                sg.Button('Data Source One'), 
                sg.Button('Data Source Three')
            ]
        ]
        return layout

class DataSourceThree():
    '''
    This class is used to build the third data source window. 
    It contains an attribute "data_frame", used to remember the last selected data frame.
    It also contains a function that returns a layout for a data view window.
    '''
    data_frame = pd.DataFrame()
    
    def get_layout(self):
        '''
        This function returns a layout for a data view window.
        '''
        layout = [
            [ # --- gui row one
                sg.Button('Select Data Source')
            ], [ # --- gui row two
                sg.Text("", key="-TITLE-")
            ], [ # --- gui row three
                sg.Canvas(key='-CANVAS-')
            ], [ # --- gui row four
                sg.Text('Summary Information')
            ], [ # --- gui row five
                sg.Text('Chat Placeholder')
            ], [ # --- gui row six
                sg.Button('Data Source One'), 
                sg.Button('Data Source Two')
            ]
        ]
        return layout

window_login, window_register, window_home, window_one, window_two, window_three = login(), None, None, None, None, None
sg.theme('Dark Blue 3')
one = DataSourceOne()
two = DataSourceTwo()
three = DataSourceThree()
figure_agg = None

while True:
    window, event, values = sg.read_all_windows()
    if event == "Exit" or event == sg.WIN_CLOSED:
        if window == window_one:
            window_one = None
            window.close()
        if window == window_two:
            window_two = None
            window.close()
        if window == window_three:
            window_three = None
            window.close()
        if window == window_register:
            window_register = None
            window.close()
        if window == window_home or window == window_login:
            break   
    if event == "Login":
        window_login = None
        window.close()
        window_home = home()
    if event == "Register" and window != window_register:
        window_register = registration()
    if event == "Register" and window == window_register:
        window_register = None
        window.close()
    if event == 'Select Data Source':
        file_path = sg.PopupGetFile('Please select a data source')
        if file_path:
            if figure_agg:
                delete_figure_agg(figure_agg)
            if window_one:
                one.data_frame = pd.read_csv(file_path).pivot('place', 'group', 'count')
                data_plot = one.data_frame.plot(kind='line')
            elif window_two:
                two.data_frame = pd.read_csv(file_path).pivot('place', 'group', 'count')
                data_plot = two.data_frame.plot(kind='line')
            elif window_three:
                three.data_frame = pd.read_csv(file_path).pivot('place', 'group', 'count')
                data_plot = three.data_frame.plot(kind='line')
            fig = plt.gcf()
            figure_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
    if event == 'Data Source One' and not window_one:
        if window == window_two:
            window_two = None
            window.close()
        if window == window_three:
            window_three = None
            window.close()
        window_one = sg.Window("Data Source One", one.get_layout(), modal=True, finalize=True)
        if not one.data_frame.empty:
            if figure_agg:
                delete_figure_agg(figure_agg)
            data_plot = one.data_frame.plot(kind='line')
            fig = plt.gcf()
            figure_agg = draw_figure(window_one['-CANVAS-'].TKCanvas, fig)
    if event == 'Data Source Two' and not window_two:
        if window == window_one:
            window_one = None
            window.close()
        if window == window_three:
            window_three = None
            window.close()
        window_two = sg.Window("Data Source Two", two.get_layout(), modal=True, finalize=True)
        if not two.data_frame.empty:
            if figure_agg:
                delete_figure_agg(figure_agg)
            data_plot = two.data_frame.plot(kind='line')
            fig = plt.gcf()
            figure_agg = draw_figure(window_two['-CANVAS-'].TKCanvas, fig)
    if event == 'Data Source Three' and not window_three:
        if window == window_one:
            window_one = None
            window.close()
        if window == window_two:
            window_two = None
            window.close()
        window_three = sg.Window("Data Source Three", three.get_layout(), modal=True, finalize=True)
        if not one.data_frame.empty:
            if figure_agg:
                delete_figure_agg(figure_agg)
            data_plot = three.data_frame.plot(kind='line')
            fig = plt.gcf()
            figure_agg = draw_figure(window_three['-CANVAS-'].TKCanvas, fig)
