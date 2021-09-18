import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

print("Hi, Panadas")

df = pd.read_csv("wpd_datasets.csv")

x1 = df["X1"]
y1 = df["Y1"]

x2 = df["X2"]
y2 = df["Y2"]

x3 = df["X3"]
y3 = df["Y3"]

x4 = df["X4"]
y4 = df["Y4"]

# find the peaks using the Scipy package's argrelextreama function
# Ref: https://eddwardo.github.io/posts/2019-06-05-finding-local-extreams-in-pandas-time-series/
peak1 = argrelextrema(df.Y1.values, np.greater_equal, order=3)[0]
peak2 = argrelextrema(df.Y2.values, np.greater_equal, order=3)[0]
peak3 = argrelextrema(df.Y3.values, np.greater_equal, order=3)[0]
peak4 = argrelextrema(df.Y4.values, np.greater_equal, order=3)[0]

# print(peak1)
# print(peak2)
# print(peak3)
# print(peak4)


def generatePeakPoints(peakNumList, xValueList, yValueList):
    result = []
    for p in peakNumList:
        result.append((xValueList[p], yValueList[p]))

    return result


# peakPointList1 = generatePeakPoints(peak1, x1, y1)
# peakPointList2 = generatePeakPoints(peak2, x2, y2)
# peakPointList3 = generatePeakPoints(peak3, x3, y3)
# peakPointList4 = generatePeakPoints(peak4, x4, y4)


def plotPeakPoints(listOfPeakPoints):
    good = "go"
    bad = "rv"

    if len(listOfPeakPoints) > 2:
        color = bad
    else:
        color = good

    for x, y in listOfPeakPoints:
        plt.plot(x, y, color)

def addPeaksInPlot(peakNumList, xValueList, yValueList):
    peakPointList = generatePeakPoints(peakNumList, xValueList, yValueList)

    good = "go"
    bad = "rv"


    if len(peakPointList) > 2:
        color = bad
        text = "Bad"
        boxColor = "red"
    else:
        color = good
        text = "Good"
        boxColor = "green"

    for x, y in peakPointList:
        plt.plot(x, y, color)

    plt.text(xValueList.mean(), yValueList.mean(), text, fontsize=12,
             bbox=dict(facecolor=boxColor, alpha=0.5))




plt.figure(1)
plt.subplot(2, 2, 1)
plt.plot(x1, y1)
addPeaksInPlot(peak1, x1, y1)

plt.figure(1)
plt.subplot(2, 2, 2)
plt.plot(x2, y2)
addPeaksInPlot(peak2, x2, y2)

plt.figure(1)
plt.subplot(2, 2, 3)
plt.plot(x3, y3)
addPeaksInPlot(peak3, x3, y3)

plt.figure(1)
plt.subplot(2, 2, 4)
plt.plot(x4, y4)

addPeaksInPlot(peak4, x4, y4)

plt.show()

# import matplotlib.pyplot as plt
#
# fig, ax = plt.subplots(2, 2)
# x = [1, 2]
# y = [1, 2]
#
# ax[0, 0].plot(x, y)
# ax[0, 1].plot(x, y)
# ax[1, 0].plot(x, y)
#
# ax[1, 1].set_axis_off()
# ax[1, 1].text(0.5, 0.5, 'my text');
