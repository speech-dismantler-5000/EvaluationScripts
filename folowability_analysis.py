import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('survey.csv', sep=',')
useful = df.iloc[:,[14,16,18,20,22]]
print(useful)

x = ["Filler", "Frequency", "Volume", "Transcript", "Playback"]
useful.columns = x
mean = useful.mean()
std = useful.std()
print(mean)
print(std)
p = mean.plot(kind="bar",legend=False,fontsize=16,yerr=std)
p.set_ylim(1,5)
p.set_title("Followability (averages) n=%d"%useful.shape[0], fontsize=20)
p.set_ylabel("Score (1-5)", fontsize=18)
p.set_xlabel("Feature", fontsize=18)
p.set_xticklabels(x,rotation = 45, ha="right")
plt.tight_layout()
plt.show()