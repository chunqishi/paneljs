import streamlit as st
from streamlit_echarts import st_echarts

from constants import URL_PATH

# option = {
#     "xAxis": {
#         "type": "category",
#         "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
#     },
#     "yAxis": {"type": "value"},
#     "series": [{"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line"}],
# }

import requests

option = requests.get(f"http://127.0.0.1:8000{URL_PATH.PATH_ECHART}").json()

st.json(option)

st_echarts(
    options=option, height="400px",
)

