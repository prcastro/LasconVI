import pandas
import matplotlib.pyplot as plt

table = pandas.read_csv("iclamp.somaA.output", sep=" ")

plt.plot(table["t"], table["somaA.v"])
plt.savefig("test1_soma.svg")
plt.close()

plt.plot(table["t"], table["dend.v"])
plt.savefig("test1_dend.svg")
plt.close()
