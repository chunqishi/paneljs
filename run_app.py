'''

https://docs.streamlit.io/library/cheatsheet

'''


def start():
    import pathlib
    from streamlit.web import bootstrap
    app_path = str(pathlib.Path(__file__).parent.joinpath('app.py'))
    bootstrap.run(app_path, '', [], flag_options={})


if __name__ == "__main__":
    start()
