import pandas as pd
c =30
df = pd.DataFrame([c + x for x in range(0,30)],index=[*range(1,31,1)],columns=['Temperature (c)'])
df.plot(color ="red", title ="Temperature (c) vs Day (d)")