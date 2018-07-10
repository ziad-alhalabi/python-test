import os
import pandas as pd
import matplotlib.pyplot as plt


#newpath = r'results'
#if not os.path.exists(newpath):
#    os.makedirs(newpath)


# Data to plot
labels = 'Camden', 'Paddington', 'Stratford', 'Greenwich'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.savefig('pollution.png')



df = pd.DataFrame(pd.np.random.randint(10, 35, size=(7, 4)), columns=list('ABCD'))

df = df.rename(columns={'A': 'London', 'B': 'Liverpool'})

ax = df[['London','Liverpool']].plot(kind='bar', title ="Difference in Temperature", figsize=(15, 10), legend=True, fontsize=12)
ax.set_xlabel("Date", fontsize=12)
ax.set_ylabel("Temperature", fontsize=12)

plt.savefig('temperature.png')


print("London Weather:")
print(df['London'].describe())


print("Liverpool Weather:")
print(df['London'].describe())
