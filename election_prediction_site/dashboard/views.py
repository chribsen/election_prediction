from django.shortcuts import render, render_to_response
import mpld3
import pandas as pd

def home(request):
    import matplotlib.pyplot as plt, mpld3
    fig = plt.figure()
    plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
    figure = mpld3.fig_to_html(fig)
    return render_to_response('election_prediction_site/index.html', {'figure': figure})