import pandas as pd

data = [
    {
        "Name":"raj","Age":20,"City":"Delhi","Address":"Mg road, new delhi"
    },
    {
        "Name":"ajay","Age":25,"City":"Mumbai","Address":"Mg road, Borivali"
    },
    {
        "Name":"parth","Age":24,"City":"Mumbai","Address":"Near mcd, Mumbai"
    },
    {
        "Name":"priya","Age":28,"City":"Bangalore","Address":"Mg road, Bangalore"
    },
    {
        "Name":"Mit","Age":30,"City":"Ahmedabad","Address":"Mg road, Ahmedabad"
    }
]

df = pd.DataFrame(data)
#print(df)

#df = df.loc[df["Age"]>25]
#df = df.query("Age>25")
# df = df.query("Address.str.contains('mg',case=False)")
# print(df)

def contains_mg(address):
    return "mg" in address.lower()

#df  =df[df["Address"].apply(contains_mg)]
#df =  df[df["Address"].map(contains_mg)]
#df = df.filter(like="Address")

print(df)
