import datetime as dt
import matplotlib.pyplot as plt

def save_graph(filename):
    now = dt.datetime.now()
    date_string = now.strftime("%m%d_%Hh%Mm")
    plt.savefig(f'images/{filename}_{date_string}.png')
    print(f'graph saved as {filename}_{date_string}.png')
