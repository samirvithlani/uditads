import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame[{
    'Name':["raj","ram","ravi","raju"],
    'Age':[20,21,25,23],
}]

df.plot(x="Name",y="Age",kind="bar")
