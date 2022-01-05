import pandas as pd

df = pd.read_csv("Class_130.csv")

df['Radius']=df['Radius'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

radius = df["Radius"].tolist()
mass = df["Mass"].tolist()
gravity = []

def convertSI(radius, mass):
    for i in range(0, len(radius)):
        radius[i] = radius[i]*1.989e+30
        mass[i] = mass[i]*6.957e+8

convertSI(radius, mass)

def acceleration_due_to_gravity(radius, mass):
    G = 6.674e-11
    for index in range(0,len(mass)):
        g = (mass[index]*G)/((radius[index]**2))
        gravity.append(g)

acceleration_due_to_gravity(radius, mass)


df["Gravity"] = gravity
df[""] = "SR.NO/"

df.to_csv("Fianl-131.csv")