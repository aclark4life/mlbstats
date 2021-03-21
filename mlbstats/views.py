from io import BytesIO

from django.http import HttpResponse
from django.utils import timezone
from django_pandas.io import read_frame
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.dates import DateFormatter, date2num
from matplotlib.figure import Figure

import pybaseball as pyb

from .models import Player


def spraychart(request):  # http://stackoverflow.com/a/5515994/185820
    """"""

    start_date = "2020-07-23"
    end_date = "2020-09-28"

    df = pyb.statcast_batter(start_date, end_date, 458015)

    home_df = df.loc[df["home_team"] == "CIN"]

    canvas = pyb.spraychart(
        home_df, "reds", title="Joey Votto: 2020 Season", colorby="launch_speed"
    )

    # write image data to a string buffer and get the PNG image bytes
    buf = BytesIO()
    canvas.print_png(buf)
    data = buf.getvalue()

    # write image bytes back to the browser
    return HttpResponse(data, content_type="image/png")


def spraychart2(request):  # http://stackoverflow.com/a/5515994/185820
    """"""

    players = Player.objects.all()

    df = read_frame(players)

    canvas = pyb.spraychart(
        df, "reds", title="Joey Votto: 2020 Season", colorby="launch_speed"
    )

    # write image data to a string buffer and get the PNG image bytes
    buf = BytesIO()
    canvas.print_png(buf)
    data = buf.getvalue()

    # write image bytes back to the browser
    return HttpResponse(data, content_type="image/png")
