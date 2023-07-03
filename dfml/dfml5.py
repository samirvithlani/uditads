import pandas as pd

subjects = ["Maths","English","Science","Social","Hindi","Sanskrit","Computer","Chem"]
stress =[9,3,5,1,2,4,6,7]
grades =[15,10,7,8,11,9,12,13]

df = pd.DataFrame(list(zip(stress,grades)),index = subjects,columns=['Stress','Grades'])

print(df)
df.plot()