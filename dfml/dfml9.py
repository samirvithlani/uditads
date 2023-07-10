import pandas as pd
from IPython.display import display

def highlight_colors(s):
    color = 'red' if s <6 else 'blue'
    return 'background-color: %s' % color

df =pd.DataFrame({'A':[14,4,5,4,1],'B':[5,2,54,3,2],'C':[20,20,7,3,8],'D':[14,3,6,2,6],'E':[5,2,6,4,2],'F':[20,20,7,3,8]})
display(df.style.applymap(highlight_colors))
