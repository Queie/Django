from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
import datetime, random
import pandas as pd



# area 객체에 따라서 다르게 반응한다.
def text(request):
	return HttpResponse("kospi")


# Basic Line Chart
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

#def line_chart(request):
def index(request):

    df = pd.read_csv('sam.csv')
    fig,ax1=plt.subplots(1,1,dpi=100)
    plt.plot(df.Volume, 'r')
    plt.plot(df.Close, 'b')

    # django 로 그림을 출력
    canvas=FigureCanvas(fig)
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response



# Heat Map
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def heatmap(request):
    df = pd.read_csv('samsung.csv')
    fig,ax1=plt.subplots(1,1,dpi=400)
    sns.heatmap(df,cmap='RdBu_r',cbar=False, ax=ax1)
    canvas=FigureCanvas(fig)
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response



# Pi chart
from pylab import figure, axes, pie, title
from matplotlib.backends.backend_agg import FigureCanvasAgg

def pichart(request):

    f = figure(1,figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    fracs = [35,25,25, 15]
    explode=(0, 0.1, 0.05, 0.2)

    # 파이차트의 그림자등 속성
    pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)

    # Pi chart 의 타이틀
    title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})

    canvas = FigureCanvasAgg(f)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response



# Date Line Chart
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter

def date_chart(request):
    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response