'''

https://echarts.apache.org/examples/en/index.html#chart-type-heatmap


'''

import pandas as pd

import json


class DataFrameEcharts:

    def __init__(self, dataframe: pd.DataFrame = None):
        self.dataframe = dataframe

    def to_heatmap(self, dataframe=None):
        '''

        :return: json
        '''
        df = dataframe or self.dataframe
        xs = df.columns.tolist()
        ys = df.index.tolist()

        from pyecharts.charts import HeatMap
        from pyecharts import options as opts
        chart = HeatMap()
        array = df.to_numpy()
        values = []
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                values.append([j, i, array[i][j]])

        chart.add_xaxis(xs)
        chart.add_yaxis("", ys, values,
                        label_opts=opts.LabelOpts(is_show=True))
        chart.set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=array.min(), max_=array.max()))
        return chart

    def to_heatmap_json(self, dataframe=None):
        '''

        :return: json
        '''
        df = dataframe or self.dataframe
        xs = df.columns.tolist()
        ys = df.index.tolist()

        array = df.to_numpy()
        values = []
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                values.append([j, i, array[i][j]])

        opts = {
            "xAxis": {
                "data": xs,
            },
            "yAxis": {
                "data": ys
            },
            "series": [
                {
                    "data": values,
                    "type": "heatmap",
                    "label": {
                        "show": True
                    }
                }
            ],
            "visualMap": {
                "min": array.min(),
                "max": array.max(),
                "calculable": True,
                "orient": 'horizontal',
                "left": 'center',
                "top": '0%'
            }
        }
        return opts


if __name__ == "__main__":
    import numpy as np

    Index = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
    Cols = ['A', 'B', 'C', 'D']
    df = pd.DataFrame(abs(np.random.randn(5, 4)), index=Index, columns=Cols)
    print(df)

    # opts = DataFrameEcharts(df).to_heatmap().dump_options()
    # print(opts)
    DataFrameEcharts(df).to_heatmap().render('heatmap.html')
