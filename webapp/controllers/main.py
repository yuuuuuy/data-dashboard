import random
import datetime
from os import path
from flask import Blueprint, render_template
from pyecharts import HeatMap

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder=path.join(path.pardir, 'templates', 'analysis'),
    url_prefix='/home')


@main_blueprint.route('/', methods=['GET'])
def home():
    hm = create_heatmap()
    return render_template('index.html', hm=hm)


def create_heatmap():
    begin = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 12, 31)
    data = [[str(begin + datetime.timedelta(days=i)),
             random.randint(1000, 25000)] for i in
            range((end - begin).days + 1)]
    heatmap = HeatMap("日历热力图示例", "某人 2017 年微信步数情况", width=1100)
    heatmap.add("", data, is_calendar_heatmap=True,
                visual_text_color='#000', visual_range_text=['', ''],
                visual_range=[1000, 25000], calendar_cell_size=['auto', 30],
                is_visualmap=True, calendar_date_range="2017",
                visual_orient="horizontal", visual_pos="center",
                visual_top="80%", is_piecewise=True)
    return heatmap
