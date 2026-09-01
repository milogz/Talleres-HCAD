OK_FORMAT = True

test = {   'name': 'q1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> assert isinstance(fig, go.Figure), 'fig debe ser un go.Figure.'\n"
                                               ">>> assert len(fig.data) > 0, 'La figura debe contener al menos un "
                                               "trazo.'\n"
                                               ">>> assert isinstance(fig.data[0], go.Pie), 'El trazo debe ser un "
                                               "go.Pie.'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
