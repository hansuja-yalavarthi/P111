import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean = statistics.mean(data)
stdev = statistics.stdev(data)
def randomSetOfMean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
mean_list = []
for i in range(0, 100):
    setOfMeans = randomSetOfMean(30)
    mean_list.append(setOfMeans)
stdev = statistics.stdev(mean_list)
first_stdev_start, first_stdev_end = mean - stdev, mean + stdev
second_stdev_start, second_stdev_end = mean - (2 * stdev), mean + (2 * stdev)
third_stdev_start, third_stdev_end = mean - (3 * stdev), mean + (3 * stdev)

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean_sample = statistics.mean(data)
print("Mean of sample: ", mean_sample)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_sample, mean_sample], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()
zScore = (mean-mean_sample)/stdev
print("z-score is: ", zScore)