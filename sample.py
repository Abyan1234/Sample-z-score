

import pandas as pd 
import csv 
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics 
import random 


df = pd.read_csv("studentMarks.csv") 
data = df["Math_score"].tolist() 
 


def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,100):
    set_of_means=random_set_of_mean(30)
    mean_list.append(set_of_means)
std_deviation=statistics.stdev(mean_list)
mean=statistics.mean(set_of_means)

first_std_devitation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)
print("std1:= ",first_std_devitation_start,first_std_deviation_end) 
print("std2:= ",second_std_deviation_start,second_std_deviation_end) 
print("std1:= ",first_std_devitation_start,first_std_deviation_end) 

fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_std_devitation_start,first_std_devitation_start],y=[0,0.17],mode="lines",name="standard deviation 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="standard deviation 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="standard deviation 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="standard deviation 2"))

fig.show()

sample1=mean
z_score=(sample1/mean)/std_deviation

print("This is sample1:= ",sample1)
print("This is z_score:= ",z_score)
print("mean of sampling distribution:- ",mean) 
print("Standard deviation of sampling distribution:- ",std_deviation)
    


fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False) 
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.20], mode="lines", name="MEAN")) 
fig.show()

