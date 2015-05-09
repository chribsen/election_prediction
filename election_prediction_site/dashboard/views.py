from django.shortcuts import render, render_to_response
import numpy as np
import matplotlib.pyplot as plt, mpld3
import mpld3
from pywordcloud import pywordcloud

def home(request):
    import matplotlib.pyplot as plt, mpld3

    # Graph
    fig = plt.figure()
    x = [4,12,14,4,22,18]
    y = [3,10,16,3,20,17]
    plt.plot([1,2,3,4], [1,4,9,16], mec='w', mew=5, ms=20)
    graph1 = mpld3.fig_to_html(fig)

    # Graph 2
    fig = plt.figure()
    plt.plot([1,2,3,4], [1,4,9,16], 'ro')
    graph2 = mpld3.fig_to_html(fig)


    # Histogram
    fig = plt.figure()
    ax = fig.add_subplot(111, axisbg='#EEEEEE')
    ax.grid(color='white', linestyle='solid')

    x = np.random.normal(size=1000)
    ax.hist(x, 30, histtype='stepfilled', fc='lightblue', alpha=0.5);
    histogram = mpld3.fig_to_html(fig)

    return render_to_response('election_prediction_site/index.html', {'graph1': graph1,'graph2':graph2, 'histogram':histogram})





class PlotFactory:

    def get_graph(self, x, y):
        fig = plt.figure()

        plt.plot(x, y, mec='w', mew=5, ms=20)
        figure = mpld3.fig_to_html(fig)
        return figure

    def get_wordcloud(self, corpus, using='pywordcloud'):
        #mask = imread("stormtrooper_mask.png")
        #wc = WordCloud(max_words=1000, mask=mask, margin=10,
        #       random_state=1).generate(corpus)
        #return wc.to_html()

        return pywordcloud.create(corpus,
            outfile="wordcloud.html",
            uppercase=False,
            showfreq=True,
            frequency=100,
            removepunct = False,
            minfont = 1.5,
            maxfont = 6,
            hovercolor="green",
            showborder=False,
            fontfamily='calibri',
            width="1000px",
            height="400px",
            #colorlist = ["red","blue","yellow","black","green"]
        )

    def get_histogram(self, x):
        fig = plt.figure()