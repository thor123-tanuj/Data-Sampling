from os import name
import plotly.figure_factory as ff
import csv
import statistics
import pandas as pd
import random
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["average"].tolist()

def random_mean(counter) :
    data_Set = []
    for i in range(0 , counter) :
        random_index = random.randint(0 , len(data) - 1)
        value = data[random_index]
        data_Set.append(value)
    mean_new = statistics.mean(data_Set)
    return mean_new

def show_Figure(mean_new) :
    df = mean_new
    mean = statistics.mean(df)
    fig = ff.create_distplot([df] , ["average"] , show_hist = False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()
    
def setup() :
    mean_new = []
    for i in range(0 , 1000) :
        mean_set = random_mean(100)
        mean_new.append(mean_set)
        
    mean = statistics.mean(mean_new)
    print("Mean of Sampling Distribution :-",mean )
    show_Figure(mean_new)

setup()