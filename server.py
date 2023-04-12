from fastapi import FastAPI

from constants import URL_PATH

app = FastAPI()


@app.get(URL_PATH.PATH_ROOT)
async def root():
    return {"message": "Hello World"}


@app.get(URL_PATH.PATH_ECHART)
async def echart():
    import numpy as np
    import pandas as pd
    from dataframe_echarts import DataFrameEcharts
    Index = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
    Cols = ['A', 'B', 'C', 'D']
    df = pd.DataFrame(abs(np.random.randn(5, 4)), index=Index, columns=Cols)
    print(df)
    opts = DataFrameEcharts(df).to_heatmap_json()
    return opts


def start():
    import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    uvicorn.run(app, port=8000)


if __name__ == "__main__":
    start()
