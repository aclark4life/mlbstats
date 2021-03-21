from django.http import HttpResponse
from django.utils import timezone
from io import BytesIO
from matplotlib.dates import DateFormatter
from matplotlib.dates import date2num
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg


import pybaseball as pyb


def spraychart(request):  # http://stackoverflow.com/a/5515994/185820
    """"""

    start_date = '2020-07-23'
    end_date = '2020-09-28'

    df = pyb.statcast_batter(start_date, end_date, 458015)

    home_df = df.loc[df['home_team'] == 'CIN']

    costs = [[3000, "2018-01-01"], [4000, "2018-02-01"], [3000, "2018-03-01"]]
    grosses = [[10000, "2018-01-01"], [30000, "2018-02-01"], [20000, "2018-03-01"]]
    nets = [[25000, "2018-01-01"], [26000, "2018-02-01"], [27000, "2018-03-01"]]

    # Cost
    x1 = [  # http://matplotlib.org/examples/api/date_demo.html
        date2num(timezone.datetime.strptime(i[1], "%Y-%m-%d")) for i in costs
    ]
    y1 = [i[0] for i in costs]
    # Gross
    x2 = [date2num(timezone.datetime.strptime(i[1], "%Y-%m-%d")) for i in grosses]
    y2 = [i[0] for i in grosses]
    # Net
    x3 = [date2num(timezone.datetime.strptime(i[1], "%Y-%m-%d")) for i in nets]
    y3 = [i[0] for i in nets]

    # figure = Figure()
    # canvas = FigureCanvasAgg(figure)

    # axes = figure.add_subplot(1, 1, 1)
    # axes.grid(True)
    # axes.plot(x1, y1)
    # axes.plot(x2, y2)
    # axes.plot(x3, y3)
    # axes.xaxis.set_major_formatter(DateFormatter("%m"))

    canvas = pyb.spraychart(home_df, 'reds', title='Joey Votto: 2020 Season',colorby='launch_speed')

    # write image data to a string buffer and get the PNG image bytes
    buf = BytesIO()
    canvas.print_png(buf)
    data = buf.getvalue()
    # write image bytes back to the browser
    return HttpResponse(data, content_type="image/png")
