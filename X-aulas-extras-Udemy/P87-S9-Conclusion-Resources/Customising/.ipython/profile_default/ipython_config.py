
c = get_config()
c.InlineBackend.figure_format = 'retina'
c.InlineBackend.rc.update({"figure.figsize": (7, 4), 'figure.dpi': 120})
c.InteractiveShellApp.matplotlib = "inline"
c.Completer.use_jedi = False