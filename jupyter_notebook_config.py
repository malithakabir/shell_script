c = get_config()  # Get the config object.
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False  # Do not open a browser window by default when using notebooks.
c.NotebookApp.password = 'SHA1_KEY'
