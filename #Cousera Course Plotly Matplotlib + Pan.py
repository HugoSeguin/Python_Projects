#Cousera Course Plotly Matplotlib + Pandas

import seaborn as sns
import pandas as pd
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as pyplot
from matplot lib import font_manager as fmgr
from pandas.plotting import autocorrelaiton_plot
import plot nien
from plotnine import ggplot.geom_line,aes

import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_object as go
import numpy as np

from datetime import datetime.timedelta

work_years = [1,2,3]
income = [1,2,3]

df = pd.Dataframe({'Years at work':work_years,'Income':income})

df.head()

#Line Plot
l_p = ggplot(data=df, mapping = aes(x="Years at work", y="Income"))

(l_p + plotnine.geom(color="blue")+ plotnine.lab(title = "simple line plot (Years/income)")).draw();

#MultiLine Plot

Ml_engineers_income = [2,3,4]


income_df = pd.Dataframe({'ML_engineers_income':ML_engineers_income, 'Years at work':work_years,'Income':income})

income_df.head()

(ggplot()+ 
plitnine.geom_line(data=income_df, mapping=ase (x="Years at Work", y="ML englineer nicome", colo ="blue"))+
plotnine.geom_line(data=income_df,mapping=aes(x="years at work", y="SDE income",color = red))+
plotnine.labs*tilte="Multine line plot")+
plotnine.scale_color_identity(guide='legend', name = "legend", breaks=("blue", "red"), labels= (["ML engineers income", "SFe Income"] )).draw()

#bar plot
df = sns.load_dataset('titanic')
df.head()

(plotnine.ggplot(data=df.dropna(), mapping = aes(x='pclass', y='fare', fill = 'sex'))+
plitnine.geom_col()+
plotnine.labs(title="Bar Plot of pasaenger clas vs fare")).draw()

#Scatter Plot

scatter_plot = ggplot (data=df, mapping=aes(x='pclass', y='fare'))

(scatter_plot +
plotnine.labs(title = 'Scatter plot for passenger class vs fare')+
plotnine.geom_point(shape='o', size=7, clolor="green", alpha=.7)).draw();

#Histogram

hist = ggplot(data=df, mapping=aes(x='alive'))

(hist + 
plotnine.lab(title="histogram of passenger status")+
plotnine.geom_histogram()+
plotnine.geom_rug()).draw()

#Density Plot


(de = ggplot(data=df,mapping = aes("age"))

(dke+
plotnine.geom_density()+
plotnine.lab(title="density plot for age of paseenger")).draw()

#Box plot

bp=ggplot(data=df.mapping=aes(x="embarked", y="fare"))

(bp+
plotnine.eom_boxplot()+
plotnine.labs(title="box plot for embarked vs fare")).draw()

#Violin Plot

bp=ggplot(data=df, mapping = aes(x="sex", y="age"))

(vp+
plotnine.geom_violin()+
plotnine.labs(title="violin plot for passenger age by gneder")+
plotnine.geom_jitter(position=plotnine.positon_jitter(0,3))).draw()





