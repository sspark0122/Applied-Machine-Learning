import numpy as np
import matplotlib.pyplot as plt

def getIris(path):
    data = []
    labels = []

    for line in open(path):
        tmp = line.split(",")
        if len(tmp) != 5:
            continue
        data.append([])
        tmp[-1] = tmp[-1][:-1]
        for i in range(len(tmp) - 1):
            data[-1].append(float(tmp[i]))
        labels.append(tmp[-1])

    return data, labels

data, labels = getIris("./iris.data.txt")
data = np.array(data)
labels = np.array(labels)

colors = {
    "Iris-setosa":"r",
    "Iris-versicolor":"g",
    "Iris-virginica":"b",
}
color_array = [colors[i] for i in labels]
cnt = 1
for i in range(4):
    for j in range(i+1,4):
        xs = np.array(data[:,i])
        ys = np.array(data[:,j])
        plt.subplot(2,3,cnt)
        cnt += 1
        plt.scatter(xs, ys, c=color_array)
plt.suptitle("Iris data (red=setosa, green=versicolor, blue=virginica)")
plt.savefig("plot.png")

# future reference:
# https://stackoverflow.com/questions/663171/is-there-a-way-to-substring-a-string-in-python
# https://www.pythonforbeginners.com/dictionary/python-split
# https://stackoverflow.com/questions/903853/how-do-you-extract-a-column-from-a-multi-dimensional-array
# https://matplotlib.org/gallery/subplots_axes_and_figures/figure_title.html
