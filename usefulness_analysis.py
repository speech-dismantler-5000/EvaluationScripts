import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('survey.csv', sep=',')
useful = df.iloc[:,[6,8,4,10,12]]
x = ["Filler", "Frequency","Volume", "Transcript", "Playback"]
useful.columns = x
mean = useful.mean()
print(mean)
std = useful.std()
print(std)
p = mean.plot(kind="bar",legend=False,fontsize=16,yerr=std)
p.set_ylim(1,5)
p.set_title("Usefulness (averages) n=%d"%useful.shape[0], fontsize=20)
p.set_ylabel("Score (1-5)", fontsize=18)
p.set_xlabel("Feature", fontsize=18)
p.set_xticklabels(x,rotation = 45, ha="right")
plt.tight_layout()
plt.show()
