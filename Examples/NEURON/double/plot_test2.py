import pandas
import matplotlib.pyplot as plt

table = pandas.read_csv("iclamp.dend.output", sep=" ")

plt.plot(table["t"], table["somaA.v"])
plt.savefig("test2_soma.svg")
plt.close()

plt.plot(table["t"], table["dend.v"])
plt.savefig("test2_dend.svg")
plt.close()
