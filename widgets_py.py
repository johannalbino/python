from ipywidgets import *
from IPython.display import display

w = widgets.Dropdown(options={'one':1, 'two':2}, value=2, description='Number : ')
display(w)