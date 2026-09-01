OK_FORMAT = True

test = {   'name': 'q3',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> assert isinstance(fig, go.Figure), 'fig debe ser un go.Figure.'\n"
                                               ">>> assert isinstance(fig.data[0], go.Scatter), 'El trazo debe ser un "
                                               "go.Scatter.'\n"
                                               ">>> assert 'markers' in (fig.data[0].mode or 'markers'), 'El modo debe "
                                               "incluir markers.'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
