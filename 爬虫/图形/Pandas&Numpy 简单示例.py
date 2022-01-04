import pandas as pd
import numpy as np
from pyecharts import Bar

title = "bar chart"
index = pd.date_range('3/8/2017',periods=6,freq="M")
df1=pd.DataFrame(np.random.randn(6),index=index)
df2=pd.DataFrame(np.random.randn(6),index=index)

dtvule1=[i[0] for i in df1.values]
dtvule2=[i[0] for i in df2.values]

_index=[i for i in df1.index.format()]

bar=Bar(title,"test111111")
bar.add('profit',_index,dtvule1)
bar.add('loss',_index,dtvule2)
bar.render("reder.html")